# Hand Gesture Controlled Presentation System

## Overview

The Hand Gesture Controlled Presentation System is a computer vision-based application that enables users to control presentation slides using hand gestures instead of a keyboard or mouse. The system uses a webcam to capture hand movements and recognizes specific gestures in real time to perform actions such as moving to the next slide, returning to the previous slide, displaying a pointer, drawing annotations, and erasing annotations.

The project is developed using Python and leverages OpenCV, CVZone, MediaPipe, NumPy, and PyQt5 for hand tracking, gesture recognition, image processing, and graphical user interface development.

---

## Features

- Control presentation slides using hand gestures.
- Navigate to the next slide.
- Navigate to the previous slide.
- Display a virtual pointer on slides.
- Draw annotations directly on presentation slides.
- Erase previously drawn annotations.
- Real-time webcam feed display.
- User-friendly graphical interface.

---

## Technologies Used

- Python
- OpenCV
- CVZone
- MediaPipe
- NumPy
- PyQt5

---

## Project Structure

```text
HandGesturePresentation/
│
├── app.py
├── main.py
│
└── Presentation/
    ├── slide1.jpg
    ├── slide2.jpg
    ├── slide3.jpg
```

---

## Prerequisites

Before running the project, ensure the following software is installed:

- Python 3.8 or above
- Webcam
- Internet connection (for installing required packages)

---

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd HandGesturePresentation
```

### Step 2: Install Required Packages

```bash
pip install opencv-python
pip install cvzone
pip install mediapipe
pip install numpy
pip install pyqt5
```

Alternatively:

```bash
pip install opencv-python cvzone mediapipe numpy pyqt5
```

---

## Preparing Presentation Slides

The project requires presentation slides in image format.

You can create slides using Microsoft PowerPoint and export them as JPG or PNG images.

Place all slide images inside the Presentation folder.

Example:

```text
Presentation/
├── slide1.jpg
├── slide2.jpg
├── slide3.jpg
├── slide4.jpg
└── slide5.jpg
```

---

## How to Run the Project

### Run the GUI Application

```bash
python app.py
```

A window titled **Hand Gesture Controlled Presentation** will appear.

Click the **Start Presentation** button to launch the gesture-controlled presentation system.

### Run the Presentation Module Directly

```bash
python main.py
```

---

## Hand Gestures and Their Functions

| Gesture | Function |
|----------|----------|
| Thumb Up | Move to Next Slide |
| Pinky Finger Up | Move to Previous Slide |
| Index + Middle Finger Up | Show Pointer |
| Index Finger Up | Draw Annotation |
| Index + Middle + Ring Finger Up | Erase Annotation |

---

## System Workflow

### Step 1: Webcam Initialization

The webcam captures live video frames from the user.

### Step 2: Hand Detection

MediaPipe and CVZone detect the user's hand and identify hand landmarks.

### Step 3: Finger Detection

The system determines which fingers are raised based on landmark positions.

### Step 4: Gesture Recognition

Specific finger combinations are matched to predefined gestures.

### Step 5: Slide Control

Based on the detected gesture, the system performs actions such as:

- Moving to the next slide
- Moving to the previous slide
- Displaying a pointer
- Drawing annotations
- Erasing annotations

### Step 6: Display Output

The selected slide along with the webcam feed is displayed on the screen in real time.

---

## Applications

- Smart Classrooms
- Online Learning Platforms
- Business Presentations
- Training Sessions
- Seminars and Workshops
- Interactive Learning Systems
- Touchless Human-Computer Interaction

---

## Advantages

- Eliminates the need for a mouse or keyboard during presentations.
- Provides a natural and interactive user experience.
- Supports real-time gesture recognition.
- Enables touchless presentation control.
- Improves audience engagement.
- Easy to set up and use.

---

## Limitations

- Requires adequate lighting conditions.
- Performance depends on webcam quality.
- Supports only predefined gestures.
- Limited to single-hand tracking.
- Accuracy may decrease with background interference.

---

## Future Enhancements

- Voice command support.
- PDF presentation support.
- Multi-hand gesture recognition.
- AI-based custom gesture training.
- Cloud storage integration.
- Gesture customization options.
- Mobile device integration.

---

## Libraries Used

### OpenCV

OpenCV is used for image processing, webcam access, and displaying images.

### MediaPipe

MediaPipe provides real-time hand landmark detection.

### CVZone

CVZone simplifies hand tracking and gesture recognition using MediaPipe.

### NumPy

NumPy is used for numerical operations and coordinate calculations.

### PyQt5

PyQt5 is used to create the graphical user interface.

---

## Conclusion

The Hand Gesture Controlled Presentation System demonstrates the practical application of computer vision and gesture recognition technologies in creating a touchless presentation environment. By combining OpenCV, MediaPipe, and CVZone, the system provides an efficient and interactive way to control presentations using natural hand movements. This project highlights the potential of human-computer interaction through gesture-based interfaces and can be further extended with advanced AI capabilities.

---

## Author

Usha P

## License

This project is developed for educational and learning purposes.