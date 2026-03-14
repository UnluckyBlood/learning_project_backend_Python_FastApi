from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

#обработчик исключений, возвращает ошибки jsonom 


# 404 ошибка, возвращает код,сообщ,путь
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error":{
                "code": exc.status_code,
                "message": exc.detail,
                "path": request.url.path
            }
        }
    )

# 422 ошибка, ошибка валидации, детали ошибок в сообщение
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "code": 422,
                "message": "Ошибка валидации",
                "details": exc.errors(),
                "path": request.url.path
            }
        }
    )

# 500 ошибка, непредвиденные исключения
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error":{
                "code": 500,
                "message": "Внутренняя ошибка сервера",
                "path": request.url.path
            }
        }
    )