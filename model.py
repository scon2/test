from pydantic import BaseModel
from typing import List, Optional

class Model(BaseModel):
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