from sqlalchemy import String, Boolean, Date, Column
from sqlalchemy.dialects.postgresql import UUID

from src.db.database_config import Base


class Note(Base):
    __tablename__ = "note"

    id = Column(UUID(as_uuid=True), pramary_key=True)
    title = Column(String(30), nullable=False)
    text = Column(String(30))
    is_completed = Column(Boolean)
    date_completion = Column(Date)

