from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.ping import router as ping_router

app = FastAPI()

app.include_router(health_router)

app.include_router(ping_router,prefix="/limiter")
