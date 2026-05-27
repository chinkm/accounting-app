from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
#from app.schemas.user import UserCreate, UserResponse   
from app.core.config import settings

#password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

#secret key and algorithm for JWT
SECRET_KEY = settings.SECRET_KEY #should be a secure random string in production and stored in environment variables
ALGORITHM = settings.ALGORITHM #e.g. "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES #e.g. 30

def verify_password(plain_password:str, hashed_password: str)->bool:
    #check if the provided password matches the hashed password
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password:str)->str:
    #hash the provided password
    return pwd_context.hash(str(password))

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None)->str:
    #create a JWT access token with the provided data and expiration time
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User: # Adding a return type helps Pylance down the line
    #decode the JWT token and retrieve the current user from the database
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # 1. Extract the username (or user ID) from the token payload
        username: str | None = payload.get("sub")
        # 2. If the username is not found in the token, raise an exception
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.name == username).first()
    if user is None:
        raise credentials_exception
    return user
