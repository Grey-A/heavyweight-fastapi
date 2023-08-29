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
    return db.query(models.User).filter_by(email=email).first()
