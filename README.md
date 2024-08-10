# SKIN DISEASE DETECTION

This project aims to develop a machine learning model capable of detecting skin diseases from images. It also includes a web application that allows users to upload images and receive predictions from the trained model.

## PROJECT OVERVIEW 
Skin diseases are common, and early detection is crucial for effective treatment. This project utilizes deep learning techniques to classify various skin conditions based on images. The model is integrated into a Flask web application, providing an easy-to-use interface for real-time predictions.

## FEATURES
Image Classification: Classifies images into different skin disease categories.
Web Interface: User-friendly interface for uploading images and viewing predictions.
Model Integration: Real-time predictions using a pre-trained deep learning model.

## TECHNOLOGIES USED
1. Python: Core programming language.
2. Flask: Web framework used for the application.
3. TensorFlow/Keras: Libraries used for building and training the neural network.
4. HTML/CSS/JavaScript: For the web interface.


## INSTALLATIONS AND SETTING VIRTUAL ENVIRONMENT

### Prerequisites
Python 3.x
Virtual environment tool (optional but recommended)

## STEPS : 
1) ``` bash
   git clone https://github.com/nikithamarythomas/skindisease.git
   cd skindisease-main
   ```

2) Create and activate virtual environment
   ``` python 
   python3 -m venv venv
   source venv/bin/activate  
   ```
   # On Windows use 
   `venv\Scripts\activate`

3) Install Dependencies
    ``` python
    pip install -r requirements.txt
    ```

## USAGE 

1) RUNNING WEB APPLICATION
   ``` bash
    python app.py
   ```
</br>
    This command will start the Flask server. Open your browser and navigate to http://127.0.0.1:5000 to use the application.
    Upload an image of a skin condition to receive a prediction from the model.


### CONTRIBUTING TO THIS REPOSITORY
Contributions are welcome! Please follow these steps:

1) Fork the repository.
2) Create a new branch for your feature or bugfix.
3) Submit a pull request with a clear description of your changes.

## DEPLOYMENT
The Flask application was successfully deployed on Render, allowing users to access the model for skin disease detection in a cloud environment. However, during the deployment process, we encountered a significant challenge:

Although the application ran smoothly in the local environment, we faced issues when processing images in the cloud environment on Render. This problem is likely due to the limitations of cloud storage or differences in how files are handled between local storage and Render's cloud storage.

## Steps for Deployment on Render:
1) Prepare the Flask Application:

      Ensure the application is fully functional locally before deploying.
      Confirm that all dependencies are listed in requirements.txt.

2) Create a Render Account:

      Sign up at Render.

3) Deploy the Application:

      Link the GitHub repository to Render.

4) Environment Configuration:

      Ensure all necessary environment variables (e.g., FLASK_ENV, MODEL_PATH) are configured correctly in the Render dashboard.

5) Monitor and Troubleshoot:

      After deployment, monitor the application for any issues, particularly related to image processing.


### TROUBLESHOOT
----Common issues and solutions:----<br/>
Installation Errors: Ensure all dependencies are installed correctly.<br/>
Server Issues: Check for port conflicts or missing environment variables.


### ACKNOWLEDGEMENTS
Special thanks to the developers and contributors who helped build this project. Additionally, acknowledgment for the dataset sources and any libraries used.

### CONTACT INFORMATIONS
For questions or support, contact at [nimisha.parameswaranthankamani@dcmail.ca / nikitha.thomas@dcmail.ca / geethu.vijayan@dcmail.ca / anju.sunny@dcmail.ca].

### FAQ
1) What formats of images are supported?
   The application supports JPEG and PNG formats.
2) Can the model be trained on new data?
   Yes, the model can be retrained using the skin.ipynb notebook with new data.
