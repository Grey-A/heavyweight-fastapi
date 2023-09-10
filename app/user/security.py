from fastapi import Form
from jose import jwt
from typing import Annotated, Union
from passlib.context import CryptContext

from app.config.settings import settings


class OAuth2PasswordRequestForm:
    """
    Custom OAuth2PasswordRequestForm Based on fast.security.OAuth2PasswordRequestForm which allows email and password login
    """

    def __init__(
        self,
        *,
        grant_type: Annotated[Union[str, None], Form(pattern="password")] = None,
        username: Annotated[str, Form()],
        password: Annotated[str, Form()],
        scope: Annotated[str, Form()] = "",
        client_id: Annotated[Union[str, None], Form()] = None,
        client_secret: Annotated[Union[str, None], Form()] = None,
    ):
        self.grant_type = grant_type
        self.email = username  # NOTE: Take note of here
        self.password = password
        self.scopes = scope.split()
        self.client_id = client_id
        self.client_secret = client_secret


def hash_password(raw: str) -> str:
    """This function hashes a password

    Args:
        raw (str): The raw password

    Returns:
        str: The hashed password
    """
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(raw)


def verify_password(plain_password: str, hashed_password: str):
    """This function verifies a password

    Args:
        plain_password (str): The plain password
        hashed_password (str): The hashed password

    Returns:
        bool: True if the password is correct, False otherwise
    """
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    """This function creates a JWT token

    Args:
        data (dict): The data to be encoded

    Returns:
        str: The JWT token
    """
    return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.HASHING_ALGORITHM)
