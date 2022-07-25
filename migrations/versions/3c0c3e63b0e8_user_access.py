"""user access

Revision ID: 3c0c3e63b0e8
Revises: 0cf50524c4a0
Create Date: 2022-07-05 04:18:50.356811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c0c3e63b0e8'
down_revision = '0cf50524c4a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('access_list', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'access_list')
    # ### end Alembic commands ###
