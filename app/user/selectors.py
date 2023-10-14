from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.user import models


def get_user(email: str, db: Session):
    """This function returns a user obj from the database

    Args:
        email (str): The user's email
        db (Session): The DB session

    Returns:
        models.User: The user obj
    """
    user = db.query(models.User).filter_by(email=email).first()
    if user and user.is_active:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
