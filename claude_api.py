import requests

# Claude API integration
CLAUDE_API_KEY = 'YOUR_CLAUDE_API_KEY'
CLAUDE_API_URL = 'https://api.anthropic.com/v1/claude'  # Placeholder URL, replace with actual API URL

def get_claude_response(prompt: str) -> str:
    """Get response from Claude AI"""
    headers = {
        "Authorization": f"Bearer {CLAUDE_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "max_tokens": 500,  # Adjust token limit
        "temperature": 0.7  # Adjust temperature for creativity
    }

    response = requests.post(CLAUDE_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()['text']
    else:
        raise Exception(f"Claude API error: {response.status_code} - {response.text}")
