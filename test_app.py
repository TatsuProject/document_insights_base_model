
import requests
import base64
import concurrent.futures
import uuid

# Load and encode an image
with open("", "rb") as image_file: # give your image path here
    encoded_string = base64.b64encode(image_file.read()).decode()

# Prepare the request payload
payload = {'image': encoded_string, "request_id": str(uuid.uuid4()), "task_type": "checkbox"}

# Function to send a POST request
def send_request():
    try:
        response = requests.post('http://127.0.0.1:5000/predict', json=payload)
        print(f"Status Code: {response.status_code}")
        predictions = response.json()
        print(f"Response: {predictions}")
    except Exception as e:
        print(f"Request failed: {e}")

# Use ThreadPoolExecutor to send 10 requests in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request) for _ in range(1)]

    # Wait for all futures to complete
    concurrent.futures.wait(futures)
