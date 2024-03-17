class Attendance(object):

    def __init__(self, id=None, student=None, subject=None, classroom=None, grade=None, attendance_date=None, status=None, notes=None) -> None:
        self._id= id
        self._student = student
        self._subject = subject
        self._classroom = classroom
        self._grade = grade
        self._attendance_date = attendance_date
        self._status = status
        self._notes = notes

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def student(self):
        return self._student
    
    @student.setter
    def student(self, value):
        self._student = value

    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def classroom(self):
        return self._classroom
    
    @classroom.setter
    def classroom(self, value):
        self._classroom = value

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, value):
        self._grade = value

    @property
    def attendance_date(self):
        return self._attendance_date
    
    @attendance_date.setter
    def attendance_date(self, value):
        self._attendance_date = value

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        self._status = value

    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def notes(self, value):
        self._notes = value

    def as_dict(self, include_none_data=False):
        data = {
            'id': self._id,
            'student': self._student,
            'subject': self._subject,
            'classroom': self._classroom,
            'grade': self._grade,
            'attendance_date': self._attendance_date,
            'status': self._status,
            'notes': self._notes
        }
        if not include_none_data:
            data = {key: value for key, value in data.items() if value is not None}

        return data