Skin Disease Detection
This project aims to develop a machine learning model capable of detecting skin diseases from images. It also includes a web application that allows users to upload images and receive predictions from the trained model.

Project Overview
Skin diseases are common, and early detection is crucial for effective treatment. This project utilizes deep learning techniques to classify various skin conditions based on images. The model is integrated into a Flask web application, providing an easy-to-use interface for real-time predictions.

Features
Image Classification: Classifies images into different skin disease categories.
Web Interface: User-friendly interface for uploading images and viewing predictions.
Model Integration: Real-time predictions using a pre-trained deep learning model.

Installation

Prerequisites
Python 3.x
Virtual environment tool (optional but recommended)

STEPS : 
1) git clone <repository_url>
   cd skindisease-main

2) Create and activate virtual environment
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3) Install Dependencies
    pip install -r requirements.txt

USAGE 

1) RUNNING WEB APPLICATION
    python app.py -------------This command will start the Flask server. Open your browser and navigate to http://127.0.0.1:5000 to use the application.
    Upload an image of a skin condition to receive a prediction from the model.


