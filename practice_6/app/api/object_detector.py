from fastapi import APIRouter, UploadFile, File, Response
from app.models.schemas import detector

router = APIRouter()

@router.post("/predict")
async def predict_endpoint(file: UploadFile = File(...)):
    file_bytes = await file.read()
    
    processed_image = detector.predict(file_bytes)
    
    return Response(content=processed_image, media_type="image/jpeg")
