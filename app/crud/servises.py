from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud


async def invest_funds(session: AsyncSession):
    donations = await donation_crud.get_all_by_attribute('fully_invested', False, session)
    projects = await charity_project_crud.get_all_by_attribute('fully_invested', False, session)

    for donation in donations:
        for project in projects:
            if donation.full_amount - donation.invested_amount <= 0:
                break

            available_to_invest = min(donation.full_amount - donation.invested_amount, project.full_amount - project.invested_amount)

            donation.invested_amount += available_to_invest
            project.invested_amount += available_to_invest

            if donation.invested_amount == donation.full_amount:
                donation.fully_invested = True
                donation.close_date = func.now()

            if project.invested_amount == project.full_amount:
                project.fully_invested = True
                project.close_date = func.now()

            if donation.fully_invested:
                break

    await session.commit()
    for donation in donations:
        await session.refresh(donation)
    for project in projects:
        await session.refresh(project)
