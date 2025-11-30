from fastapi import FastAPI
from app.api.object_detector import router as api_router

app = FastAPI(title="YOLO Service")

app.include_router(api_router, prefix="/api")

# uvicorn app.main:app --reload