"""edit tls team

Revision ID: f99518ff6647
Revises: 8916cdc8066a
Create Date: 2022-03-12 03:06:33.887503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f99518ff6647'
down_revision = '8916cdc8066a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wfh_pcs', sa.Column('token', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wfh_pcs', 'token')
    # ### end Alembic commands ###
