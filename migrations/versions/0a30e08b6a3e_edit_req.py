"""edit req

Revision ID: 0a30e08b6a3e
Revises: abe238432b54
Create Date: 2022-02-06 03:37:38.141233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a30e08b6a3e'
down_revision = 'abe238432b54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reqtype', sa.Column('reqstatue', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reqtype', 'reqstatue')
    # ### end Alembic commands ###
