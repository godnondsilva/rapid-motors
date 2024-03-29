"""add color

Revision ID: fc9da6e8e240
Revises: dfef5452e0d0
Create Date: 2022-01-11 10:03:02.433645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc9da6e8e240'
down_revision = 'dfef5452e0d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('color', sa.String(length=30), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cars', 'color')
    # ### end Alembic commands ###
