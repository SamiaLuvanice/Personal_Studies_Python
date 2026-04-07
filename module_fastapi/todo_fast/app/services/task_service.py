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
    async def get_task_by_id(task_id: UUID) -> Optional[Task]:
        task = await Task.find_one(Task.task_id == task_id)
        return task

    @staticmethod
    async def update_task(task_id: UUID, task_update: TaskUpdate) -> Optional[Task]:
        task = await TaskService.get_task_by_id(task_id)
        if not task:
            return None
        
        update_data = task_update.model_dump(exclude_unset=True)
        await task.update({"$set": update_data})
        return task

    @staticmethod
    async def delete_task(task_id: UUID) -> bool:
        task = await TaskService.get_task_by_id(task_id)
        if not task:
            return False
        await task.delete()
        return True
