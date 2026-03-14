from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# функция сравнивания паролей с хэшэм
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)
# создание хэш пароля при реге
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
# формируем jwt и время жизни ставим и секретный ключ подписывается              
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt