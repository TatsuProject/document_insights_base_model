from fireworks.client import Fireworks
import json
from .prompts_manager import get_document_prompt
from dotenv import load_dotenv
import os
load_dotenv()

# Initialize Fireworks client
api_key = os.getenv("FIREWORKS_API_KEY")
client = Fireworks(api_key=api_key)

def parse_document_content_api(doc_type, context):
    # Get the document-specific prompt
    doc_prompt = get_document_prompt(doc_type, context)

    if doc_prompt == "Invalid document type":
        return {}

    messages = [
        {"role": "system", "content": "You are a document parser, and your job is to analyze documents carefully and parse them accurately."},
        {"role": "user", "content": doc_prompt}
    ]

    # Fireworks API call using SDK
    response = client.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p3-70b-instruct",  # Qwen 2.5 model
        messages=messages,
        temperature=0.7,
        max_tokens=1024
    )

    # Parse response
    return json.loads(response.choices[0].message.content)


if __name__ == "__main__":
    fireworks_resp = parse_document_content_api("", "")
    print(fireworks_resp)