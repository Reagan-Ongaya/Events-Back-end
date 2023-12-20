from fastapi import FastAPI, Depends,  HTTPException, status, Response
from sqlalchemy.orm import Session
from database import get_db
from models import Destination
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
    destinations = db.query(Destination).all()
    return destinations

#getting a single destination
@app.get('/destinations/{destination_id}')
def destination(destination_id: int, db: Session = Depends(get_db)):
    destination = db.query(Destination).filter(Destination.id == destination_id)
    return destination

#creating a destination
@app.post('/destinations')
def create_destinations(destination: DestinationSchema, db: Session = Depends(get_db)):
    #unpacking a dict & passed a keyvalue
    new_destination = Destination (**destination.model_dump())
    
    #adding the destination to transaction
    db.add(new_destination)
    
    #commiting trabnsaction
    db.commit()
    
    #getting destination from db
    return{
        "message":"Destination created with success",
        "destination" :new_destination
    }
    
    
 #updating   
@app.patch('/destinations/{destination_id}')
def update_destination(destination_id : int, db: Session = Depends(get_db)):
    update_destination = db.query(Destination).filter(Destination.id == destination_id)
    return update_destination
 
    
# deletion
@app.delete('/destinations/{destination_id}')
def delete_destination(destination_id: int, db: Session = Depends(get_db)):
    delete_destination = db.query(Destination).filter(Destination.id == destination_id).first()

    if delete_destination == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Destination {destination_id} does not exist")
    else:
        delete_destination.delete()
        # running transaction
        db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)