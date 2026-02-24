import cv2
import numpy as np
import pygame
from keras.models import load_model
from keras.preprocessing.image import img_to_array

# Initialiser pygame
pygame.mixer.init()

def start_alarm(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(-1)  # boucle infinie

# Utiliser les Haar cascades intégrées à OpenCV (plus sûr)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
left_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_lefteye_2splits.xml")
right_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_righteye_2splits.xml")

cap = cv2.VideoCapture(0)
model = load_model("trained_model.h5")

count = 0
alarm_on = False
alarm_sound = "data/alarm.mp3"

status1 = 'Open'
status2 = 'Open'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    prob1 = 0.0
    prob2 = 0.0

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]

        left_eye = left_eye_cascade.detectMultiScale(roi_gray)
        right_eye = right_eye_cascade.detectMultiScale(roi_gray)

        # LEFT EYE
        for (x1, y1, w1, h1) in left_eye:
            eye1 = roi_gray[y1:y1+h1, x1:x1+w1]
            eye1 = cv2.resize(eye1, (24, 24))
            eye1 = eye1.astype('float') / 255.0
            eye1 = img_to_array(eye1)
            eye1 = np.expand_dims(eye1, axis=0)

            pred1 = model.predict(eye1, verbose=0)
            prob1 = float(pred1[0][0])
            status1 = 'Closed' if prob1 < 0.5 else 'Open'
            break

        # RIGHT EYE
        for (x2, y2, w2, h2) in right_eye:
            eye2 = roi_gray[y2:y2+h2, x2:x2+w2]
            eye2 = cv2.resize(eye2, (24, 24))
            eye2 = eye2.astype('float') / 255.0
            eye2 = img_to_array(eye2)
            eye2 = np.expand_dims(eye2, axis=0)

            pred2 = model.predict(eye2, verbose=0)
            prob2 = float(pred2[0][0])
            status2 = 'Closed' if prob2 < 0.5 else 'Open'
            break

        # Affichage terminal
        print(f"Left: {status1} ({prob1:.3f}) | Right: {status2} ({prob2:.3f})")

        #  LOGIQUE ALARME APRÈS 3 CLOSED
        if status1 == 'Closed' and status2 == 'Closed':
            count += 1
            print(f"⚠️ CLOSED COUNT: {count}")

            if count >= 3:
                print("🚨 DROWSINESS ALERT !!!")
                if not alarm_on:
                    alarm_on = True
                    start_alarm(alarm_sound)
        else:
            count = 0
            if alarm_on:
                pygame.mixer.music.stop()
                alarm_on = False

    cv2.imshow("Drowsiness Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()
