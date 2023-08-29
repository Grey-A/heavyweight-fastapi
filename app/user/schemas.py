from datetime import datetime
from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    first_name: str = Field(description="The User's first name", max_length=50)
    last_name: str = Field(description="The User's last name", max_length=50)
    email: str = Field(description="The User's email address", max_length=255)


# This will be used when creating a new user
class UserCreate(BaseUser):
    password: str = Field(description="The User's Raw password", max_length=255)


# This will be used when we need to return a user obj
class User(BaseUser):
    is_active: bool = Field(description="If the user account is disabled or not")
    last_login: datetime | None = Field(description="The User's last login date")
    created_at: datetime = Field(description="The User's creation date")


class UserLogin(BaseModel):
    email: str = Field(description="The User's email address", max_length=255)
    password: str = Field(description="The User's Raw password", max_length=255)


class Token(BaseModel):
    access_token: str = Field(description="The JWT access token")
    token_type: str = Field(description="The JWT token type")
