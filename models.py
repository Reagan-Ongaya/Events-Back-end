from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, DateTime, Integer

#create base model 
Base = declarative_base()


#defining destination model
class Destiation(Base):
    __tablename__ = "destinations"
    
    #def column
    id = Column(Integer(), primary_key=True )
    name = Column(Text())
    location = Column(Text())
    image = Column(Text())
    price = Column(Integer())
    start_date = Column(DateTime())
    end_date = Column(DateTime())