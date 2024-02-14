from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_name_duplicate, check_new_full_amount,
                                check_project_exists, check_project_is_closed,
                                check_project_is_invested)
from app.core.db import get_async_session
from app.crud.charity_project import charity_project_crud
from app.crud.servises import invest_funds
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.core.user import current_superuser

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
) -> CharityProjectDB:
    await check_name_duplicate(charity_project.name, session)
    new_charity_project = await charity_project_crud.create(charity_project, session)
    await invest_funds(session)
    return new_charity_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
) -> list[CharityProjectDB]:
    all_charity_projects = await charity_project_crud.get_multi(session)
    return all_charity_projects


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
) -> CharityProjectDB:
    charity_project = await check_project_exists(project_id, session)
    await check_project_is_closed(charity_project)
    await check_project_is_invested(project_id, session)
    charity_project = await charity_project_crud.remove(charity_project, session)
    return charity_project


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
        project_id: int,
        new_charity_project: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
) -> CharityProjectDB:
    charity_project = await check_project_exists(
        project_id, session)
    await check_project_is_closed(charity_project)
    if new_charity_project.name:
        await check_name_duplicate(new_charity_project.name, session)
    if new_charity_project.full_amount and charity_project.invested_amount:
        charity_project = await check_new_full_amount(charity_project, new_charity_project)
    charity_project = await charity_project_crud.update(charity_project, new_charity_project, session)
    return charity_project
