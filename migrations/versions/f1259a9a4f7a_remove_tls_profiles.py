"""remove TLs profiles

Revision ID: f1259a9a4f7a
Revises: 08375a3602bf
Create Date: 2022-03-10 15:20:21.487255

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f1259a9a4f7a'
down_revision = '08375a3602bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='tls')
    op.drop_table('tls')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tls',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('bio', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('password', mysql.VARCHAR(length=250), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('address', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('date_created', mysql.DATETIME(), nullable=True),
    sa.Column('statue', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('role', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('email', 'tls', ['email'], unique=False)
    # ### end Alembic commands ###
