from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import CharityBase


class Donation(CharityBase):
    user_id = Column(
        Integer,
        ForeignKey('user.id')
    )
    comment = Column(
        Text,
        nullable=True
    )

    def __repr__(self):
        return super().__repr__()
