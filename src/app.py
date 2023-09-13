from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.routers import lamoda_router, twitch_router
from src.exceptions.custom_exception import CustomExceptionHandler

app = FastAPI()


@app.exception_handler(CustomExceptionHandler)
async def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


app.include_router(lamoda_router.router, prefix="/lamoda", tags=["lamoda"])
app.include_router(twitch_router.router, prefix="/twitch", tags=["twitch"])
