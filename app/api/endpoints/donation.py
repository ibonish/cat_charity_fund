from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.core.db import get_async_session
from app.crud.donation import donation_crud
from app.crud.servises import invest_funds
from app.schemas.donation import DonationCreate, DonationDB
from app.core.user import current_user
from app.models import User
from app.core.user import current_superuser

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
    response_model_exclude_none=True,
    response_model_exclude={'user_id', 'invested_amount', 'fully_invested', 'close_date'}
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
) -> DonationDB:
    new_donation = await donation_crud.create(donation, session, user)
    await invest_funds(session)
    return new_donation


@router.get(
    '/my',
    response_model=list[DonationDB],
    response_model_exclude={'user_id', 'invested_amount', 'fully_invested', 'close_date'},
)
async def get_user_donation(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):

    reservations = await donation_crud.get_by_user(
        session=session, user=user
    )
    return reservations
