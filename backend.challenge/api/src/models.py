from pydantic import BaseModel


class Detection(BaseModel):
    year: int
    make: str
    model: str
    category: str
