from utils.validate_fields import fields_are_valid, validate_data_types
from models.student import Student
from models.definitions import Gender, TypeOfIdentifications

class StudentFactory(object):
    TYPES = {
            'id': int,
            'type_of_identification': [t.value for t in TypeOfIdentifications],
            'identification': str,
            'first_name': str,
            'last_name': str,
            'birthdate': str,
            'gender': [g.value for g in Gender],
            'address': str,
            'email': str,
            'phone': str,
            'current_grade': str
    }
    ACTIONS= {
        'create': [
            'type_of_identification',
            'identification',
            'first_name',
            'last_name',
            'birthdate',
            'gender',
            'current_grade'
        ],
        'update': [
            'id',
            'type_of_identification',
            'identification',
            'first_name',
            'last_name',
            'birthdate',
            'gender',
            'current_grade'
        ],
        'delete': [
            'id'
        ],
        'list': [
            'id',
            'type_of_identification',
            'identification',
            'first_name',
            'last_name',
            'birthdate',
            'gender',
            'current_grade'
        ]
    }

    @staticmethod
    def create(**data:dict):
        if fields_are_valid(StudentFactory.ACTIONS['create'], data):
            if validate_data_types(StudentFactory.TYPES, data):
                return Student(
                    type_of_identification=data.get('type_of_identification'),
                    identification=data.get('identification'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    birthdate=data.get('birthdate'),
                    gender=data.get('gender'),
                    address=data.get('address', None),
                    email=data.get('email', None),
                    phone=data.get('phone', None),
                    current_grade=data.get('current_grade')
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    @staticmethod
    def update(**data:dict):
        if fields_are_valid(StudentFactory.ACTIONS['update'], data):
            if validate_data_types(StudentFactory.TYPES, data):
                return Student(
                    id=data.get('id'),
                    type_of_identification=data.get('type_of_identification', None),
                    identification=data.get('identification', None),
                    first_name=data.get('first_name', None),
                    last_name=data.get('last_name', None),
                    birthdate=data.get('birthdate', None),
                    gender=data.get('gender', None),
                    address=data.get('address', None),
                    email=data.get('email', None),
                    phone=data.get('phone', None),
                    current_grade=data.get('current_grade', None)
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing,')

    @staticmethod
    def delete(**data):
        if fields_are_valid(StudentFactory.ACTIONS['delete'], data):
            if validate_data_types(StudentFactory.TYPES, data):
                return Student(
                    id=data.get('id')
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    def list(**data):
        if fields_are_valid(StudentFactory.ACTIONS['list'], data):
            if validate_data_types(StudentFactory.TYPES, data):
                return Student(
                    id=data.get('id'),
                    type_of_identification=data.get('type_of_identification'),
                    identification=data.get('identification'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    birthdate=data.get('birthdate'),
                    gender=data.get('gender'),
                    address=data.get('address', None),
                    email=data.get('email', None),
                    phone=data.get('phone', None),
                    current_grade=data.get('current_grade')
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    def default(**data):
        if validate_data_types(StudentFactory.TYPES, data):
            return Student(
                id=data.get('id', None),
                type_of_identification=data.get('type_of_identification', None),
                identification=data.get('identification', None),
                first_name=data.get('first_name', None),
                last_name=data.get('last_name', None),
                birthdate=data.get('birthdate', None),
                gender=data.get('gender', None),
                address=data.get('address', None),
                email=data.get('email', None),
                phone=data.get('phone', None),
                current_grade=data.get('current_grade', None)
            )
        raise TypeError('Types of data is not valid.')
