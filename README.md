# Drowsiness Detection System using CNN & OpenCV

```{=html}
<p align="center">
```
`<img src="model.png" width="650">`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<b>`{=html}Real-Time Driver Drowsiness Detection using Deep
Learning`</b>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## Overview

Driver drowsiness is one of the primary causes of road accidents
worldwide. Long driving hours, fatigue, stress, and sleep deprivation
significantly reduce alertness and reaction time.

This project implements a real-time Drowsiness Detection System using:

-   Python\
-   OpenCV\
-   Convolutional Neural Networks (CNN)\
-   Keras (TensorFlow backend)

The system continuously monitors the driver's eyes through a webcam and
triggers an alert when prolonged eye closure is detected.

------------------------------------------------------------------------

## Key Features

-   Real-time webcam monitoring\
-   Eye detection using Haar Cascades\
-   CNN-based eye state classification\
-   Immediate alert system\
-   Lightweight and easy to deploy\
-   Compatible with standard webcams

------------------------------------------------------------------------

## System Workflow

1.  Webcam captures live video feed.\
2.  OpenCV detects face and extracts eye regions.\
3.  The CNN model classifies each eye as Open or Closed.\
4.  If eyes remain closed beyond a defined threshold, an alarm is
    triggered.

------------------------------------------------------------------------

## Dataset

The model is trained on a subset of the following Kaggle dataset:

https://www.kaggle.com/serenaraju/yawn-eye-dataset-new

The dataset contains labeled images for:

-   Open Eyes\
-   Closed Eyes

------------------------------------------------------------------------

## Model Architecture

```{=html}
<p align="center">
```
`<img src="model.png" width="750">`{=html}
```{=html}
</p>
```
The CNN architecture consists of:

-   Convolution Layers\
-   ReLU Activation\
-   MaxPooling Layers\
-   Fully Connected Layers\
-   Softmax Output Layer

------------------------------------------------------------------------

## Installation & Setup

### Step 1 --- Clone the Repository

``` bash
git clone https://github.com/adamfutur/Drowsiness-Detection-System-CNN-OpenCV.git
```

### Step 2 --- Navigate to Project Directory

``` bash
cd Drowsiness-Detection-System-CNN-OpenCV
```

### Step 3 --- Install Required Dependencies

``` bash
pip install -r requirements.txt
```

If requirements.txt is not available:

``` bash
pip install opencv-python keras tensorflow numpy pygame
```

------------------------------------------------------------------------

## Run the Application

``` bash
python detect_drowsiness.py
```

Make sure your webcam is connected before running the script.

------------------------------------------------------------------------

## Project Structure

    Drowsiness-Detection-System-CNN-OpenCV/
    │
    ├── dataset/
    ├── models/
    ├── detect_drowsiness.py
    ├── model.h5
    ├── alarm.wav
    ├── model.png
    └── README.md

------------------------------------------------------------------------

## Requirements

-   Python 3.7+
-   OpenCV
-   TensorFlow / Keras
-   NumPy
-   Pygame

------------------------------------------------------------------------

## Future Improvements

-   Improve accuracy using larger datasets\
-   Add head pose estimation\
-   Deploy as a mobile or embedded system application\
-   Integrate with vehicle safety systems

------------------------------------------------------------------------

## License

This project is open-source .
