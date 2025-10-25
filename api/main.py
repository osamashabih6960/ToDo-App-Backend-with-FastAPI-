from fastapi import FastAPI, HTTPException, status
from fastapi import APIRouter, Depends
from api.routes.models import ToDoCreate, ToDoResponse
from api.database import schemas
from api.database.db_engine import SessionLocal, get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()

schemas.Base.metadata.create_all(engine)


@app.get('/', response_model= ToDoResponse)
def read_data(db: Session = Depends(get_db)):
    todo_item = db.query(schemas.ToDo).first()
    if not todo_item:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "ToDo item not found")
    return todo_item


@app.put('/{id}', response_model= ToDoResponse)
def update_data(id: str, request: ToDoCreate, db: Session = Depends(get_db)):
    todo_item = db.query(schemas.ToDo).filter(schemas.ToDo.id == id).first()
    if not todo_item:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    todo_item.task_title = request.task_title
    todo_item.description = request.description
    todo_item.task_completed = request.task_completed
    db.commit()
    db.refresh(todo_item)
    return todo_item

@app.post('/', response_model= ToDoResponse)
def create_data(request: ToDoCreate, db: Session = Depends(get_db)):
    new_todo = schemas.ToDo(
        task_title = request.task_title,
        description = request.description,
        task_completed = request.task_completed
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo  

@app.delete('/{id}')
def delete_data(id: str, db: Session = Depends(get_db)):
    todo_item = db.query(schemas.ToDo).filter(schemas.ToDo.id == id).first()
    if not todo_item:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "item not found and data cannot be deleted")
    db.delete(todo_item)
    db.commit()
    return {"detail": "ToDo item deleted successfully"}