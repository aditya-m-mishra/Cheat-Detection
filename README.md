# AI Exam Cheating Detector

An AI-powered computer vision application that detects suspicious exam behavior using a webcam.  
The system analyzes face presence and head position to identify possible cheating activities such as looking away, multiple people in frame, or absence of a person.

---

##  Features

- Real-time face detection using OpenCV  
- Detects:
  - No person in frame  
  - Multiple people in frame  
  - Looking away from screen  
- Displays live status on screen  
- Maintains a cheating score counter  
- Lightweight and easy-to-run Python project  

---

##  Tech Stack

- Python 3.8+  
- OpenCV  
- NumPy  
- MediaPipe  

---

##  Project Structure

examCheat_detector/
│
├── main.py
├── utils.py
├── requirements.txt
├── README.md
├── run.bat (optional)
└── .gitignore
