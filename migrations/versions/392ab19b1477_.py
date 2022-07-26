"""empty message

Revision ID: 392ab19b1477
Revises: 61178c51b416
Create Date: 2022-05-24 21:13:34.624611

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '392ab19b1477'
down_revision = '61178c51b416'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orderitems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deliveryNote', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['deliveryNote'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('order_items')
    op.drop_constraint('stock_ibfk_3', 'stock', type_='foreignkey')
    op.create_foreign_key(None, 'stock', 'orderitems', ['stock_order'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stock', type_='foreignkey')
    op.create_foreign_key('stock_ibfk_3', 'stock', 'order_items', ['stock_order'], ['id'])
    op.create_table('order_items',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('deliveryNote', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('quantity', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['deliveryNote'], ['orders.id'], name='order_items_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('orderitems')
    # ### end Alembic commands ###
