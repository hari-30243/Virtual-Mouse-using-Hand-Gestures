🖱️ Virtual Mouse Using Hand Gestures

A real-time touchless virtual mouse system that allows users to control mouse movement, clicking, and scrolling using hand gestures captured via a webcam, without any physical input device.

📌 Overview

This project uses computer vision and hand landmark detection to interpret hand gestures and map them to system-level mouse actions.
It demonstrates a practical Human–Computer Interaction (HCI) application using real-time video processing.

The system works entirely on CPU and does not require any external sensors or hardware.

❓ Problem Statement

Traditional input devices such as a mouse or touchpad:

Require physical contact

Are not accessible for all users

Are inconvenient in hands-free or hygienic environments

This project solves the problem by enabling hands-free computer interaction using only a webcam and hand gestures.

🎯 Features

☝️ Move mouse cursor using index finger

🤏 Click using finger pinch gesture

✌️ Continuous vertical scrolling (up/down)

🤟 Continuous horizontal scrolling (left/right)

✊ Stop / pause interaction using fist

⚡ Real-time performance with low latency

🧼 Clean UI (no landmark overlay in final output)

🛠️ Technologies Used

Python 3.10

OpenCV – Webcam access and video processing

MediaPipe – Real-time hand detection and landmark tracking

PyAutoGUI – Mouse and scroll automation

NumPy – Coordinate mapping and geometric calculations

Virtual Environment (venv) – Dependency isolation

🧠 System Workflow

Webcam captures live video frames

Frames are processed using OpenCV

MediaPipe detects hand and finger landmarks

Rule-based logic determines the gesture

Gesture is mapped to mouse/scroll action

System responds in real time

🖐️ Gesture Mapping
Gesture	Action
☝️ Index finger	Move mouse
✌️ Two fingers	Scroll up / down
🤟 Three fingers	Scroll left / right
🤏 Index + middle close	Click
✊ Fist	Stop interaction
📁 Project Structure
HandGestureControl/
│
├── main.py        # Main application file
├── venv/          # Virtual environment (ignored in GitHub)
└── README.md      # Project documentation

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/virtual-mouse.git
cd virtual-mouse

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate

3️⃣ Install Dependencies
pip install opencv-python mediapipe pyautogui numpy

4️⃣ Run the Application
python main.py


Press q to exit.

📈 Results & Performance

Runs at ~30 FPS on CPU

Stable real-time gesture detection

Accurate mouse control with minimal jitter

Smooth continuous scrolling

No machine learning training required

🚀 Future Enhancements

Add gesture-based volume control

Enable/disable gesture mode using a specific gesture

Improve cursor smoothing using filtering

Support left and right hand detection

Convert into a desktop application

👨‍💻 Author

Hari Haran
B.Tech Student
Aspiring Software / AI Engineer

📜 License

This project is for educational and internship demonstration purposes.
