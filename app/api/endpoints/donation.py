from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.servises.invest import invest_funds
from app.models import User
from app.schemas.donation import DonationCreate, DonationDB

router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session),
) -> list[DonationDB]:
    all_donations = await donation_crud.get_multi(session)
    return all_donations


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude={'user_id',
                            'invested_amount',
                            'fully_invested',
                            'close_date'},
    response_model_exclude_none=True
)
async def create_new_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
) -> DonationDB:
    new_donation = await donation_crud.create(
        donation,
        session,
        user,
        save=False
    )
    session.add_all(
        invest_funds(
            new_donation,
            await charity_project_crud.get_all_not_invested(
                session
            )
        )
    )
    await session.commit()
    await session.refresh(new_donation)
    return new_donation


@router.get(
    '/my',
    response_model=list[DonationDB],
    response_model_exclude={'user_id',
                            'invested_amount',
                            'fully_invested',
                            'close_date'},
)
async def get_user_donation(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    reservations = await donation_crud.get_by_user(
        session=session, user=user
    )
    return reservations
