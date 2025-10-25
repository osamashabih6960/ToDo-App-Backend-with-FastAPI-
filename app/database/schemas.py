from sqlalchemy import Column, Integer, String, DATETIME, Boolean
from sqlalchemy.orm import declarative_base
import uuid
from datetime import datetime, timezone


Base = declarative_base()

class ToDo(Base):
    __tablename__ = "Todo"
    id = Column(String, primary_key=True, index = True, default= lambda: str(uuid.uuid4()))
    task_title = Column(String)
    description = Column(String)
    created_at = Column(DATETIME, default=lambda: datetime.now(timezone.utc))
    task_completed = Column(Boolean)



