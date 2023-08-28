from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    DateTime,
)

from app.config.database import DBBase


class User(DBBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)  # If the user account is disabled or not
    last_login = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now())
