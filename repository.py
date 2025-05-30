from itertools import takewhile
from sqlalchemy import select
from typing import List
from database import new_session, TaskOrm
from schemas import STaskadd, STask


class TaskRepository:
    @classmethod
    async def  add_one(cls, data: STaskadd):
        async with  new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def find_all(cls) -> List[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()

            task_schemas = [STask.model_validate(task_model, from_attributes=True) for task_model in task_models]
            return task_schemas