from fastapi import FastAPI
import uvicorn
import os
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.textSummarizer.pipeline.prediction_pipeline import PredictionPipeline
from src.textSummarizer.logger import logging


text: str = "What is ChatGPT? ChatGPT is an AI language model developed by OpenAI that is designed to understand and generate human-like text based on the input it receives. It is built on the GPT (Generative Pre-trained Transformer) architecture, which is a type of deep learning model specifically designed for natural language processing tasks. ChatGPT has been trained on a diverse range of internet text, allowing it to generate coherent and contextually relevant responses across various topics. Users can interact with ChatGPT for a variety of applications, including answering questions, providing explanations, generating creative content, and assisting with writing tasks."

app = FastAPI()

@app.get("/", tags=['authentication'])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/health", tags=['authentication'])
async def health_check():
    return Response(content="OK", media_type="text/plain", status_code=200)

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response(content="Training completed successfully", media_type="text/plain", status_code=200)
    except Exception as e:
        return Response(content=f"Training failed: {str(e)}", media_type="text/plain", status_code=500)

@app.get("/predict")
async def predict_response():
    try:
        logging.info("Prediction started")
        prediction_pipeline = PredictionPipeline()
        summary = prediction_pipeline.predict(text)
        logging.info("Prediction completed")
        return Response(content=summary, media_type="text/plain", status_code=200)
    except Exception as e:
        logging.exception("Prediction failed")
        return Response(content=f"Prediction failed: {str(e)}", media_type="text/plain", status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
