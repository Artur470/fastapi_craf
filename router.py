from typing import Annotated

from fastapi import APIRouter, Depends
from typing import List
from repository import TaskRepository
from schemas import STaskadd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags = ["таски"]

)


@router.post("")

async def add_task(
        task:  Annotated[STaskadd, Depends()],

) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True,"task_id": task_id}




@router.get("", response_model=List[STask])
async def get_tasks() -> List[STask]:
    tasks = await TaskRepository.find_all()
    return tasks