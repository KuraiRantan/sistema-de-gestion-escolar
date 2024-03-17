class StudentRepository(object):

    def __init__(self, db) -> None:
        self._db = db;
        self._student_table = db.student;

    def add(self, student):
        try:
            id = self._student_table.insert(**student.as_dict())
            student = self._db(self._student_table.id == id).select().first()
            return student
        except Exception as e:
            raise Exception('Error adding student.', e)
    
    def update(self, student):
        try:
            student = self._db(self._student_table.id == student.id).select().first()
            if(student):
                student.update(**student.as_dict(include_none_data=True))
                return student
            else:
                return None
        except Exception as e:
            raise Exception('Error updating student.', e)
    
    def get_grades(self):
        try:
            grades = self._db(self._student_table.id>0).select(self._student_table.current_grade, distinct=True)
            return grades
        except Exception as e:
            raise Exception('Error fetching the grades.', e)
        
    def get_all_by_grade(self, grade):
        try:
            students = self._db(self._student_table.current_grade == grade).select()
            return students
        except Exception as e:
            raise Exception('Failed to retrieve the student filtered by grade.', e)