from fastapi import APIRouter, Depends
from uuid import UUID

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

@api_router.get("/notes/{note_id}", response_model=NoteItem)
def get_note_by_id( note_id: UUID,  note_service: NotesService = Depends(get_note_service)):
    note_item = note_service.get_item(note_id)
    return note_item

@api_router.patch("/notes/{note_id}/complete")
def mark_completed_note(note_id: UUID, note_service: NotesService = Depends(get_note_service)):
    return note_service.mark_item_as_completed(note_id)


@api_router.delete("/notes/{note_id}/delete")
def delete_note(note_id: UUID, note_service: NotesService = Depends(get_note_service)):
    return note_service.delete_item(note_id)




