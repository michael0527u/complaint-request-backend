import requests
import os
from dotenv import load_dotenv

# ✅ Load .env file
load_dotenv()

# ✅ Retrieve API key and URL
API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL")
MODEL_ID = os.getenv("OPENROUTER_MODEL_ID")

# ✅ Check if API key is present
if not API_KEY:
    print("❌ Error: OPENROUTER_API_KEY is missing. Check your .env file!")
    exit()

# ✅ Prepare the request
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": MODEL_ID,
    "messages": [{"role": "user", "content": "Hello, can you test my OpenRouter API key?"}],
    "max_tokens": 50
}

# ✅ Send the request
try:
    response = requests.post(BASE_URL, headers=headers, json=payload)
    response_data = response.json()

    # ✅ Debugging output
    print("📡 OpenRouter API Response:", response_data)

    # ✅ Check if API returned choices
    if "choices" in response_data:
        print("✅ API Key is WORKING!")
    else:
        print("⚠️ API Key is NOT working. Response format unexpected.")

except Exception as e:
    print("❌ Error contacting OpenRouter API:", e)
