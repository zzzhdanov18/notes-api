from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class NoteItemCreate(BaseModel):
    title: str
    text: str
    date_completion: str


class NoteItem(NoteItemCreate):
    id: UUID
    is_completed: bool

    class Config:
        orm_mode = True
