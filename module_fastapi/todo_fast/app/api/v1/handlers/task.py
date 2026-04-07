from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.task_schema import TaskCreate, TaskDetails, TaskUpdate
from app.models.user_model import User
from app.api.dependencies.user_deps import get_current_user
from app.services.task_service import TaskService

task_router = APIRouter()


@task_router.get("/", summary="Lista as tarefas do usuário", response_model=List[TaskDetails])
async def list_tasks(
    user: User = Depends(get_current_user)
)-> List[TaskDetails]:
    return await TaskService.list_tasks_by_user(user) 


@task_router.post("/", summary="Adiciona tarefa", response_model=TaskDetails)
async def create_task(
    data: TaskCreate,
    user: User = Depends(get_current_user)
)-> TaskDetails:
    return await TaskService.create_task(user, data)


@task_router.put("/{task_id}", summary="Atualiza uma tarefa", response_model=TaskDetails)
async def update_task(
    task_id: UUID,
    task_update: TaskUpdate,
    user: User = Depends(get_current_user),
) -> TaskDetails:
    task = await TaskService.get_task_by_id(task_id)
    if not task or task.owner.id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada."
        )
    
    updated = await TaskService.update_task(task_id, task_update)
    return updated


@task_router.delete("/{task_id}", summary="Deleta uma tarefa")
async def delete_task(
    task_id: UUID,
    user: User = Depends(get_current_user),
):
    task = await TaskService.get_task_by_id(task_id)
    if not task or task.owner.id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada."
        )
    
    await TaskService.delete_task(task_id)
    return {"detail": "Tarefa deletada com sucesso."}