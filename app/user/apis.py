from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.user import schemas, security, services

router = APIRouter()


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.User,
)
def user_create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Directly call the service function to create a new user
    return services.create_user(user=user, db=db)


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=schemas.Token,
)
def user_login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db),
):
    # Directly call the service function to login
    return services.login_user(user_credentials=user, db=db)


@router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    response_model=schemas.User,
)
def user_details(user: schemas.User = Depends(services.get_current_user)):
    # Directly return the user obj
    return user
