from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
# ждём логин и пароль текстом
class LoginRequest(BaseModel):
    username: str
    password: str
# ответ при входе, токен и тип "носитель"
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
# класс для создания пользователей
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=4)
class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)