# Smart Document Scanner using OpenCV

A computer vision project that detects a document from an image and converts it into a clean scanned output using image processing techniques.


## Features

✔ Detects document automatically from image  
✔ Finds document boundaries using contours  
✔ Applies perspective transformation  
✔ Converts image into clean black & white scan  
✔ Saves final output image  


## Tech Stack

Python  
OpenCV   
NumPy  



##  Project Structure

DocumentScanner/
│
├── main.py
└── document.jpg   (user must add this file)

## Installation

Step 1: Create folder
mkdir DocumentScanner
cd DocumentScanner

Step 2: Create virtual environment
python -m venv venv

Activate:

Windows:
venv\Scripts\activate


Step 3: Install dependencies
pip install opencv-python numpy



## Input Image Requirement
 User must download image manually
 Rename it to: document.jpg
 Place inside project folder