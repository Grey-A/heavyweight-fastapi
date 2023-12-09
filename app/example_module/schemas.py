from pydantic import BaseModel, Field


class TheMessage(BaseModel):
    content: str = Field(description="The Message")
