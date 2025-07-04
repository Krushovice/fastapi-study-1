"""add poster field

Revision ID: d8fa1fcfab4c
Revises: f08280997d1c
Create Date: 2025-05-27 17:07:22.615913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8fa1fcfab4c'
down_revision: Union[str, None] = 'f08280997d1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('poster', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('films', 'poster')
    # ### end Alembic commands ###
