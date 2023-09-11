from datetime import datetime
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.config.settings import settings
from app.dependencies import get_db
from app.user import models, schemas, selectors
from app.user.exceptions import InvalidTokenException
from app.user.security import create_access_token, hash_password, verify_password
from app.user.validators import validate_user


# NOTE: This doesnt allow login with email and password on the swagger docs
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="user/login")


def create_user(user: schemas.UserCreate, db: Session):
    """This function creates a new user entry in the database

    Args:
        user (schemas.UserCreate): The user schema obj
        db (Session): The DB session

    Returns:
        models.User: The created user obj
    """
    validate_user(user=user, db=db)
    obj = models.User(**user.model_dump())
    obj.password = hash_password(raw=user.password)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def login_user(user_credentials: schemas.UserLogin, db: Session):
    """This function logs in a user

    Args:
        user_credentials (schemas.UserLogin): The user login schema obj
        db (Session): The DB session

    Returns:
        schemas.Token: The JWT token
    """
    user = authenticate_user(
        email=user_credentials.email, password=user_credentials.password, db=db
    )
    access_token = create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="Bearer")


def authenticate_user(email: str, password: str, db: Session):
    """This function authenticates a user

    Args:
        email (str): The user's email
        password (str): The user's password
        db (Session): The DB session

    Raises:
        HTTPException[400]: Incorrect email or password
        HTTPException[404]: User not found

    Returns:
        models.User: The authenticated user obj
    """
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if not verify_password(plain_password=password, hashed_password=user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )
    user.last_login = datetime.now()
    db.commit()
    db.refresh(user)
    return user


def get_current_user(
    token: str = Depends(OAUTH2_SCHEME), db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.HASHING_ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise InvalidTokenException
        user = selectors.get_user(email=email, db=db)
        return user
    except JWTError:
        raise InvalidTokenException
