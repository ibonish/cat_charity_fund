"""Sec

Revision ID: 66f7de17ff72
Revises: 582d16584726
Create Date: 2024-02-14 02:34:37.322836

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '66f7de17ff72'
down_revision = '582d16584726'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charityproject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=False),
    sa.Column('invested_amount', sa.Integer(), nullable=False),
    sa.Column('fully_invested', sa.Boolean(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('chariryproject')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chariryproject',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('full_amount', sa.INTEGER(), nullable=False),
    sa.Column('invested_amount', sa.INTEGER(), nullable=False),
    sa.Column('fully_invested', sa.BOOLEAN(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.Column('close_date', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('charityproject')
    # ### end Alembic commands ###
