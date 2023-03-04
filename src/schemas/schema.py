from pydantic import BaseModel
from datetime import date
from uuid import UUID


class NoteItemCreate(BaseModel):
    title: str
    text: str
    date_completion: date


class NoteItem(NoteItemCreate):
    id: UUID
    is_complete: bool

    class Config:
        orm_mode = True
