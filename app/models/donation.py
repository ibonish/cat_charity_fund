from sqlalchemy import (Boolean, CheckConstraint, Column, DateTime, Integer,
                        Text, func, ForeignKey)

from app.core.db import Base


class Donation(Base):
    user_id = Column(
        Integer,
        ForeignKey('user.id')
    )
    comment = Column(
        Text,
        nullable=True
    )
    full_amount = Column(
        Integer,
        nullable=False,
    )
    invested_amount = Column(
        Integer,
        default=0,
        nullable=False,
    )
    fully_invested = Column(
        Boolean,
        default=False,
        nullable=False
    )
    create_date = Column(
        DateTime,
        default=func.now(), nullable=False)
    close_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))

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
