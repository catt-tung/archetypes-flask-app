"""empty message

Revision ID: 473e5800a8b5
Revises: 819affafa30b
Create Date: 2022-04-12 14:32:57.951687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '473e5800a8b5'
down_revision = '819affafa30b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='profiles_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='profiles_pkey')
    )
    # ### end Alembic commands ###
