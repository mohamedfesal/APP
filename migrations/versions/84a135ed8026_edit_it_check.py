"""edit it check

Revision ID: 84a135ed8026
Revises: 5cbd6767ab9c
Create Date: 2022-02-04 06:07:55.483700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84a135ed8026'
down_revision = '5cbd6767ab9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departure', sa.Column('statue', sa.Boolean(), nullable=True))
    op.add_column('itcheck', sa.Column('internalEmail', sa.Boolean(), nullable=True))
    op.add_column('itcheck', sa.Column('externalEmail', sa.Boolean(), nullable=True))
    op.add_column('itcheck', sa.Column('comment', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('itcheck', 'comment')
    op.drop_column('itcheck', 'externalEmail')
    op.drop_column('itcheck', 'internalEmail')
    op.drop_column('departure', 'statue')
    # ### end Alembic commands ###
