"""edit requists

Revision ID: a4dbde8dd9c8
Revises: b9409b415248
Create Date: 2022-01-28 09:31:28.448049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4dbde8dd9c8'
down_revision = 'b9409b415248'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('dep_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'requests', 'departure', ['dep_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'requests', type_='foreignkey')
    op.drop_column('requests', 'dep_id')
    # ### end Alembic commands ###
