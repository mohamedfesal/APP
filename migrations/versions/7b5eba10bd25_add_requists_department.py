"""add requists department

Revision ID: 7b5eba10bd25
Revises: dc3723b7e81a
Create Date: 2022-02-07 04:06:37.642217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b5eba10bd25'
down_revision = 'dc3723b7e81a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('depart_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'requests', 'department', ['depart_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'requests', type_='foreignkey')
    op.drop_column('requests', 'depart_id')
    # ### end Alembic commands ###
