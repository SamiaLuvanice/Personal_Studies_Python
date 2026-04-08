from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConfigurationError

from app.models.user_model import User
from app.models.task_model import Task

from app.api.v1.router import router

from contextlib import asynccontextmanager

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    client_db = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
    if settings.MONGO_DB_NAME:
        database = client_db[settings.MONGO_DB_NAME]
    else:
        try:
            database = client_db.get_default_database()
        except ConfigurationError as exc:
            raise RuntimeError(
                "Mongo database not defined. Set MONGO_DB_NAME in .env or include the DB name in MONGO_CONNECTION_STRING."
            ) from exc

    await init_beanie(
        database=database,
        document_models=[User, Task],
    )

    app.state.mongo_client = client_db
    try:
        yield
    finally:
        client_db.close()

app.include_router(
    router, 
    prefix=settings.API_V1_STR
)