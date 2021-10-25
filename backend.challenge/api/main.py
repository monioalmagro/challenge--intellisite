from fastapi import FastAPI
from fastapi_pagination import Page, add_pagination, paginate

from src.models import Detection
from src.schemas import detectionsEntity
from src.utils import find_all, stats

app = FastAPI()


@app.get("/detections", response_model=Page[Detection])
async def root():
    x = find_all()
    detections = detectionsEntity(x)
    return paginate(detections)


@app.get("/stats")
async def root():
    x = stats()
    return x


add_pagination(app)
