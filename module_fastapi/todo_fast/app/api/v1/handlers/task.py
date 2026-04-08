from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.v1.handlers import user
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

@task_router.get("/{task_id}", summary="Detalhe de uma Tarefa or id", response_model=TaskDetails)
async def detail(
    task_id: UUID,
    user: User = Depends(get_current_user)):
    return await TaskService.detail(user, task_id)

@task_router.post("/", summary="Adiciona tarefa", response_model=TaskDetails)
async def create_task(
    data: TaskCreate,
    user: User = Depends(get_current_user)
)-> TaskDetails:
    return await TaskService.create_task(user, data)


@task_router.put("/{task_id}", summary="Atualiza tarefa", response_model=TaskDetails)
async def update_task(
    task_id: UUID,
    data: TaskUpdate,
    user: User = Depends(get_current_user)):
    return await TaskService.update_task(user, task_id, data)

@task_router.delete("/{task_id}", summary="Deleta tarefa")
async def delete_task(
    task_id: UUID,
    user: User = Depends(get_current_user)):    
    await TaskService.delete_task(user, task_id)
    return None