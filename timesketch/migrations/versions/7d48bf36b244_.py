"""Change type for query_string

Revision ID: 7d48bf36b244
Revises: ecf00882f546
Create Date: 2017-07-05 15:58:12.765562

"""
# This code is auto generated. Ignore linter errors.
# pylint: skip-file

# revision identifiers, used by Alembic.
revision = '7d48bf36b244'
down_revision = 'ecf00882f546'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('view', 'query_string', type_=sa.UnicodeText)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('view', 'query_string', type_=sa.Unicode(255))
    # ### end Alembic commands ###
