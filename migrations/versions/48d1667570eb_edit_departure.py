"""edit departure

Revision ID: 48d1667570eb
Revises: 788fc83d456b
Create Date: 2022-01-27 13:45:42.176780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48d1667570eb'
down_revision = '788fc83d456b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dep_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('depart_name', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'department', ['depart_name'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'depart_name')
    op.drop_table('department')
    # ### end Alembic commands ###