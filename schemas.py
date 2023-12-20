from pydantic import BaseModel

class DestinationSchema(BaseModel):
    name: str
    location: str
    image: str
    price: int
    start_date: str
    end_date: str
