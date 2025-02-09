# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Allows requests from React (running on a different port)

# 1. Load your trained model
#    Make sure 'food_model.h5' is in the same directory or adjust path accordingly.
model = tf.keras.models.load_model('food_model.h5')

# 2. Define the class labels (must match your model's output dimensions/order)
class_labels = [
    'cheese_plate', 
    'club_sandwhich', 
    'cup_cakes', 
    'donuts',
    'foie_gras', 
    'garlic_bread', 
    'gnocchi', 
    'ice_cream', 
    'samosa', 
    'tuna_tartare'
]

# 3. Helper function to preprocess the image
def preprocess_image(img_path):
    # Adjust target size to match what your model expects
    img = image.load_img(img_path, target_size=(235, 235))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# 4. Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded file temporarily
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    print(f"Image saved to: {file_path}")

    # Preprocess the image
    img_array = preprocess_image(file_path)

    # Make a prediction
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_label = class_labels[predicted_class_index]

    # Remove the temporary file
    os.remove(file_path)

    # Return the prediction as JSON
    return jsonify({'prediction': predicted_class_label})

# 5. Run the Flask app
if __name__ == '__main__':
    app.run(port=5001, debug=True)
