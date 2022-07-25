"""user access

Revision ID: 0cf50524c4a0
Revises: 4500f4a6ebfb
Create Date: 2022-07-05 02:32:53.287097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cf50524c4a0'
down_revision = '4500f4a6ebfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('access_contrl',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user_access',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_access_id', sa.Integer(), nullable=True),
    sa.Column('access_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['access_id'], ['access_contrl.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_access_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_access')
    op.drop_table('access_contrl')
    # ### end Alembic commands ###
