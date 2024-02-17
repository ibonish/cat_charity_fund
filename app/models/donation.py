from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import CharityBase

INFORMATION_MESSAGE = (
    'user_id: {user_id}',
    'comment: {comment}',
    '{super}'
)


class Donation(CharityBase):
    user_id = Column(
        Integer,
        ForeignKey('user.id')
    )
    comment = Column(
        Text,
        nullable=True
    )

    def __repr__(self) -> str:
        return INFORMATION_MESSAGE.format(
            user_id=self.user_id,
            comment=self.comment,
            super=super().__repr__(),
        )
