"""edit it check

Revision ID: abe238432b54
Revises: 84a135ed8026
Create Date: 2022-02-05 00:22:40.252668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abe238432b54'
down_revision = '84a135ed8026'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('itcheck', sa.Column('vpn', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('itcheck', 'vpn')
    # ### end Alembic commands ###
