from fastapi import HTTPException


class CustomExceptionHandler(HTTPException):
    def __init__(self, status_code: int = 500, detail: str = 'Internal Server Error'):
        super().__init__(status_code=status_code, detail=detail)
