from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.APP_NAME)

@app.get("/health")
def health_check():
    return {"status": "ok"}
