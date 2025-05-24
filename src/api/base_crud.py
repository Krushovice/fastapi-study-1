from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


class BaseCRUD[TModel, TCreateSchema, TUpdateSchema]:
    """
    Универсальный базовый класс, который умеет делать CRUD-операции
    с учетом Pydantic-схем для create и update."""

    model: TModel

    @classmethod
    async def create(
        cls,
        session: AsyncSession,
        schema_in: TCreateSchema,
    ) -> TModel | None:
        """Создать одну запись из схемы `TCreateSchema`"""
        obj = cls.model(**schema_in.model_dump())
        session.add(obj)
        try:
            await session.commit()
            return obj
        except SQLAlchemyError as e:
            await session.rollback()
            print(f"Ошибка при создании объекта: {e}")
            return None

    @classmethod
    async def read(
        cls,
        session: AsyncSession,
        pk: int,
    ) -> TModel | None:

        stmt = select(cls.model).filter_by(id=pk)
        film = await session.execute(stmt)

        return film.scalar_one_or_none()

    @classmethod
    async def read_by_filters(
        cls,
        session: AsyncSession,
        relation_name: str | None = None,
        **filters,
    ) -> TModel | None:
        """
        Получить одну запись, удовлетворя фильтрам.
        Если передан relation_name, жадно подгружаем указанную связь (relationship).
        """
        try:
            query = select(cls.model).filter_by(**filters)

            if relation_name:
                query = query.options(selectinload(getattr(cls.model, relation_name)))

            result = await session.execute(query)
            return result.scalar_one_or_none()

        except SQLAlchemyError as e:
            await session.rollback()
            print(f"Ошибка при поиске объекта: {e}")
            return None

    @classmethod
    async def read_all(
        cls,
        session: AsyncSession,
        **filters,
    ) -> Sequence[TModel]:
        """
        Получить все записи, удовлетворяя фильтрам (или все, если не заданы).
        """
        try:
            query = select(cls.model)
            if filters:
                query = query.filter_by(**filters)
            result = await session.execute(query)
            return result.scalars().all()
        except SQLAlchemyError as e:
            await session.rollback()
            print(f"Ошибка при получении списка объектов: {e}")
            return []

    @classmethod
    async def read_with_relation(
        cls,
        session: AsyncSession,
        pk: int,
        relation_name: str,
    ) -> TModel | None:
        """
        Получает объект модели по primary key (id=pk),
        а также жадно подгружает связь relation_name.
        """
        try:
            query = (
                select(cls.model)
                .filter_by(id=pk)
                .options(selectinload(getattr(cls.model, relation_name)))
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            await session.rollback()
            print(f"Ошибка при загрузке связанной модели {relation_name}: {e}")
            return None

    @classmethod
    async def update(
        cls,
        session: AsyncSession,
        pk: int,
        schema_in: TUpdateSchema,
    ) -> TModel | None:
        """
        Обновить запись по primary key, используя схему `TUpdateSchema`.
        """
        obj = await cls.read(session, pk)
        if not obj:
            return None

        try:
            # Применяем к объекту все поля из схемы (кроме unset).
            # Если нужно – можно использовать exclude_none=True или exclude_unset=True.
            update_data = schema_in.model_dump(exclude_unset=True)
            for attr, value in update_data.items():
                setattr(obj, attr, value)

            session.add(obj)
            await session.commit()
            return obj

        except SQLAlchemyError as e:
            await session.rollback()
            print(f"Ошибка при обновлении объекта: {e}")
            return None

    @classmethod
    async def delete(
        cls,
        session: AsyncSession,
        pk: int,
    ) -> bool:
        """Удалить запись"""
        obj = await cls.read(session, pk)
        if not obj:
            return False
        try:
            await session.delete(obj)
            await session.commit()
            return True
        except SQLAlchemyError as e:
            await session.rollback()
            print(f"Ошибка при удалении объекта: {e}")
            return False
