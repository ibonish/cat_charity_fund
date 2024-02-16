from sqlalchemy import (CheckConstraint, Column, ForeignKey,
                        Integer, Text)

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
    table_args = (
        CheckConstraint(
            'full_amount > 0',
            name='check_full_amount_positive'
        ),
        CheckConstraint(
            'invested_amount <= full_amount',
            name='check_invested_amount'
        ),
    )
