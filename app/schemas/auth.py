from pydantic import BaseModel
# ждём логин и пароль текстом
class LoginRequest(BaseModel):
    username: str
    password: str
# ответ при входе, токен и тип "носитель"
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"