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
from logging.handlers import TimedRotatingFileHandler
from threading import Lock
import torch
from doc_classifier.inference import doc_classifier_predict
from doc_parser.get_llm_response import parse_document_content
from doc_parser.ocr import extract_text_from_image


logging.basicConfig(level=logging.INFO)
log_handler = TimedRotatingFileHandler("./logs/yolo_logs_24h.log", when="midnight", interval=1, backupCount=7)
log_handler.setLevel(logging.INFO)
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
log_handler.setFormatter(log_formatter)

# Add the handler to bittensor logger
root_logger = logging.getLogger()  # Get the root logger instance
root_logger.addHandler(log_handler)


app = Flask(__name__)

# Load the YOLOv8 model
model = YOLO("model/checkbox_detector.pt")
device = "cuda" if torch.cuda.is_available() else "cpu"
# device = "cpu"

@app.route('/predict', methods=['POST'])
def predict():
    # Decode the incoming image
    request_id = request.json.get('request_id', '')
    task_type = request.json.get('task_type', 'checkbox')
    try:
        image_data = request.json.get('image')
        image = base64.b64decode(image_data)
        image_rgb = Image.open(io.BytesIO(image)).convert('RGB')

        image = np.array(image_rgb)
        logging.info(f"[{request_id}]: Received image with shape: {image.shape}")
    except Exception as e:
        logging.error(f"[{request_id}]: Error decoding image: {e}")
        return jsonify({'error': 'Invalid image format'}), 400

    predictions = []
    status = "success"
    # Make predictions
    if task_type=="checkbox":
        try:
            # with model_lock:  # Ensure that only one thread accesses the model at a time
            logging.info(f"---------- device: {device}")
            results = model.predict(source=image, device=device)
            # logging.info(f"[{request_id}]: Model predictions: {results}")
        except Exception as e:
            logging.error(f"[{request_id}]: Error during model prediction: {e}")
            return jsonify({'error': 'Model prediction failed'}), 500


        # Prepare the output
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
    elif task_type=="doc-class":
        logging.info(f"---------- device: {device}")
        predictions.append(doc_classifier_predict(image_rgb))

    elif task_type=="doc-parse":
        logging.info(f"---------- device: {device}")
        doc_type = doc_classifier_predict(image_rgb)
        context = extract_text_from_image(image_data)
        parsed_result = parse_document_content(doc_type, context)
        final_dict = {
            "document_class": doc_type,
            "NER": parsed_result
        }
        predictions.append(final_dict)

    else:
        predictions.append("unsupported task type")
        status = "error"

    logging.info(f"[{request_id}]: Predictions: {predictions}")
    # Return the predictions as JSON
    return jsonify({'request_id': request_id, 'predictions': predictions, "status": status})

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
