from datetime import datetime
from typing import Union, List

from app.models.charity_project import CharityProject
from app.models.donation import Donation


def invest_funds(
    target: Union[CharityProject, Donation],
    sources: Union[List[CharityProject], List[Donation]],
) -> Union[List[CharityProject], List[Donation]]:
    updated = []
    for source in sources:
        available_amount = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )
        for investment in [target, source]:
            investment.invested_amount += available_amount
            investment.fully_invested = (
                investment.invested_amount == investment.full_amount
            )
            if investment.fully_invested:
                investment.close_date = datetime.now()
        updated.append(source)
        if target.fully_invested:
            break
    return updated
