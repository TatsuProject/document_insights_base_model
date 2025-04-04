import ollama
from .prompts_manager import get_document_prompt
import json

client = ollama.Client(host='http://localhost:11434')


def parse_document_content(doc_type, context):
    doc_prompt = get_document_prompt(doc_type, context)

    if doc_prompt == "Invalid document type":
        return {}
    messages=[
            {"role": "system", "content": "You are a document parser, and your job is to analyze documents carefully and parse them accurately."},
            {"role": "user", "content": doc_prompt}
        ]

    response = client.chat(model="qwen2.5:14b", messages=messages)
    return json.loads(response["message"]["content"])
