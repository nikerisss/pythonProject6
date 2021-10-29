"""First commit

Revision ID: b11c11ba0667
Revises: 
Create Date: 2021-10-29 09:59:21.788762

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = 'b11c11ba0667'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=20), nullable=True),
    sa.Column('firstname', sa.VARCHAR(length=20), nullable=True),
    sa.Column('lastname', sa.VARCHAR(length=20), nullable=True),
    sa.Column('email', sa.VARCHAR(length=20), nullable=True),
    sa.Column('password', sa.VARCHAR(length=20), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('user_status', sa.VARCHAR(length=30), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('Credit',
    sa.Column('credit_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('credit_limit', sa.Integer(), nullable=True),
    sa.Column('duration', sa.Date(), nullable=True),
    sa.Column('credit_currency', sa.VARCHAR(length=20), nullable=True),
    sa.Column('passport_number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.user_id'], ),
    sa.PrimaryKeyConstraint('credit_id')
    )
    op.create_table('Payment',
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('credit_id', sa.Integer(), nullable=True),
    sa.Column('payment', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['credit_id'], ['Credit.credit_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.user_id'], ),
    sa.PrimaryKeyConstraint('payment_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Payment')
    op.drop_table('Credit')
    op.drop_table('User')
    # ### end Alembic commands ###
