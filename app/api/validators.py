from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectUpdate

CHECK_NAME_MESSAGE = 'Проект с таким именем уже существует!'
NOT_FOUND = 'Проект не найден!'
CLOSED_PROJECT = 'Закрытый проект нельзя редактировать!'
INVESTED_PROJECT = 'В проект были внесены средства, не подлежит удалению!'
CHECK_FULL_AMOUNT = 'Новая сумма не меньше уже инвестированных средств!'


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name,
        session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=400,
            detail=CHECK_NAME_MESSAGE,
        )


async def check_project_exists(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        charity_project_id,
        session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=404,
            detail=NOT_FOUND
        )
    return charity_project


async def check_project_is_closed(
        charity_project: CharityProject,
) -> None:
    if charity_project.fully_invested:
        raise HTTPException(
            status_code=400,
            detail=CLOSED_PROJECT
        )


async def check_project_is_invested(
        project_id: int,
        session: AsyncSession
) -> None:
    charity_project = await charity_project_crud.get(
        project_id,
        session
    )
    if charity_project.invested_amount:
        raise HTTPException(
            status_code=400,
            detail=INVESTED_PROJECT
        )


async def check_new_full_amount(
    charity_project: CharityProject,
    new_charity_project: CharityProjectUpdate
) -> CharityProject:
    if charity_project.invested_amount > new_charity_project.full_amount:
        raise HTTPException(
            status_code=400,
            detail=CHECK_FULL_AMOUNT
        )
