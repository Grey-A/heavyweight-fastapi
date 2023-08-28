from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db

from app.user import schemas, services

router = APIRouter()


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.User,
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Directly call the service function to create a new user
    return services.create_contributor(user=user, db=db)
