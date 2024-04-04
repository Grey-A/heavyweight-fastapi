"""This module contains the schemas for the example module."""

from pydantic import BaseModel, Field

from app.common.schemas import PaginationSchema, ResponseSchema


class Name(BaseModel):
    """The base schema for the name model."""

    first_name: str = Field(description="The first name of the user")
    last_name: str = Field(description="The last name of the user")


class NameResponse(ResponseSchema):
    """The response schema for the names endpoint."""

    data: list[Name] = Field(description="The list of names")
    meta: PaginationSchema = Field(description="The pagination metadata")
