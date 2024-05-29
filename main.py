from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List, Optional
from model import Model

app = FastAPI()


class spot(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    location: Optional[str] = None
    time: Optional[str] = None
    tags: Optional[List[str]] = None
    description: Optional[str] = None
    category: Optional[str] = None
    isVideo: Optional[bool] = None
    likes: Optional[int] = None
    like_ratio: Optional[float] = None
    img_url: Optional[str] = None

db: List[Model] = []
db_cafes: List[Model] = []
db_pubs: List[Model] = []
db_restaurants: List[Model] = []



def load_data_from_json(data: List[Model]):
    global db
    global db_cafes
    global db_pubs
    global db_restaurants
    data = sorted(data, key=lambda x: x.like_ratio, reverse=True)
    max_id = max((spot.id for spot in db if spot.id is not None), default=0)
    for item in data:
        max_id += 1
        item.id = max_id
        db.append(item)
    for i in db:
        if i.category == 'cafes':
            db_cafes.append(i)
        elif i.category == 'restaurants':
            db_restaurants.append(i)
        elif i.category == 'pubs':
            db_pubs.append(i)

@app.get("/")
async def message():
    return '어디가유 데이터 서버입니다. 확인용 3'

@app.post("/load-data/")
def load_data(data: List[Model]):
    try:
        load_data_from_json(data)
        return {"message": "Data loaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/spots/")
def create_spot(spot: Model):
    if db:
        max_id = max(s.id for s in db if s.id is not None)
        spot.id = max_id + 1
    else:
        spot.id = 1

    db.append(spot)
    return spot

@app.get("/spots/")
def read_spots():
    return db

@app.get("/spots/cafes/")
def get_cafes():
    return db_cafes

@app.get("/spots/restaurants/")
def get_restaurants():
    return db_restaurants

@app.get("/spots/pubs/")
def get_pubs():
    return db_pubs

@app.get("/spots/{spot_id}")
def read_spot(spot_id: int):
    for spot in db:
        if spot_id == spot.id:
            return spot
    raise HTTPException(status_code=404, detail="Spot not found")
