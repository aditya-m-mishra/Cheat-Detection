# AI Exam Cheating Detector

An AI-powered computer vision application that detects suspicious exam behavior using a webcam.

The system analyzes face presence and head position to identify possible cheating activities such as:
- Looking away from the screen
- Multiple people in frame
- Absence of a person

---

## Features

- Real-time face detection using OpenCV
- Detects:
  - No person in frame
  - Multiple people in frame
  - Looking away from screen
- Displays live status on screen
- Maintains a cheating score counter
- Lightweight and easy-to-run Python project

---

## Tech Stack

- Python 3.8+
- OpenCV
- NumPy
- MediaPipe

---

## Project Structure

```text
examCheat_detector/
├── main.py              # Main application file
├── utils.py             # Helper functions
├── requirements.txt     # Project dependencies
├── README.md            # Documentation
├── run.bat              # Optional Windows launcher
└── .gitignore           # Ignored files and folders
```

---

## Installation

```bash
git clone <repository-url>
cd examCheat_detector
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

Or run:

```bash
run.bat
```

(Windows only)

---

## Future Improvements

- Eye tracking support
- Sound/activity detection
- Cheating report generation
- Web dashboard integration

---
