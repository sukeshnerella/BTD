from flask import Flask, render_template, request, jsonify
from PIL import Image
import tensorflow as tf
import numpy as np
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the pre-trained CNN model
CNN = tf.keras.models.load_model("CNN.h5", compile=False)
cl_labels = ['glioma', 'meningioma', 'notumor', 'pituitary']

def preprocess_image(image):
    img = image.resize((224, 224))
    iArray = tf.keras.preprocessing.image.img_to_array(img)
    iArray = tf.expand_dims(iArray, 0)
    return iArray

def predict_class(image_array):
    p = CNN.predict(image_array)
    return cl_labels[np.argmax(p)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        image = Image.open(file)
        image_array = preprocess_image(image)
        predicted_class = predict_class(image_array)
        return jsonify({'prediction': predicted_class})
    except Exception as e:
        return jsonify({'error': f'Error predicting the image: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
