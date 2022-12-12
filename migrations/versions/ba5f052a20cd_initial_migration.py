"""Initial migration.

Revision ID: ba5f052a20cd
Revises: e83b9147551d
Create Date: 2022-12-12 18:18:10.364789

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ba5f052a20cd'
down_revision = 'e83b9147551d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_column('repeticiones')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.add_column(sa.Column('repeticiones', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))

    # ### end Alembic commands ###