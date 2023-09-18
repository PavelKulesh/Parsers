import os
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.routers import lamoda_router, twitch_router
from src.exceptions.custom_exception import CustomExceptionHandler

app = FastAPI()


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(os.getenv('REDIS_URI'))
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


@app.exception_handler(CustomExceptionHandler)
async def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


app.include_router(lamoda_router.router, prefix="/lamoda", tags=["lamoda"])
app.include_router(twitch_router.router, prefix="/twitch", tags=["twitch"])
