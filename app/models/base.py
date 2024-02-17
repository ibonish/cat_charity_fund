from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer

from app.core.db import Base

INFORMATION_MESSAGE = (
    'id: {id}, ',
    'full_amount: {full_amount}, ',
    'invested_amount: {invested_amount}',
    'create_date: {create_date}',
    'close_date: {close_date}',
)


class CharityBase(Base):
    __abstract__ = True
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
        default=datetime.now,
        nullable=False
    )
    close_date = Column(DateTime)

    table_args = (
        CheckConstraint(
            'full_amount > 0',
            name='check_full_amount_positive'
        ),
        CheckConstraint(
            'invested_amount <= full_amount',
            name='check_invested_amount'
        ),
        CheckConstraint(
            'invested_amount >= 0',
            name='check_invested_amount'
        ),
    )

    def __init__(self, **kwargs):
        kwargs.setdefault('invested_amount', 0)
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return INFORMATION_MESSAGE.format(
            id=self.id,
            full_amount=self.full_amount,
            invested_amount=self.invested_amount,
            create_date=self.create_date,
            close_date=self.close_date
        )
