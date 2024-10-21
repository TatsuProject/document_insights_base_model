from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import base64
import io
from PIL import Image
import sys
import os
import logging
from threading import Lock
import torch

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Load the YOLOv8 model
model = YOLO("model/checkbox_detector.pt")
device = "cuda" if torch.cuda.is_available() else "cpu"
# device = "cpu"

@app.route('/predict', methods=['POST'])
def predict():
    # Decode the incoming image
    request_id = request.json.get('request_id', '')
    try:
        image_data = request.json.get('image')
        image = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image)).convert('RGB')
        image = np.array(image)
        logging.info(f"[{request_id}]: Received image with shape: {image.shape}")
    except Exception as e:
        logging.error(f"[{request_id}]: Error decoding image: {e}")
        return jsonify({'error': 'Invalid image format'}), 400

    # Make predictions
    # Make predictions
    try:
        # with model_lock:  # Ensure that only one thread accesses the model at a time
        print("---------- device: ", device)
        results = model.predict(source=image, device=device)
        # logging.info(f"[{request_id}]: Model predictions: {results}")
    except Exception as e:
        logging.error(f"[{request_id}]: Error during model prediction: {e}")
        return jsonify({'error': 'Model prediction failed'}), 500


    # Prepare the output
    predictions = []
    if results[0].boxes:
        for box in results[0].boxes:
            prediction = {
                "state": "selected",
                "confidence": float(box.conf[0]),
                "boundingBox": [
                    int(round(box.xyxy[0][0].item())),  # x1
                    int(round(box.xyxy[0][1].item())),  # y1
                    int(round(box.xyxy[0][2].item())),  # x2
                    int(round(box.xyxy[0][1].item())),  # y1 again (x2, y1)
                    int(round(box.xyxy[0][2].item())),  # x2 again
                    int(round(box.xyxy[0][3].item())),  # y2
                    int(round(box.xyxy[0][0].item())),  # x1 again (x1, y2)
                    int(round(box.xyxy[0][3].item()))   # y2 again
                ]
            }
            predictions.append(prediction)
    else:
        logging.info(f"[{request_id}]: No boxes detected.")

    logging.info(f"[{request_id}]: Predictions: {predictions}")
    # Return the predictions as JSON
    return jsonify({'request_id': request_id, 'predictions': predictions})

@app.route('/', methods=['POST', 'GET'])
def check_status():
    res = {"Status": "Running"}
    return jsonify(res)

if __name__ == '__main__':
    # Default port is 5000, but you can pass a different port as a command-line argument
    port = 5000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    app.run(host="0.0.0.0", debug=False, port=port)
