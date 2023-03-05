from pydantic import BaseModel, validator
from datetime import datetime, date 
from uuid import UUID


class NoteItemCreate(BaseModel):
    title: str
    text: str
    date_completion: date


class NoteItem(NoteItemCreate):
    id: UUID
    is_completed: bool

    class Config:
        orm_mode = True
