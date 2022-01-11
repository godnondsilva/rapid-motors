"""remove color

Revision ID: dfef5452e0d0
Revises: 0a75a6427448
Create Date: 2022-01-11 10:02:50.287931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfef5452e0d0'
down_revision = '0a75a6427448'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cars', 'color')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('color', sa.VARCHAR(length=10), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
