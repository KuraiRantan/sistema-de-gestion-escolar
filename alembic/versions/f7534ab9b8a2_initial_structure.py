"""Initial structure

Revision ID: f7534ab9b8a2
Revises: 
Create Date: 2024-03-16 09:55:18.513402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7534ab9b8a2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('student',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('typeOfIdentification', sa.String(), nullable=False),
        sa.Column('identification', sa.String(), nullable=False),
        sa.Column('firstName', sa.String(), nullable=False),
        sa.Column('lastName', sa.String(), nullable=False),
        sa.Column('birthdate', sa.Date(), nullable=False),
        sa.Column('gender', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('phone', sa.String(), nullable=True),
        sa.Column('currentGrade', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table('subject',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table('classroom',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('capacity', sa.Integer(), nullable=False),
        sa.Column('ubication', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table('attendance',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('student', sa.Integer(), nullable=False),
        sa.Column('subject', sa.Integer(), nullable=False),
        sa.Column('classroom', sa.Integer(), nullable=False),
        sa.Column('grade', sa.String(), nullable=False),
        sa.Column('attendanceDate', sa.Date(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['classroom'], ['classroom.id'], name='fk_attendance_classroom'),
        sa.ForeignKeyConstraint(['student'], ['student.id'], name='fk_attendance_student'),
        sa.ForeignKeyConstraint(['subject'], ['subject.id'], name='fk_attendance_subject'),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    # Drop foreign key constraints to avoid problems.
    op.drop_constraint(table_name='attendance',constraint_name='fk_attendance_classroom')
    op.drop_constraint(table_name='attendance',constraint_name='fk_attendance_student')
    op.drop_constraint(table_name='attendance',constraint_name='fk_attendance_subject')
    # Drop tables
    op.drop_table('student')
    op.drop_table('classroom')
    op.drop_table('subject')
    op.drop_table('attendance')

