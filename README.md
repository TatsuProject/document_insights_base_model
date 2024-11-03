# YOLO Checkbox Detector

The **YOLO Checkbox Detector** leverages the power of **YOLOv8-large**, trained extensively on a unique dataset of 10,000 diverse documents, both scanned and general, to accurately detect checkboxes. Our model achieves exceptional performance, significantly outperforming leading AI solutions like GPT-4 Vision and Azure Form Recognizer.

### Model Performance
Our model was rigorously tested on a challenging test set of 300 images. Here’s how it stacks up:

| Model                       |  F1-Score |
|-----------------------------|-------------|
| **Azure Form Recognizer**    | 0.72       |
| **GPT-4 Vision**             | 0.63       |
| **YOLO Checkbox Detector**   | **0.88**   |

With an F1-Score of 0.88, the YOLO Checkbox Detector sets a new benchmark in checkbox detection, offering superior accuracy and reliability for document processing tasks.

## Table of Contents

- [ Installation](#installation)
- [ Downloading Model Weights](#downloading-model-weights)
- [ Running Tests](#running-tests)

##  Installation

Follow these steps to set up the YOLO Checkbox Detector:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TatsuProject/yolo_checkbox_detector
   cd yolo_checkbox_detector
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Downloading Model Weights

Retrieve the YOLOv8 Checkbox Detector weights by joining our [Discord community](https://discord.com/channels/799672011265015819/1263858989800886302). 

1. After downloading, create a `model` directory in the project root.
2. Place the downloaded weights into the `model` folder.

## Running Tests

1. **Start the service:**
   ```bash
   python app.py
   ```

2. **Run the test script** to analyze an image containing checkboxes:
   ```bash
   python test_app.py
   ```
   Make sure to provide the path to your target image in the script for accurate detection.
