from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.core.db import get_async_session
from app.crud.donation import donation_crud
from app.crud.servises import invest_funds
from app.schemas.donation import DonationCreate, DonationDB

router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationDB],
    response_model_exclude_none=True,
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
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
) -> DonationDB:
    new_donation = await donation_crud.create(donation, session)
    await invest_funds(session)
    return new_donation
