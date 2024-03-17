from utils.validate_fields import fields_are_valid, validate_data_types
from modules.models.subject import Subject

class SubjectFactory(object):
    TYPES = {
            'id': int,
            'name': str,
            'description': str
    }
    ACTIONS= {
        'create': [
            'name',
        ],
        'update': [
            'id',
            'name',
        ],
        'delete': [
            'id'
        ],
        'list': [
            'id',
            'name',
        ]
    }

    @staticmethod
    def create(**data:dict):
        if fields_are_valid(SubjectFactory.ACTIONS['create'], data):
            if validate_data_types(SubjectFactory.TYPES, data):
                return Subject(
                    name=data.get('name'),
                    description=data.get('description', None),
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    @staticmethod
    def update(**data:dict):
        if fields_are_valid(SubjectFactory.ACTIONS['update'], data):
            if validate_data_types(SubjectFactory.TYPES, data):
                return Subject(
                    id=data.get('id'),
                    name=data.get('name'),
                    description=data.get('description', None),
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing,')

    @staticmethod
    def delete(**data):
        if fields_are_valid(SubjectFactory.ACTIONS['delete'], data):
            if validate_data_types(SubjectFactory.TYPES, data):
                return Subject(
                    id=data.get('id')
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    def list(**data):
        if fields_are_valid(SubjectFactory.ACTIONS['list'], data):
            if validate_data_types(SubjectFactory.TYPES, data):
                return Subject(
                    id=data.get('id'),
                    name=data.get('name'),
                    description=data.get('description', None),
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    def default(**data):
        if validate_data_types(SubjectFactory.TYPES, data):
            return Subject(
                id=data.get('id', None),
                name=data.get('name', None),
                description=data.get('description', None),
            )
        raise TypeError('Types of data is not valid.')
