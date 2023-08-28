from sqlalchemy.orm import Session

from app.user import models, schemas
from app.user.security import hash_password
from app.user.validators import validate_user


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
