from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Create a Flask application instance
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the pre-trained model
model = tf.keras.models.load_model('best_model.h5')



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
def preprocess_image(image_path):
    """Load and preprocess the image."""
    img = load_img(image_path, target_size=(28, 28))
    img_array = img_to_array(img)
    img_array = img_array / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict_page():
    return render_template('predict.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Preprocess the image and make predictions
        image_data = preprocess_image(file_path)
        predictions = model.predict(image_data)
        
        print("Processed image data shape:", image_data.shape)
        print("Raw predictions:", predictions)
        
        predicted_class = np.argmax(predictions, axis=1)[0]
        print("Predicted class index:", predicted_class)
        
        classes = {
            4: 'melanocytic nevi', 
            6: 'melanoma', 
            2: 'benign keratosis-like lesions', 
            1: 'basal cell carcinoma', 
            5: 'pyogenic granulomas and hemorrhage', 
            0: 'Actinic keratoses and intraepithelial carcinomae',  
            3: 'dermatofibroma'
        }
        result = classes.get(predicted_class, "Unknown")

        # Debug output
        print("Prediction result:", result)
        
        response = jsonify({'prediction': result})
        print(response)
        return response

    
    return jsonify({'error': 'Invalid file type'}), 400




# Run the application
if __name__ == '__main__':
    app.run(debug=True)
