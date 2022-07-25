"""edit departure

Revision ID: 35dd963c61b5
Revises: db29b43f7e08
Create Date: 2022-01-26 12:39:29.846909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35dd963c61b5'
down_revision = 'db29b43f7e08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departure_req', sa.Column('agents_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'departure_req', 'agents', ['agents_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'departure_req', type_='foreignkey')
    op.drop_column('departure_req', 'agents_id')
    # ### end Alembic commands ###