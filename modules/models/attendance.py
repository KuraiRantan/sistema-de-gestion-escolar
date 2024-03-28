from typing import Dict, Union
from datetime import date
from modules.models.definitions import AttendanceStatus
from modules.models.student import Student
from modules.models.classroom import Classroom
from modules.models.subject import Subject

class Attendance(object):
    """Class that represents the Attendance entity."""

    def __init__(self, id: Union[int, None]=None, student: Union[Student, None]=None, subject: Union[Subject, None]=None, classroom: Union[Classroom, None]=None, grade: Union[str, None]=None, attendance_date: Union[date, None]=None, status: Union[AttendanceStatus, None]=None, notes: Union[str, None]=None) -> None:
        """Constructor of the Attendance class.

        Args:
            id (Union[int, None], optional): Unique attendance record identification. Defaults to None.
            student (Union[Student, None], optional): Student record identifier associated with attendance. Defaults to None.
            subject (Union[Subject, None], optional): Subject record identifier associated with attendance. Defaults to None.
            classroom (Union[Classroom, None], optional): Classroom record identifier associated with attendance. Defaults to None.
            grade (Union[str, None], optional): Grade of the student whose attendance is taken. Defaults to None.
            attendance_date (Union[date, None], optional): Date of attendance. Defaults to None.
            status (Union[AttendanceStatus, None], optional): Assistance status. Defaults to None.
            notes (Union[str, None], optional): Additional general considerations regarding the day's attendance. Defaults to None.
        """
        self._id= id
        self._student = student
        self._subject = subject
        self._classroom = classroom
        self._grade = grade
        self._attendance_date = attendance_date
        self._status = status
        self._notes = notes

    @property
    def id(self) -> Union[int, None]:
        """Get the unique identifier of the attendance record."""
        return self._id
    
    @id.setter
    def id(self, value: Union[int, None]) -> None:
        """Set the unique identifier of the attendance record."""
        self._id = value

    @property
    def student(self) -> Union[Student, None]:
        """Get the associated student record."""
        return self._student
    
    @student.setter
    def student(self, value: Union[Student, None]) -> None:
        """Set the associated student record."""
        self._student = value

    @property
    def subject(self) -> Union[Subject, None]:
        """Get the associated subject record."""
        return self._subject
    
    @subject.setter
    def subject(self, value: Union[Subject, None]) -> None:
        """Set the associated subject record."""
        self._subject = value

    @property
    def classroom(self) -> Union[Classroom, None]:
        """Get the associated classroom record."""
        return self._classroom
    
    @classroom.setter
    def classroom(self, value: Union[Classroom, None]) -> None:
        """Set the associated classroom record."""
        self._classroom = value

    @property
    def grade(self) -> Union[str, None]:
        """Get the grade of the student whose attendance is taken."""
        return self._grade
    
    @grade.setter
    def grade(self, value: Union[str, None]) -> None:
        """Set the grade of the student whose attendance is taken."""
        self._grade = value

    @property
    def attendance_date(self) -> Union[date, None]:
        """Get the date of attendance."""
        return self._attendance_date
    
    @attendance_date.setter
    def attendance_date(self, value: Union[date, None]) -> None:
        """Set the date of attendance."""
        self._attendance_date = value

    @property
    def status(self) -> Union[AttendanceStatus, None]:
        """Get the assistance status."""
        return self._status
    
    @status.setter
    def status(self, value: Union[AttendanceStatus, None]) -> None:
        """Set the assistance status."""
        self._status = value

    @property
    def notes(self) -> Union[str, None]:
        """Get the additional general considerations regarding the day's attendance."""
        return self._notes
    
    @notes.setter
    def notes(self, value: Union[str, None]) -> None:
        """Set the additional general considerations regarding the day's attendance."""
        self._notes = value

    def as_dict(self, include_none_data=False) -> Dict[str, Union[int, str, date, Dict, None]]:
        """Represents class attribute information as a data dictionary.

        Args:
            include_none_data (bool, optional): Indicates whether or not to include data with a value of None in the dict. Defaults to False.

        Returns:
            Dict[str, Union[int, str, date, Dict, None]]: A dictionary with the attributes as key and the corresponding value.
        """
        data = {
            'id': self._id,
            'student': None if self._student is None else self._student.as_dict(),
            'subject': None if self._subject is None else self._subject.as_dict(),
            'classroom': None if self._classroom is None else self._classroom.as_dict(),
            'grade': self._grade,
            'attendance_date': self._attendance_date,
            'status': self._status,
            'notes': self._notes
        }
        if not include_none_data:
            data = {key: value for key, value in data.items() if value is not None}

        return data
