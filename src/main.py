from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core.middlewares import ProcessTimeMiddleware
from src.users.router import users_router


def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI service")

    v1_api_router = APIRouter()
    v1_api_router.include_router(users_router, prefix="/users", tags=["Users"])

    app.include_router(v1_api_router, prefix="/api/v1")

    app.add_middleware(ProcessTimeMiddleware, some_attribute="process_time")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_app()
