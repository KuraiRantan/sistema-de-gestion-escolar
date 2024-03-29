from typing import List
from gluon.dal import DAL
from datetime import datetime, timezone, timedelta
from modules.models.attendance import Attendance
from modules.models.student import Student
from modules.factory.attendance_factory import AttendanceFactory
from modules.factory.student_factory import StudentFactory
from modules.factory.subject_factory import SubjectFactory
from modules.factory.classroom_factory import ClassroomFactory

class AttendanceRepository(object):
    """Class that provides methods to interact with the database, specifically with the Attendance entity."""

    def __init__(self, db: DAL) -> None:
        """Constructor of the AttendanceRepository class.

        Args:
            db (DAL): The database connection instance.
        """
        self._db =db
        self._attendance_table = db.attendance
        self._student_table = db.student

    def add(self, attendance: Attendance) -> Attendance:
        """Insert a new attendance into the database.

        Args:
            attendance (Attendance): The instance that contains the new attendance information.

        Raises:
            Exception: Error trying to perform the operation.

        Returns:
            Attendance: The instance that contains the information for the new attendance added.
        """
        try:
            id = self._attendance_table.insert(**attendance.as_dict())
            attendance.id = id
            return attendance
        except Exception as e:
            raise Exception('Error adding attendance.', e)
        
    def generate_attendances(self, students: List[Student], subject_id: int, classroom_id: int, grade: str) -> None:
        """Generate attendance for each student.

        Args:
            students (List[Student]): List of students for whom attendance will be created.
            subject_id (int): Identifier of the subject associated with the assistance.
            classroom_id (int): Identifier of the classroom associated with the assistance.
            grade (str): Degree associated with attendance.

        Raises:
            Exception: Error trying to perform the operation.
        """
        try:
            for student in students:
                existing_attendance = self._db(
                    (self._attendance_table.student==student.id) &
                    (self._attendance_table.subject==subject_id) &
                    (self._attendance_table.classroom == classroom_id) &
                    (self._student_table.current_grade == grade) &
                    (self._attendance_table.attendance_date == (datetime.now(timezone.utc) - timedelta(hours=5)).date())
                ).select().first()
                if existing_attendance is None:
                    self._attendance_table.insert(
                        student=student.id,
                        subject=subject_id,
                        classroom=classroom_id,
                        grade=grade
                    )
        except Exception as e:
            raise Exception('The attendance list could not be generated.', e)

    def get_list_attendance(self, subject_id: int, classroom_id: int, grade: str) -> List[Attendance]:
        """Get all attendance list based on search parameters.

        Args:
            subject_id (int): Identifier of the subject associated with the assistance.
            classroom_id (int): Identifier of the classroom associated with the assistance.
            grade (str): Degree associated with attendance.

        Raises:
            Exception: Error trying to perform the operation.

        Returns:
            List[Attendance]: List of tuples, in the first position of the tuple is the attendance, and in the second position is the associated student.
        """
        try:
            students_attendances_select = self._db(
                (self._student_table.id == self._attendance_table.student) &
                (self._attendance_table.subject == subject_id) &
                (self._attendance_table.classroom == classroom_id) &
                (self._student_table.current_grade == grade) &
                (self._attendance_table.attendance_date == (datetime.now(timezone.utc) - timedelta(hours=5)).date())
            ).select()
            
            attendances = []
            for value in students_attendances_select:
                attendance_dict = value.attendance.as_dict()
                student = StudentFactory.list(**value.student.as_dict())
                subject = SubjectFactory.default(id=subject_id)
                classroom = ClassroomFactory.default(id=subject_id)
                attendance = AttendanceFactory.list(
                    id= attendance_dict.get('id'),
                    student=student,
                    subject=subject,
                    classroom=classroom,
                    grade=attendance_dict.get('grade'),
                    attendance_date=attendance_dict.get('attendance_date'),
                    status=attendance_dict.get('status'),
                    notes=attendance_dict.get('notes')
                )
                attendances.append(attendance)
            return attendances
        except Exception as e:
            raise Exception('An error occurred while obtaining the attendance list.', e)
        
    def update_status(self, attendance: Attendance) -> None:
        """Change attendance status.

        Args:
            attendance (Attendance): The instance that contains the attendance information.

        Raises:
            Exception: Error trying to perform the operation.
        """
        try:
            self._db(self._attendance_table.id == attendance.id).update(status=attendance.status)
            
        except Exception as e:
            raise Exception('Error updating attendance status.', e)
