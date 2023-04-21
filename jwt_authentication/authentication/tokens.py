from datetime import timedelta, datetime
from jose import JWTError, jwt
from config import Settings
from . import schemas


FORGOT_PASSWORD_SECRET_KEY = Settings().FORGOT_PASSWORD_SECRET_KEY
FORGOT_PASSWORD_EXPIRE_MINUTES = 60
ALGORITHM = Settings().ALGORITHM


def create_forgot_password_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=FORGOT_PASSWORD_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, FORGOT_PASSWORD_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_forgot_password_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, FORGOT_PASSWORD_SECRET_KEY, algorithms=[ALGORITHM])
        if email := payload.get("sub"):
            token_data = schemas.TokenData(email=email)
        else:
            raise credentials_exception
        return token_data
    except JWTError as e:
        raise credentials_exception from e