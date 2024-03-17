from utils.validate_fields import fields_are_valid, validate_data_types
from modules.models.classroom import Classroom

class ClassroomFactory(object):
    TYPES = {
            'id': int,
            'name': str,
            'capacity': int,
            'ubication': str,
    }
    ACTIONS= {
        'create': [
            'name',
            'capacity',
            'ubication',
        ],
        'update': [
            'id',
            'name',
            'capacity',
            'ubication',
        ],
        'delete': [
            'id'
        ],
        'list': [
            'id',
            'name',
            'capacity',
            'ubication'
        ]
    }

    @staticmethod
    def create(**data:dict):
        if fields_are_valid(ClassroomFactory.ACTIONS['create'], data):
            if validate_data_types(ClassroomFactory.TYPES, data):
                return Classroom(
                    name=data.get('name', None),
                    capacity=data.get('capacity', None),
                    ubication=data.get('ubication', None)
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    @staticmethod
    def update(**data:dict):
        if fields_are_valid(ClassroomFactory.ACTIONS['update'], data):
            if validate_data_types(ClassroomFactory.TYPES, data):
                return Classroom(
                    id=data.get('id'),
                    name=data.get('name', None),
                    capacity=data.get('capacity', None),
                    ubication=data.get('ubication', None)
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing,')

    @staticmethod
    def delete(**data):
        if fields_are_valid(ClassroomFactory.ACTIONS['delete'], data):
            if validate_data_types(ClassroomFactory.TYPES, data):
                return Classroom(
                    id=data.get('id')
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    def list(**data):
        if fields_are_valid(ClassroomFactory.ACTIONS['list'], data):
            if validate_data_types(ClassroomFactory.TYPES, data):
                return Classroom(
                    id=data.get('id'),
                    name=data.get('name', None),
                    capacity=data.get('capacity', None),
                    ubication=data.get('ubication', None)
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    def default(**data):
        if validate_data_types(ClassroomFactory.TYPES, data):
            return Classroom(
                id=data.get('id', None),
                name=data.get('name', None),
                capacity=data.get('capacity', None),
                ubication=data.get('ubication', None)
            )
        raise TypeError('Types of data is not valid.')
