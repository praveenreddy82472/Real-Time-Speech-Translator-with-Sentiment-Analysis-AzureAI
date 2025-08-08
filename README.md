# Real-Time Speech Translator with Sentiment Analysis

A modern web app that captures your speech live, transcribes it in real-time, translates it to Telugu (or your chosen language), and performs sentiment analysis — all with smooth UI and instant feedback!

---

## Features

- 🎙️ **Real-time speech recognition** and transcription  
- 🌐 **Instant translation** to Telugu (configurable)  
- 😊😐😠 **Sentiment analysis** with detailed confidence scores  
- 🌓 **Dark/light mode toggle** for comfortable use anytime  
- ✨ **Smooth animations** and user-friendly design  
- 🚀 Powered by **FastAPI**, **Azure Cognitive Services**, and **Web Speech API**

---

## 📸 Sample Outputs

Here are some screenshots of the Smart Resume Scanner in action:

![Output 1](https://github.com/praveenreddy82472/Real-Time-Speech-Translator-with-Sentiment-Analysis-AzureAI/blob/main/Sample_outputs/Screenshot%202025-08-08%20133122.jpg)

---
## Live Demo

Try the real-time speech translator [here](http://127.0.0.1:8000)!

---
## Demo Preview

| Speak / Transcript                     | Translation                       | Sentiment                                   |
|--------------------------------------|---------------------------------|---------------------------------------------|
| _“Hello, how are you?”_ (live)       | _“హలో మీరు ఎలా ఉన్నారు?”_         | **Neutral** (Pos: 0.05, Neu: 0.90, Neg: 0.05) |

---

## How to Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/real-time-speech-translator.git
   cd real-time-speech-translator
2. **Start the FastAPI server**
   ```bash
    uvicorn app:app --reload
