from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///api/database/todo.db"

engine = create_engine(DATABASE_URL, connect_args= {"check_same_thread": False})
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind = engine)

# Dependency to get the db session

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()