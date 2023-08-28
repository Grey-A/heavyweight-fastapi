"""created_user_table

Revision ID: 76ac90e94d8d
Revises: 
Create Date: 2023-08-28 23:54:26.343024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "76ac90e94d8d"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(20), nullable=False),
        sa.Column("last_name", sa.String(20), nullable=False),
        sa.Column("email", sa.String, nullable=False, unique=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("last_login", sa.DateTime),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("users")
