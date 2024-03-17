from factory.attendance_factory import AttendanceFactory
from datetime import datetime

class AttendanceRepository(object):

    def __init__(self, db) -> None:
        self._db =db
        self._attendance_table = db.attendance
        self._student_table = db.student

    def add(self, attendance):
        try:
            id = self._attendance_table.insert(**attendance.as_dict())
            attendance = self._db(self._attendance_table.id == id).select().first()
            return attendance
        except Exception as e:
            raise Exception('Error adding attendance.', e)
        
    def generate_attendances(self, students, subject_id, classroom_id, grade):
        try:
            for student in students:
                existing_attendance = self._db(
                    (self._attendance_table.student==student['id']) &
                    (self._attendance_table.subject==subject_id) &
                    (self._attendance_table.classroom == classroom_id) &
                    (self._student_table.current_grade == grade) &
                    (self._attendance_table.attendance_date == datetime.now().date())
                ).select().first()
                if existing_attendance is None:
                    attendance = AttendanceFactory.create(student=student['id'],subject=subject_id, classroom=classroom_id,grade=grade)
                    self._attendance_table.insert(**attendance.as_dict(include_none_data=False))
        except Exception as e:
            raise Exception('The attendance list could not be generated.', e)

    def get_list_attendance(self, subject_id, classroom_id, grade):
        try:
            students_attendances = self._db(
                (self._student_table.id==self._attendance_table.student) &
                (self._attendance_table.subject== subject_id) &
                (self._attendance_table.classroom == classroom_id) &
                (self._student_table.current_grade == grade) &
                (self._attendance_table.attendance_date==datetime.now().date())
            ).select()
            return students_attendances
        except Exception as e:
            raise Exception('An error occurred while obtaining the attendance list.', e)
        
    def update_status(self, attendance):
        try:
            self._db(self._attendance_table.id == attendance.id).update(status=attendance.status)
            
        except Exception as e:
            raise Exception('Error updating attendance status.', e)
