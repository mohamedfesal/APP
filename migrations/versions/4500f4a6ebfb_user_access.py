"""user access

Revision ID: 4500f4a6ebfb
Revises: 67fbcc3127ba
Create Date: 2022-07-05 02:30:28.497404

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4500f4a6ebfb'
down_revision = '67fbcc3127ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='access_contrl')
    op.drop_table('access_contrl')
    op.drop_table('user_access')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_access',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('user_access_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('access_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['access_id'], ['access_contrl.id'], name='user_access_ibfk_1', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_access_id'], ['users.id'], name='user_access_ibfk_2', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('access_contrl',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'access_contrl', ['name'], unique=False)
    # ### end Alembic commands ###
