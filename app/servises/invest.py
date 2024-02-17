from datetime import datetime


def invest_funds(
        target,
        sources,
):
    updated_objects = []
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
        updated_objects.append(source)
        if target.fully_invested:
            break
    return updated_objects
