"""empty message

Revision ID: d59e204e8dfa
Revises: 
Create Date: 2020-07-25 14:29:09.437575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd59e204e8dfa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key_phrase', sa.String(length=1000), nullable=True),
    sa.Column('creation_timestamp', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('last_run_timestamp', sa.DateTime(), nullable=True),
    sa.Column('single_run_only', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job_results',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('run_timestamp', sa.DateTime(), nullable=False),
    sa.Column('query_result', sa.String(length=1000), nullable=False),
    sa.Column('positive_count', sa.Integer(), nullable=True),
    sa.Column('negative_count', sa.Integer(), nullable=True),
    sa.Column('neutral_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], ),
    sa.PrimaryKeyConstraint('job_id', 'run_timestamp', 'query_result')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_results')
    op.drop_table('jobs')
    # ### end Alembic commands ###
