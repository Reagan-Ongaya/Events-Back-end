from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Destiation
from schemas import DestinationSchema

app = FastAPI()

#Creating routes for our server

@app.get('/')
def index():
    return{
        "massage" :"Welcome"
    }

#getting all destination
@app.get('/destinations')
def destinations(db: Session = Depends(get_db)):
    destinations = db.query(Destiation).all()
    return destinations

#getting a single destination
@app.get('/destinations/{destination_id}')
def destination():
    return []

#post a destination
@app.post('/')
def create():
    return{
        "message":"Created with success"
    }
    
@app.post('/destinations')
def create_destinations(destination: DestinationSchema):
    print(destination)
    return{
        "message":"Destination created with success"
    }
    
    
 #updating   
@app.patch('/destinations/{destination_id}')
def update_destination(destination_id : int):
    return{
        "message":f"Destination { destination_id }created with success"
    }
    
# deletion
@app.delete('/destinations/{destination_id}')
def delete_destination(destination_id : int):
    return{
        "message":f"Destination { destination_id }deleted with success"
    }