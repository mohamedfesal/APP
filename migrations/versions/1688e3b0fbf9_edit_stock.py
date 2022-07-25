"""edit stock

Revision ID: 1688e3b0fbf9
Revises: 072479d6028d
Create Date: 2022-06-30 18:07:05.694806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1688e3b0fbf9'
down_revision = '072479d6028d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stock', sa.Column('order_quantity', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'stock', 'orders', ['stock_order'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stock', type_='foreignkey')
    op.drop_column('stock', 'order_quantity')
    # ### end Alembic commands ###
