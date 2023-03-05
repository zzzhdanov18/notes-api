from  src.service.abstract_crud import AbstractCRUD
from uuid import UUID, uuid4
import src.models.model as model
from src.schemas.schema import NoteItemCreate


class NotesCRUD(AbstractCRUD):

    def get_list(self):
        return self.db.query(model.Note).all()
    
    def get_detail(self, note_id: UUID):
        return self.db.query(model.Note).filter(model.Note.id == note_id).first()
    
    def create(self, note: NoteItemCreate):
        new_note = model.Note(
            id=uuid4(),
            title=note.title,
            text=note.text,
            is_completed=False,
            date_completion=note.date_completion
        )
        self.db.add(new_note)
        self.db.commit()
        return new_note
    
    def mark_as_completed(self, note_id: UUID):
        target_note = self.get_detail(note_id)

        target_note.is_completed=True

        self.db.commit()

    def delete(self, note_id: UUID):
        self.db.query(model.Note).filter(model.Note.id == note_id).delete()
        self.db.commit()
        