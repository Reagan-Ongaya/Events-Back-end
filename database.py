from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#connect to pg database
engine = create_engine("postgres://admin:q0YB5QDoqZ2FyboPR1GEmAOPtlK7rDkN@dpg-cm18aaocmk4c73d6o5h0-a.frankfurt-postgres.render.com/destyinations")

SessionLocal = sessionmaker(bind=engine)

#def method of get db
def get_db():
    db = SessionLocal()
    try: 
        yield
    finally:
        db.close()