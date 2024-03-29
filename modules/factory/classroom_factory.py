from modules.utils.validate_fields import fields_are_valid, validate_data_types
from modules.models.classroom import Classroom

class ClassroomFactory(object):
    """Factory to create classroom instances.

    This class provides methods to create instances of different types of classrooms depending on the case that is required.
    """
    # Define the expected data types for each key in the data dictionary.
    TYPES = {
            'id': int,
            'name': str,
            'capacity': int,
            'ubication': str,
    }
    # Defines the actions and required fields for each action.
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
    def create(**data: dict) -> Classroom:
        """Static method that validates the attributes necessary for the creation of new classroom, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the classroom instance.
                Required:
                    - name (str)
                    - capacity (int)
                    - ubication (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Classroom: Instance generated from the data provided to the method.
        """
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
    def update(**data: dict) -> Classroom:
        """Static method that validates the attributes necessary for updating classrooms, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the classroom instance.
                Required:
                    - id (int)
                    - name (str)
                    - capacity (int)
                    - ubication (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Classroom: Instance generated from the data provided to the method.
        """
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
    def delete(**data: dict) -> Classroom:
        """Static method that validates the attributes necessary for the elimination of classrooms, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the classroom instance.
                Required:
                    - id (int)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Classroom: Instance generated from the data provided to the method.
        """
        if fields_are_valid(ClassroomFactory.ACTIONS['delete'], data):
            if validate_data_types(ClassroomFactory.TYPES, data):
                return Classroom(
                    id=data.get('id')
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    @staticmethod
    def list(**data: dict) -> Classroom:
        """Static method that validates the attributes necessary to list classrooms, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the classroom instance.
                Required:
                    - id (int)
                    - name (str)
                    - capacity (int)
                    - ubication (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Classroom: Instance generated from the data provided to the method.
        """
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

    @staticmethod
    def default(**data: dict) -> Classroom:
        """Static method that receives the attributes you want in case the other methods don't meet your needs, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the classroom instance.
                Optional:
                    - id (int)
                    - name (str)
                    - capacity (int)
                    - ubication (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.

        Returns:
            Classroom: Instance generated from the data provided to the method.
        """
        if validate_data_types(ClassroomFactory.TYPES, data):
            return Classroom(
                id=data.get('id', None),
                name=data.get('name', None),
                capacity=data.get('capacity', None),
                ubication=data.get('ubication', None)
            )
        raise TypeError('Types of data is not valid.')
