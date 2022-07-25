"""add pcs categ

Revision ID: 99d38d54e397
Revises: 75dfb8e1f617
Create Date: 2022-07-23 16:59:19.361996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99d38d54e397'
down_revision = '75dfb8e1f617'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('quantity', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pcs_categ',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pcs', sa.Column('pcs_category', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pcs', 'pcs_categ', ['pcs_category'], ['id'])
    op.create_foreign_key(None, 'stock', 'orders_history', ['order_quantity'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stock', type_='foreignkey')
    op.drop_constraint(None, 'pcs', type_='foreignkey')
    op.drop_column('pcs', 'pcs_category')
    op.drop_table('pcs_categ')
    op.drop_table('orders_history')
    # ### end Alembic commands ###
