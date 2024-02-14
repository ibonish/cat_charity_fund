from app.crud.base import CRUDBase
from app.models.donation import Donation
from app.schemas.donation import DonationCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User


class CRUDDonation(CRUDBase):
    async def get_by_user(
            self,
            session: AsyncSession,
            user: User,
    ):
        reservations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return reservations.scalars().all()


donation_crud = CRUDDonation(Donation)
