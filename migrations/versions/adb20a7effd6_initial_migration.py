"""Initial migration.

Revision ID: adb20a7effd6
Revises: 
Create Date: 2022-11-10 23:04:47.691115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adb20a7effd6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('binarios_usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('foto_perfil', sa.LargeBinary(), nullable=True),
    sa.Column('foto_documento', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('persona',
    sa.Column('type_doc', sa.Text(), nullable=False),
    sa.Column('id', sa.String(length=30), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('fecha_nacimiento', sa.DateTime(), nullable=False),
    sa.Column('sexo', sa.String(length=10), nullable=False),
    sa.Column('direccion', sa.String(length=30), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('tipo_usuario', sa.String(length=1), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
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
    sa.Column('persona_id', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['persona_id'], ['persona.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    op.drop_table('persona')
    op.drop_table('binarios_usuarios')
    # ### end Alembic commands ###
