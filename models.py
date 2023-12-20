from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, DateTime, VARCHAR,Integer

#create base model 
Base = declarative_base()


#defining destination model
class Destination(Base):
    __tablename__ = "destinations"
    
    #def column
    id = Column(Integer(), primary_key=True )
    name = Column(Text(),nullable=False)
    location = Column(Text(),nullable=False)
    image = Column(VARCHAR(),nullable=False)
    price = Column(Integer(),nullable=False)
    start_date = Column(DateTime(),nullable=False)
    end_date = Column(DateTime())