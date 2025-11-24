# SafeSite: Automated PPE Compliance Monitoring

## Overview
SafeSite is a Computer Vision application designed to enhance workplace safety. Using YOLOv8 and OpenCV, it monitors video feeds to 
ensure compliance with safety gear regulations.

![Real Time Preview](assets/11.png)

## Features
- **Real-time Inference:** Processes video at ~30 FPS.
- **Violation Detection:** Flags individuals not wearing required gear.
- **Data Persistence:** Automatically logs events to an SQLite database.

## Technologies Used
- **Language:** Python 3.9+
- **CV Core:** OpenCV, Ultralytics YOLOv8
- **Database:** SQLite3

## Installation & Running
1. Install dependencies:
   `pip install -r requirements.txt`
2. Run the application:
   `python main.py`
3. Press 'q' to exit the video window.