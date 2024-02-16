from datetime import datetime
from typing import List, TypeVar

from app.core.db import Base

ModelType = TypeVar('ModelType', bound=Base)


def invest_funds(
        target: ModelType,
        sources: List[ModelType],
) -> List[ModelType]:
    updated_objects = []
    if target.invested_amount is None:
        target.invested_amount = 0
    for source in sources:
        available_amount = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )
        for investment in [target, source]:
            recalculate_investment(investment, available_amount)
        updated_objects.append(source)
        if target.fully_invested:
            break
    return updated_objects


def recalculate_investment(
        db_obj: ModelType,
        available_amount: int
) -> None:
    db_obj.invested_amount += available_amount
    db_obj.fully_invested = (
        db_obj.invested_amount == db_obj.full_amount
    )
    if db_obj.fully_invested:
        db_obj.close_date = datetime.now()
