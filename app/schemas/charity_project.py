from pydantic import BaseModel, Field, PositiveInt
from typing import Optional
from datetime import datetime


class CharityProjectBase(BaseModel):
    """Базовая схема благотворительного проекта."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt]


class CharityProjectCreate(CharityProjectBase):
    """Схема создания благотворительного проекта."""
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(min_length=1)
    full_amount: PositiveInt


class CharityProjectDB(CharityProjectCreate):
    """Схема возврата данных из БД."""
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class CharityProjectUpdate(CharityProjectBase):
    """Схема обновления благотворительного проекта."""
    pass
