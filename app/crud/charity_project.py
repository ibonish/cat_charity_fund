from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from sqlalchemy import select
from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectCreate, CharityProjectUpdate


class CRUDMeetingRoom(CRUDBase[
    CharityProject,
    CharityProjectCreate,
    CharityProjectUpdate
]):
    async def get_project_id_by_name(
            self,
            charity_project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_charity_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_project_name
            )
        )
        db_charity_project_id = db_charity_project_id.scalars().first()
        return db_charity_project_id


charity_project_crud = CRUDMeetingRoom(CharityProject)
