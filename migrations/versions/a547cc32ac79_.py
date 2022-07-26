"""empty message

Revision ID: a547cc32ac79
Revises: 686d8ea9a9cf
Create Date: 2022-05-21 13:42:43.586891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a547cc32ac79'
down_revision = '686d8ea9a9cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('delivery_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deliveryNote', sa.Integer(), nullable=True),
    sa.Column('item', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['deliveryNote'], ['delivery.id'], ),
    sa.ForeignKeyConstraint(['item'], ['stock.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delivery_items')
    op.drop_table('delivery')
    # ### end Alembic commands ###
