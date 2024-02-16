
from sqlalchemy import Column, String, Text

from app.models.base import CharityBase


class CharityProject(CharityBase):
    name = Column(
        String(100),
        unique=True,
        nullable=False
    )
    description = Column(
        Text,
        nullable=False
    )

    def __repr__(self):
        return super().__repr__()
