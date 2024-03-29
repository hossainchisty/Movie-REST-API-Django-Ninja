from pydantic import BaseModel, Field
from datetime import datetime


class MoviePydantic(BaseModel):
    name: str
    protagonists: str
    poster: str
    trailer: str
    start_date: datetime = Field(..., alias="releaseDate")
    status: str
    ranking: int

    class Config:
        arbitrary_types_allowed = True
