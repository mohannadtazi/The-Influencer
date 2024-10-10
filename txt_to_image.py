import requests

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"
    return response.content
	

def generate_image(prompt):
    image_bytes = query({"inputs": str(prompt)})
    return image_bytes