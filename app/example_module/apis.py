from fastapi import APIRouter

from app.example_module import schemas

router = APIRouter()


@router.get("/", summary="Example Endpoint", response_model=schemas.TheMessage)
async def example_endpoint():
    return schemas.TheMessage(
        content="Accepting the Mandate of Heaven, May the People Live Long and Railway Forever Prosper"
    )
