"""empty message

Revision ID: 6cf1e8b3dd03
Revises: e4901c3826c0
Create Date: 2019-10-23 18:40:36.311426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cf1e8b3dd03'
down_revision = 'e4901c3826c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.drop_column('users', 'mermber_since')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('mermber_since', sa.DATETIME(), nullable=True))
    op.drop_column('users', 'member_since')
    # ### end Alembic commands ###