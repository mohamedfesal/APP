"""edit departure

Revision ID: ec79ce0b031d
Revises: 6220ac66be37
Create Date: 2022-01-26 14:19:29.216210

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ec79ce0b031d'
down_revision = '6220ac66be37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departure_req', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_constraint('departure_req_ibfk_1', 'departure_req', type_='foreignkey')
    op.drop_column('departure_req', 'facility_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departure_req', sa.Column('facility_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('departure_req_ibfk_1', 'departure_req', 'facility_check', ['facility_id'], ['id'])
    op.drop_column('departure_req', 'id')
    # ### end Alembic commands ###
