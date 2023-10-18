from fastapi import APIRouter
from models import process_video

router = APIRouter()

@router.post("/process_video")
async def process_video_data(video_data: bytes):
    processed_data = process_video(video_data)
    return {"processed_data": processed_data}