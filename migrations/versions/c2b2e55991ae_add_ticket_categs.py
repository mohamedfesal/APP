"""add ticket categs

Revision ID: c2b2e55991ae
Revises: d391c18a0d6d
Create Date: 2022-03-08 13:55:59.328071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2b2e55991ae'
down_revision = 'd391c18a0d6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ticket_cat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ticket_subcat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('ticket_cat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ticket_cat_id'], ['ticket_cat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket_subcat')
    op.drop_table('ticket_cat')
    # ### end Alembic commands ###
