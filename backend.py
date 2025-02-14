import requests
import os
from config import HUGGINGFACE_API_KEY

def get_ai_response(query):
    if not HUGGINGFACE_API_KEY:
        return "Error: Hugging Face API key not found. Set it in environment variables."

    url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

    data = {"inputs": query}  

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_data = response.json()

        if isinstance(response_data, list) and len(response_data) > 0:
            return response_data[0].get("generated_text", "No response received.").strip()

        return "No valid response received."
    except requests.exceptions.RequestException as e:
        return f"API Request Error: {str(e)}"
