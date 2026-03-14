from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.routes import auth, orders
from app.core.exceptions import http_exception_handler, validation_exception_handler, general_exception_handler

app = FastAPI(
    title="Orders API",
    description="REST API для управления заказами",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(orders.router)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

@app.get("/")
def root():
    return {"message": "API работает. Документация: /docs"}