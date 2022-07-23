"""creating phone.no column in the user model

Revision ID: d4a24c706226
Revises: 
Create Date: 2022-07-23 17:44:15.044854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4a24c706226'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('user', sa.Column('phone_no', sa.String(), nullable=True))


def downgrade() -> None:
    pass
