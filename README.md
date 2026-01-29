# Face Recognition System using Python

This project is a simple face recognition system built using **Python**, **OpenCV**, and the **face_recognition** library.  
It can detect and recognize known faces in real-time using a webcam.

## Features
Encode multiple faces
Real-time face recognition
Easy to add new people
Beginner-friendly project structure


## Folder Structure
face-recognition-system/
│
├── data/
│   ├── known_faces/
│   │   ├── alice/
│   │   │   ├── img1.jpg
│   │   │   └── img2.jpg
│   │   ├── bob/
│   │   │   └── img1.jpg
│   │
│   └── unknown_faces/
│       └── test.jpg
│
├── src/
│   ├── encode_faces.py
│   ├── recognize_faces.py
│   └── utils.py
│
├── encodings/
│   └── face_encodings.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
