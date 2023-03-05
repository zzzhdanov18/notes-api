from src.db.database_config import Base

from sqlalchemy import String, Boolean, Date, Column
from sqlalchemy.dialects.postgresql import UUID


class Note(Base):
    __tablename__ = "note"

    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(30), nullable=False)
    text = Column(String(30))
    is_completed = Column(Boolean)
    date_completion = Column(Date)

