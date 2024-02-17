
from sqlalchemy import Column, String, Text

from app.models.base import CharityBase


INFORMATION_MESSAGE = (
    'name: {name}',
    'description: {description}',
    '{super}'
)


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

    def __repr__(self) -> str:
        return INFORMATION_MESSAGE.format(
            name=self.name,
            description=self.description,
            super=super().__repr__(),
        )
