from fastapi import FastAPI

from src.routers import lamoda_router, twitch_router

app = FastAPI()

app.include_router(lamoda_router.router, prefix="/lamoda", tags=["lamoda"])
app.include_router(twitch_router.router, prefix="/twitch", tags=["twitch"])
