from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.user import models, schemas


# NOTE: Validators are very sensitive so when implementing one, make sure to test it thoroughly


def validate_user(user: schemas.UserCreate, db: Session):
    """This function validates the user data and confirms that it can be saved to db

    Args:
        user (schemas.UserCreate): The user schema obj
        db (Session): The DB Session

    Raises:
        HTTPException[409]: When the obj doesnt satisfy the conditions to be saved to db

    Returns:
       bool[True]: If the UserCreate obj is valid
    """

    # Check if email is taken
    if db.query(models.User).filter_by(email=user.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email taken")
    return True
