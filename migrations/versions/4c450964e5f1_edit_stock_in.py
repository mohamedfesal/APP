"""edit stock in

Revision ID: 4c450964e5f1
Revises: a547cc32ac79
Create Date: 2022-05-22 19:12:23.291552

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4c450964e5f1'
down_revision = 'a547cc32ac79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deliveryNote', sa.Integer(), nullable=True),
    sa.Column('item', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['deliveryNote'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['item'], ['stock.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('delivery_items')
    op.drop_table('delivery')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=250), nullable=True),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('delivery_items',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('deliveryNote', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('item', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('quantity', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['deliveryNote'], ['delivery.id'], name='delivery_items_ibfk_1'),
    sa.ForeignKeyConstraint(['item'], ['stock.id'], name='delivery_items_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('order_items')
    op.drop_table('orders')
    # ### end Alembic commands ###
