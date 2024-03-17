"""Change the table fields from camel case to snake case.


Revision ID: 1e8fb03a5fad
Revises: f7534ab9b8a2
Create Date: 2024-03-16 09:56:35.762880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e8fb03a5fad'
down_revision: Union[str, None] = 'f7534ab9b8a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Student table
    op.alter_column(table_name='student',column_name='typeOfIdentification',new_column_name='type_of_identification',nullable=False)
    op.alter_column(table_name='student',column_name='firstName',new_column_name='first_name',nullable=False)
    op.alter_column(table_name='student',column_name='lastName',new_column_name='last_name',nullable=False)
    op.alter_column(table_name='student',column_name='currentGrade',new_column_name='current_grade',nullable=False)
    # Attendance table
    op.alter_column(table_name='attendance', column_name='attendanceDate',new_column_name='attendance_date', nullable=False)

def downgrade() -> None:
    # Student table
    op.alter_column(table_name='student',column_name='type_of_identification',new_column_name='typeOfIdentification',nullable=False)
    op.alter_column(table_name='student',column_name='first_name',new_column_name='firstName',nullable=False)
    op.alter_column(table_name='student',column_name='last_name',new_column_name='lastName',nullable=False)
    op.alter_column(table_name='student',column_name='current_grade',new_column_name='currentGrade',nullable=False)
    # Attendance table
    op.alter_column(table_name='attendance',column_name='attendance_date',new_column_name='attendanceDate',nullable=False)
