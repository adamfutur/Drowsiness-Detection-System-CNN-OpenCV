
---

# 🚗 Drowsiness Detection System

> **Real-time driver fatigue monitoring using Deep Learning (CNN) & OpenCV.**

---

## 📌 Overview

Driver drowsiness is a leading cause of road accidents worldwide. This system leverages **Computer Vision** and **Convolutional Neural Networks (CNN)** to monitor a driver’s eye state in real-time, triggering an immediate alert if signs of fatigue are detected.

### 🛠️ Tech Stack

* **Python** (Primary Language)
* **OpenCV** (Video Capture & Facial Landmarks)
* **Keras / TensorFlow** (Model Backend)
* **Pygame** (Audio Alert System)

---

## ⚡ Key Features

* ✅ **Real-time Monitoring:** Continuous webcam tracking with low latency.
* ✅ **Robust Detection:** Face and eye detection using Haar Cascades.
* ✅ **CNN Classification:** Accurate eye-state (Open/Closed) classification.
* ✅ **Audio Alert:** Immediate alarm trigger for safety thresholds.
* ✅ **Lightweight:** Designed to run efficiently on standard hardware.

---

## 🧠 System Workflow

1. **Capture:** The system captures live video frames via webcam.
2. **Detection:** OpenCV identifies the facial region and isolates the eyes.
3. **Classification:** A pre-trained CNN model predicts the eye state.
4. **Action:** If eyes remain closed for a pre-defined period (Threshold), a loud audio alarm is triggered.

---

## 📊 Dataset & Architecture

The model is trained on a refined subset of the **[Kaggle Yawn-Eye Dataset](https://www.kaggle.com/serenaraju/yawn-eye-dataset-new)**.

### CNN Model Summary

| Layer (Type) | Description |
| --- | --- |
| **Convolutional** | Feature extraction for eye edges and textures. |
| **ReLU** | Non-linear activation for faster training. |
| **MaxPooling** | Spatial downsampling to reduce parameters. |
| **Dense / Softmax** | Final classification into "Open" or "Closed." |

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/adamfutur/Drowsiness-Detection-System-CNN-OpenCV.git
cd Drowsiness-Detection-System-CNN-OpenCV

```

### 2. Set Up Environment

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
# If requirements.txt is missing:
pip install opencv-python keras tensorflow numpy pygame

```

### 3. Run the Application

```bash
python detect_drowsiness.py

```

---

## 📁 Project Structure

```bash
├── dataset/             # Training data
├── models/              # Model weights & structure
├── detect_drowsiness.py # Main execution script
├── model.h5             # Pre-trained CNN model
├── alarm.wav            # Alert sound file
├── model.png            # Model visualization
└── README.md            # Project documentation

```

---

## 🔮 Future Improvements

* [ ] **Yawn Detection:** Add monitoring for excessive yawning.
* [ ] **Head Pose Estimation:** Detect if the driver's head is nodding off.
* [ ] **Embedded Deployment:** Optimize for Raspberry Pi or NVIDIA Jetson.
* [ ] **Mobile App:** Port to Android/iOS for dashboard mounting.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---
