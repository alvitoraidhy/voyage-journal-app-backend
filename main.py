from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Response

from config import current_env as config
from controllers.auth import views as auth_views
from controllers.note import views as note_views
import context


app = FastAPI(title="Journal App", version="1.0.0", root_path="/api/v1")
app.include_router(auth_views.router, prefix="/auth")
app.include_router(note_views.router, prefix="/notes")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    # Set up logging format
    context.logging.basicConfig(level=config.LOG_LEVEL)

    return


@app.get("/ping")
async def get_ping():
    return Response(None, 204)


register_tortoise(
    app,
    db_url=config.DB_URL,
    modules={"models": ["models"]},
    add_exception_handlers=True,
)
