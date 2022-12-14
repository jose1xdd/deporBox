"""Initial migration.

Revision ID: 03b2a77b6f84
Revises: f16876596787
Create Date: 2022-12-11 18:12:12.421285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03b2a77b6f84'
down_revision = 'f16876596787'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cedula', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('type_doc', sa.Text(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('fecha_nacimiento', sa.DateTime(), nullable=False),
    sa.Column('sexo', sa.String(length=1), nullable=False),
    sa.Column('direccion', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cedula'),
    sa.UniqueConstraint('email')
    )
    op.create_table('binarios_usuarios',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('foto_perfil', sa.LargeBinary(), nullable=True),
    sa.Column('foto_documento', sa.LargeBinary(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('test',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trimestre', sa.Text(), nullable=False),
    sa.Column('fuerza_general', sa.Integer(), nullable=False),
    sa.Column('brazos', sa.Integer(), nullable=False),
    sa.Column('piernas', sa.Integer(), nullable=False),
    sa.Column('abdomen', sa.Integer(), nullable=False),
    sa.Column('resistencia_fuerza', sa.Integer(), nullable=False),
    sa.Column('resistencia_vueltas', sa.Integer(), nullable=False),
    sa.Column('repeticiones', sa.Integer(), nullable=False),
    sa.Column('resistencia_fuerzaG', sa.Integer(), nullable=False),
    sa.Column('peso', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    op.drop_table('binarios_usuarios')
    op.drop_table('user')
    # ### end Alembic commands ###
