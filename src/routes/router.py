from fastapi import APIRouter, Depends

from src.schemas.schema import NoteItem, NoteItemCreate
from src.service.notes_service import get_note_service, NotesService


api_router = APIRouter(prefix="/api/v1", tags=["notes"])


@api_router.get('/notes', response_model=list[NoteItem])
def get_notes(note_service: NotesService = Depends(get_note_service)):
    note_items = note_service.get_items_list()
    return note_items

@api_router.post('/notes/create', response_model=NoteItem)
def create_note(note_to_create: NoteItemCreate, note_service: NotesService = Depends(get_note_service)):
    note_item = note_service.create_item(note_to_create)
    return note_item


