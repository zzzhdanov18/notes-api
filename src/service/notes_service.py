from uuid import UUID, uuid4
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from src.schemas.schema import NoteItemCreate, NoteItem
from src.service.abstract_service import AbstractService
from src.service.abstract_crud import AbstractCRUD
from src.service.notes_crud import NotesCRUD
from src.db.database_config import get_db


class NotesService(AbstractService):

    def get_items_list(self) -> list[NoteItem]:
        return self.crud.get_list()
    
    def get_item(self, note_id: UUID) -> NoteItem:
        note_item = self.crud.get_detail(note_id)

        if note_item is None:
            raise HTTPException(status_code=404, detail='note not found')
        
        return note_item
    
    def create_item(self, note_item: NoteItemCreate) -> NoteItem:
        return self.crud.create(note_item)
    
    def mark_item_as_completed(self, note_id) -> None:
        note_item = self.crud.get_detail(note_id)

        if note_item is None:
            raise HTTPException(status_code=404, detail='note not found')
        
        self.crud.mark_as_completed(note_id)

    def delete_item(self, note_id):
        note_item = self.crud.get_detail(note_id)

        if note_item is None:
            raise HTTPException(status_code=404, detail='note not found')
        
        self.crud.delete(note_id)

        return {'message': 'The note has been deleted'}
    


def get_note_service( db:Session = Depends(get_db)) -> AbstractService:
    crud: AbstractCRUD = NotesCRUD(db)
    note_service: AbstractService = NotesService(crud)
    
    return note_service



        
        