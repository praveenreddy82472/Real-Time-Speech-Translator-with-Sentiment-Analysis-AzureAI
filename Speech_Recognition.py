import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

# Load environment variables from .env file
load_dotenv()

subscription_key = os.getenv("AZURE_SPEECH_KEY")
service_region = os.getenv("AZURE_SERVICE_REGION")

def speech_recognition_continuous():
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    recognized_text = []
    
    def recognized_handler(evt):
            print(f"Recognized: {evt.result.text}")
            recognized_text.append(evt.result.text)

    speech_recognizer.recognized.connect(recognized_handler)

    print("Speak now...")
    speech_recognizer.start_continuous_recognition()
    
    input("Press Enter to stop...\n")

    speech_recognizer.stop_continuous_recognition()

    # Combine all recognized phrases into one string
    return " ".join(recognized_text)
