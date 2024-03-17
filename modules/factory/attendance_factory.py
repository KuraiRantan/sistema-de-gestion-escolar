from utils.validate_fields import fields_are_valid, validate_data_types
from modules.models.attendance import Attendance
from modules.models.definitions import AttendanceStatus

class AttendanceFactory(object):
    TYPES = {
            'id': int,
            'student': int,
            'subject': int,
            'classroom': int,
            'grade': str,
            'status': [s.value for s in AttendanceStatus],
            'attendance_date': str,
            'notes': str,
    }
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
    def create(**data:dict):
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
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    @staticmethod
    def update(**data:dict):
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
    def delete(**data):
        if fields_are_valid(AttendanceFactory.ACTIONS['delete'], data):
            if validate_data_types(AttendanceFactory.TYPES, data):
                return Attendance(
                    id=data.get('id')
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    def list(**data):
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

    def default(**data):
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
