from typing import Optional

from pydantic import BaseModel


class STaskadd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskadd):
     id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id : int
