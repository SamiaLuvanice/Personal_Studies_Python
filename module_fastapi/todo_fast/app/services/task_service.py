from typing import List, Optional
from uuid import UUID

from app.models.task_model import Task
from app.models.user_model import User
from app.schemas.task_schema import TaskCreate, TaskUpdate


class TaskService:
    @staticmethod
    async def create_task(user: User, data: TaskCreate) -> Task:
        new_task = Task(**data.dict(), owner=user)
        return await new_task.insert()
         
    @staticmethod
    async def list_tasks_by_user(user: User) -> List[Task]:
        tasks = await Task.find(Task.owner.id == user.id).to_list()
        return tasks

    @staticmethod
    async def detail(user: User, task_id: UUID) -> Optional[Task]:
        task = await Task.find_one(Task.task_id == task_id, Task.owner.id == user.id)
        return task

    @staticmethod
    async def update_task(user: User, task_id: UUID, data: TaskUpdate) -> Optional[Task]:
        task = await TaskService.detail(user, task_id)
        await task.update({
            "$set": data.dict(exclude_unset=True)
        })   
        await task.save()
        return task

    @staticmethod
    async def delete_task(user: User, task_id: UUID) -> None:
        task = await TaskService.detail(user, task_id)
        if not task:
            return
        await task.delete()
    