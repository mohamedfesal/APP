"""add tickets

Revision ID: 466f3231cf73
Revises: c2b2e55991ae
Create Date: 2022-03-09 12:20:58.221798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '466f3231cf73'
down_revision = 'c2b2e55991ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('ticket_cat', sa.Integer(), nullable=True),
    sa.Column('impact', sa.String(length=100), nullable=True),
    sa.Column('urgency', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['ticket_cat'], ['ticket_cat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tickets')
    # ### end Alembic commands ###
