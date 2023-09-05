import os
from pydantic.main import BaseModel
import uvicorn
from src.summarizer import summarize_pdf
from fastapi import FastAPI, File, UploadFile
from src.pdf import extract_text_from_pdf

app = FastAPI(title="Text to SQL APP")

API_HEALTH_ROUTE = os.environ.get("AIP_HEALTH_ROUTE", "/health")
API_SUMMARIZE_ROUTE = os.environ.get("AIP_PREDICT_ROUTE", "/summarize")



class SummaryResponse(BaseModel):
    summary: str



@app.get(API_HEALTH_ROUTE, status_code=200)
async def health():
    return {"health": "ok"}



@app.post(
    API_SUMMARIZE_ROUTE, response_model=SummaryResponse, response_model_exclude_unset=True
)
async def get_summary(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file.read())
    summary = summarize_pdf(text=text)

    return SummaryResponse(summary=summary)





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
