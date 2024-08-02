from flask import Flask, render_template
from werkzeug.utils import secure_filename
import os

# Create a Flask application instance
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Define a route for the root URL
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for a prediction example
@app.route('/predict')
def predict():
    # This is where you would implement your predict logic
    # For now, we'll just return a placeholder message
    return "Here are your predictions"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
