from modules.utils.validate_fields import fields_are_valid, validate_data_types
from modules.models.attendance import Attendance
from modules.models.definitions import AttendanceStatus
from modules.models.student import Student
from modules.models.subject import Subject
from modules.models.classroom import Classroom
from datetime import date

class AttendanceFactory(object):
    """Factory to create Attendance instances.

    This class provides methods to create instances of different types of attendances depending on the case that is required.
    """
    # Define the expected data types for each key in the data dictionary.
    TYPES = {
            'id': int,
            'student': Student,
            'subject': Subject,
            'classroom': Classroom,
            'grade': str,
            'status': [s.value for s in AttendanceStatus],
            'attendance_date': date,
            'notes': str,
    }
    # Defines the actions and required fields for each action.
    ACTIONS= {
        'create': [
            'student',
            'subject',
            'classroom',
            'grade'
        ],
        'update': [
            'id',
            'student',
            'subject',
            'classroom',
            'grade',
            'attendance_date',
            'status'
        ],
        'delete': [
            'id'
        ],
        'list': [
            'id',
            'student',
            'subject',
            'classroom',
            'grade',
            'attendance_date',
            'status'
        ]
    }

    @staticmethod
    def create(**data: dict) -> Attendance:
        """Static method that validates the attributes necessary for the creation of new attendance, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the attendance instance.
                Required:
                    - student (Student)
                    - subject (Subject)
                    - classroom (Classroom)
                    - grade (str)
                
                Optional:
                    - status (str): AttendanceStatus
                    - attendance_date (date)
                    - notes (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Attendance: Instance generated from the data provided to the method.
        """
        if fields_are_valid(AttendanceFactory.ACTIONS['create'], data):
            if validate_data_types(AttendanceFactory.TYPES, data):
                return Attendance(
                    student=data.get('student'),
                    subject=data.get('subject'),
                    classroom=data.get('classroom'),
                    grade=data.get('grade'),
                    status=data.get('status', None),
                    attendance_date=data.get('attendance_date', None),
                    notes=data.get('notes', None),
                )
            else:
                raise TypeError('Types of data is not valid.', data)
        else:
            raise ValueError('Required fields are missing.')

    @staticmethod
    def update(**data: dict) -> Attendance:
        """Static method that validates the attributes necessary for updating attendances, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the attendance instance.
                Required:
                    - id (int)
                    - student (Student)
                    - subject (Subject)
                    - classroom (Classroom)
                    - grade (str)
                
                Optional:
                    - status (str): AttendanceStatus
                    - attendance_date (date)
                    - notes (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Attendance: Instance generated from the data provided to the method.
        """
        if fields_are_valid(AttendanceFactory.ACTIONS['update'], data):
            if validate_data_types(AttendanceFactory.TYPES, data):
                return Attendance(
                    id=data.get('id'),
                    student=data.get('student'),
                    subject=data.get('subject'),
                    classroom=data.get('classroom'),
                    grade=data.get('grade'),
                    attendance_date=data.get('attendance_date'),
                    status=data.get('status'),
                    notes=data.get('notes', None)
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing,')

    @staticmethod
    def delete(**data: dict) -> Attendance:
        """Static method that validates the attributes necessary for the elimination of attendances, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the attendance instance.
                Required:
                    - id (int)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Attendance: Instance generated from the data provided to the method.
        """
        if fields_are_valid(AttendanceFactory.ACTIONS['delete'], data):
            if validate_data_types(AttendanceFactory.TYPES, data):
                return Attendance(
                    id=data.get('id')
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    def list(**data: dict) -> Attendance:
        """Static method that validates the attributes necessary to list attendances, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the attendance instance.
                Required:
                    - id (int)
                    - student (Student)
                    - subject (Subject)
                    - classroom (Classroom)
                    - grade (str)
                
                Optional:
                    - status (str): AttendanceStatus
                    - attendance_date (date)
                    - notes (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Attendance: Instance generated from the data provided to the method.
        """
        if fields_are_valid(AttendanceFactory.ACTIONS['list'], data):
            if validate_data_types(AttendanceFactory.TYPES, data):
                return Attendance(
                    id=data.get('id'),
                    student=data.get('student'),
                    subject=data.get('subject'),
                    classroom=data.get('classroom'),
                    grade=data.get('grade'),
                    attendance_date=data.get('attendance_date'),
                    status=data.get('status'),
                    notes=data.get('notes', None)
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    @staticmethod
    def default(**data: dict) -> Attendance:
        """Static method that receives the attributes you want in case the other methods don't meet your needs, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the attendance instance.
                Optional:
                    - id (int)
                    - student (Student)
                    - subject (Subject)
                    - classroom (Classroom)
                    - grade (str)
                    - status (str): AttendanceStatus
                    - attendance_date (date)
                    - notes (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.

        Returns:
            Attendance: Instance generated from the data provided to the method.
        """
        if validate_data_types(AttendanceFactory.TYPES, data):
            return Attendance(
                id=data.get('id', None),
                student=data.get('student', None),
                subject=data.get('subject', None),
                classroom=data.get('classroom', None),
                grade=data.get('grade', None),
                attendance_date=data.get('attendance_date', None),
                status=data.get('status', None),
                notes=data.get('notes', None)
            )
        raise TypeError('Types of data is not valid.')
