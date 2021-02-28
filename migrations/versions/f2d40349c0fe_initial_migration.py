"""Initial Migration

Revision ID: f2d40349c0fe
Revises: bbc30f38984b
Create Date: 2021-03-01 00:36:31.451155

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f2d40349c0fe'
down_revision = 'bbc30f38984b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('pitch_title', sa.String(), nullable=True),
    sa.Column('pitch_body', sa.String(), nullable=True),
    sa.Column('postedBy', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pitches')
    op.drop_constraint('comments_pitch_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'pitch', ['pitch_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_pitch_id_fkey', 'comments', 'pitches', ['pitch_id'], ['id'])
    op.create_table('pitches',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('pitch_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pitch_body', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('postedBy', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='pitches_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pitches_pkey')
    )
    op.drop_table('pitch')
    # ### end Alembic commands ###
