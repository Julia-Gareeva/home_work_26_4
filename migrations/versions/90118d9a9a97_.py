"""empty message

Revision ID: 90118d9a9a97
Revises: 
Create Date: 2022-11-25 05:25:18.345225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90118d9a9a97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=15), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###
