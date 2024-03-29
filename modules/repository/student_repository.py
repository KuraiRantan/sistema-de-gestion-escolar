from typing import Union, List
from gluon.dal import DAL
from modules.models.student import Student
from modules.factory.student_factory import StudentFactory
from modules.models.definitions import Gender, TypeOfIdentifications

class StudentRepository(object):
    """Class that provides methods to interact with the database, specifically with the Student entity."""

    def __init__(self, db: DAL) -> None:
        """Constructor of the StudentRepository class.

        Args:
            db (DAL): The database connection instance.
        """
        self._db = db;
        self._student_table = db.student

    def add(self, student: Student) -> Student:
        """Insert a new student into the database.

        Args:
            student (Student): The instance that contains the new student information.

        Raises:
            Exception: Error trying to perform the operation.

        Returns:
            Student: The instance that contains the information for the new student added.
        """
        try:
            id = self._student_table.insert(**student.as_dict())
            student.id = id
            return student
        except Exception as e:
            raise Exception('Error adding student.', e)
    
    def update(self, student: Student) -> Union[Student, None]:
        """Update information for an existing student.

        Args:
            student (Student): The instance that contains the student information.

        Raises:
            Exception: Error trying to perform the operation.

        Returns:
            Student | None: The instance containing the updated student information or None if the student does not exist.
        """
        try:
            student_exist = self._db(self._student_table.id == student.id).select().first()
            if(student_exist):
                student_exist.update(**student.as_dict())
                return student
            else:
                return None
        except Exception as e:
            raise Exception('Error updating student.', e)
    
    def get_grades(self) -> List[str]:
        """List of existing degrees (without repeating).

        Raises:
            Exception: Error trying to perform the operation.

        Returns:
            List[str]: List of degrees.
        """
        try:
            grades = self._db(self._student_table.id>0).select(self._student_table.current_grade, distinct=True)
            return grades
        except Exception as e:
            raise Exception('Error fetching the grades.', e)
        
    def get_all_by_grade(self, grade: str) -> List[Student]:
        """Get all students by grade.

        Args:
            grade (str): Grade a of students to look for.

        Raises:
            Exception: Error trying to perform the operation.

        Returns:
            List[Student]: List of students by grade.
        """
        try:
            students = self._db(self._student_table.current_grade == grade).select()
            return [StudentFactory.list(**student.as_dict()) for student in students]
        except Exception as e:
            raise Exception('Failed to retrieve the student filtered by grade.', e)
