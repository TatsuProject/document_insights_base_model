import base64
import pytesseract
from PIL import Image
import io

def extract_text_from_image(image_data: str) -> str:
    # Decode the base64 string into bytes
    image_bytes = base64.b64decode(image_data)
    
    # Convert bytes to a PIL Image
    image = Image.open(io.BytesIO(image_bytes))
    
    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(image)
    
    return extracted_text