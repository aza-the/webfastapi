"""empty message

Revision ID: d85678736b6c
Revises: 
Create Date: 2022-11-15 18:40:51.154679

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd85678736b6c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'flats',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('district', sa.String(), nullable=True),
        sa.Column('metro_name', sa.String(), nullable=True),
        sa.Column('metro_time', sa.String(), nullable=True),
        sa.Column('metro_get_type', sa.String(), nullable=True),
        sa.Column('size', sa.Float(), nullable=True),
        sa.Column('kitchen', sa.Float(), nullable=True),
        sa.Column('floor', sa.Integer(), nullable=True),
        sa.Column('floors', sa.Integer(), nullable=True),
        sa.Column('constructed', sa.Integer(), nullable=True),
        sa.Column('fix', sa.String(), nullable=True),
        sa.Column('type_of_building', sa.String(), nullable=True),
        sa.Column('type_of_walls', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk__flats')),
    )
    op.create_index(op.f('ix__flats__id'), 'flats', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix__flats__id'), table_name='flats')
    op.drop_table('flats')
    # ### end Alembic commands ###
