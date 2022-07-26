"""add tickets

Revision ID: fff5f43ba9de
Revises: 5d4072ab3f73
Create Date: 2022-03-09 12:38:34.253315

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fff5f43ba9de'
down_revision = '5d4072ab3f73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('ticket_sub_cat', sa.Integer(), nullable=True))
    op.drop_constraint('tickets_ibfk_1', 'tickets', type_='foreignkey')
    op.create_foreign_key(None, 'tickets', 'ticket_subcat', ['ticket_sub_cat'], ['id'])
    op.drop_column('tickets', 'ticket_cat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('ticket_cat', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'tickets', type_='foreignkey')
    op.create_foreign_key('tickets_ibfk_1', 'tickets', 'ticket_cat', ['ticket_cat'], ['id'])
    op.drop_column('tickets', 'ticket_sub_cat')
    # ### end Alembic commands ###
