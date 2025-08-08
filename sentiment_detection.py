from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("AZURE_TEXT_ANALYTICS_KEY")
endpoint = os.getenv("AZURE_TEXT_ANALYTICS_ENDPOINT")

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

def sentiment_analysis(text):
    client = authenticate_client()
    documents = [text]
    response = client.analyze_sentiment(documents=documents)[0]
    return response

if __name__ == "__main__":
    sample_text = "I love sunny days but hate the rain."
    response = sentiment_analysis(sample_text)
    print(f"Text: {sample_text}")
    print(f"Overall Sentiment: {response.sentiment}")
    for i, sentence in enumerate(response.sentences):
        print(f"Sentence {i+1} sentiment: {sentence.sentiment}")
        print(f"  Positive score: {sentence.confidence_scores.positive:.2f}")
        print(f"  Neutral score: {sentence.confidence_scores.neutral:.2f}")
        print(f"  Negative score: {sentence.confidence_scores.negative:.2f}")
