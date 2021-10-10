"""'edit'

Revision ID: d24cc15c0684
Revises: fe179501f99f
Create Date: 2021-10-08 23:06:26.401046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd24cc15c0684'
down_revision = 'fe179501f99f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_migration')
    op.drop_column('divisionOrPhylum', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('divisionOrPhylum', sa.Column('test', sa.VARCHAR(length=30), nullable=True))
    op.create_table('test_migration',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=38), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###