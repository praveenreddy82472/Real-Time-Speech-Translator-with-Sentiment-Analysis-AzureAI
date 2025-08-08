import requests
import os
from dotenv import load_dotenv
from Speech_Recognition import speech_recognition_continuous

load_dotenv()

TRANSLATOR_KEY = os.getenv("AZURE_TRANSLATOR_KEY")
TRANSLATOR_REGION = os.getenv("AZURE_TRANSLATOR_REGION")

def translate_text(text, to_language="te"):  # Telugu as example
    endpoint = f"https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to={to_language}"
    headers = {
        "Ocp-Apim-Subscription-Key": TRANSLATOR_KEY,
        "Ocp-Apim-Subscription-Region": TRANSLATOR_REGION,
        "Content-type": "application/json",
    }
    body = [{"text": text}]
    response = requests.post(endpoint, headers=headers, json=body)
    response.raise_for_status()
    result = response.json()
    translated_text = result[0]['translations'][0]['text']
    return translated_text

if __name__ == "__main__":
    sample_text = speech_recognition_continuous()
    print("Original:", sample_text)
    print("Translated:", translate_text(sample_text, to_language="te"))  # Hindi
