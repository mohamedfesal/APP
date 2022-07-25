"""add pcs categ

Revision ID: 57c5a5906ab5
Revises: 99d38d54e397
Create Date: 2022-07-23 17:50:33.701770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57c5a5906ab5'
down_revision = '99d38d54e397'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'stock', 'orders_history', ['order_quantity'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stock', type_='foreignkey')
    # ### end Alembic commands ###
