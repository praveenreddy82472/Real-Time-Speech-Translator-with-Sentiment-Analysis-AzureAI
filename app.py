from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from starlette.websockets import WebSocketDisconnect
# import your existing functions
from translator import translate_text
from sentiment_detection import sentiment_analysis

app = FastAPI()

# Mount static files on /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at root
@app.get("/")
async def get_index():
    return FileResponse("static/index.html")

def simplify_sentiment(sentiment_result):
    return {
        "sentiment": sentiment_result.sentiment,
        "positive": sentiment_result.confidence_scores.positive,
        "neutral": sentiment_result.confidence_scores.neutral,
        "negative": sentiment_result.confidence_scores.negative
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print("Received from frontend:", data)

            translation = translate_text(data, to_language="te")
            sentiment_result = sentiment_analysis(data)
            simple_sentiment = simplify_sentiment(sentiment_result)

            print(f"Translation: {translation}, Sentiment: {simple_sentiment}")

            await websocket.send_json({
                "transcript": data,
                "translation": translation,
                "sentiment": simple_sentiment
            })
    except WebSocketDisconnect:
        print("Client disconnected")
    
    except Exception as e:
        print("WebSocket error:", e)
        await websocket.close()
