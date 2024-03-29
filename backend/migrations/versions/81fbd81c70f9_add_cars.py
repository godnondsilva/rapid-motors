"""add cars

Revision ID: 81fbd81c70f9
Revises: 2f8854503768
Create Date: 2021-12-12 06:19:56.594526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81fbd81c70f9'
down_revision = '2f8854503768'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('model_id', sa.Integer(), nullable=False),
    sa.Column('car_name', sa.String(length=30), nullable=False),
    sa.Column('model_year', sa.Numeric(precision=4), nullable=False),
    sa.Column('color', sa.String(length=10), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.admin_id'], ),
    sa.PrimaryKeyConstraint('model_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    # ### end Alembic commands ###
