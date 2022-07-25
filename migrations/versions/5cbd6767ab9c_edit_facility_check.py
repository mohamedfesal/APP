"""edit facility check

Revision ID: 5cbd6767ab9c
Revises: 9b7472d73600
Create Date: 2022-02-04 05:57:54.985428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cbd6767ab9c'
down_revision = '9b7472d73600'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('facilitycheck', sa.Column('office', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('facilitycheck', 'office')
    # ### end Alembic commands ###