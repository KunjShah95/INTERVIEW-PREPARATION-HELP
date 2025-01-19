import requests

# Google Gemini API integration (example, replace with real URL and API key)
GEMINI_API_KEY = 'YOUR_GOOGLE_GEMINI_API_KEY'
GEMINI_API_URL = 'https://gemini.googleapis.com/v1beta1/text:generate'  # Example URL, replace with actual

def get_gemini_response(prompt: str) -> str:
    """Get response from Google Gemini"""
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "max_tokens": 500,  # Adjust token limit
        "temperature": 0.7  # Adjust temperature for creativity
    }

    response = requests.post(GEMINI_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()['generated_text']
    else:
        raise Exception(f"Gemini API error: {response.status_code} - {response.text}")
