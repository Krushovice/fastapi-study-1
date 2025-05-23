"""create films table

Revision ID: f08280997d1c
Revises:
Create Date: 2025-05-23 17:27:34.602716

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f08280997d1c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "films",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "title",
            sa.String(length=120),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "genre",
            sa.String(length=50),
            nullable=False,
        ),
        sa.Column(
            "duration",
            sa.Integer(),
            nullable=True,
        ),
        sa.Column(
            "release_date",
            sa.Date(),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_films"),
        ),
    )
    op.create_index(
        op.f("ix_films_title"),
        "films",
        ["title"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_films_title"),
        table_name="films",
    )
    op.drop_table("films")
