"""edit stock in

Revision ID: 386b84060afa
Revises: 4d30a915b037
Create Date: 2022-05-24 20:15:38.447446

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '386b84060afa'
down_revision = '4d30a915b037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('order_items_ibfk_1', 'order_items', type_='foreignkey')
    op.drop_column('order_items', 'deliveryNote')
    op.drop_column('order_items', 'quantity')
    op.drop_column('orders', 'date')
    op.drop_column('orders', 'title')
    op.drop_constraint('stock_ibfk_3', 'stock', type_='foreignkey')
    op.drop_column('stock', 'stock_order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stock', sa.Column('stock_order', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('stock_ibfk_3', 'stock', 'order_items', ['stock_order'], ['id'])
    op.add_column('orders', sa.Column('title', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('orders', sa.Column('date', mysql.DATETIME(), nullable=True))
    op.add_column('order_items', sa.Column('quantity', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('order_items', sa.Column('deliveryNote', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('order_items_ibfk_1', 'order_items', 'orders', ['deliveryNote'], ['id'])
    # ### end Alembic commands ###
