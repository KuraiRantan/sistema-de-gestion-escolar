from modules.utils.validate_fields import fields_are_valid, validate_data_types
from modules.models.subject import Subject

class SubjectFactory(object):
    """Factory to create subject instances.

    This class provides methods to create instances of different types of subjects depending on the case that is required.
    """
    # Define the expected data types for each key in the data dictionary.
    TYPES = {
            'id': int,
            'name': str,
            'description': str
    }
    # Defines the actions and required fields for each action.
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
    def create(**data: dict) -> Subject:
        """Static method that validates the attributes necessary for the creation of new subject, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the subject instance.
                Required:
                    - name (str)

                Optional:
                    - description (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Subject: Instance generated from the data provided to the method.
        """
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
    def update(**data: dict) -> Subject:
        """Static method that validates the attributes necessary for updating subjects, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the subject instance.
                Required:
                    - id (int)
                    - name (str)

                Optional:
                    - description (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Subject: Instance generated from the data provided to the method.
        """
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
    def delete(**data: dict) -> Subject:
        """Static method that validates the attributes necessary for the elimination of subjects, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the subject instance.
                Required:
                    - id (int)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Subject: Instance generated from the data provided to the method.
        """
        if fields_are_valid(SubjectFactory.ACTIONS['delete'], data):
            if validate_data_types(SubjectFactory.TYPES, data):
                return Subject(
                    id=data.get('id')
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    @staticmethod
    def list(**data: dict) -> Subject:
        """Static method that validates the attributes necessary to list subjects, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the subject instance.
                Required:
                    - id (int)
                    - name (str)

                Optional:
                    - description (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Subject: Instance generated from the data provided to the method.
        """
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

    @staticmethod
    def default(**data: dict) -> Subject:
        """Static method that receives the attributes you want in case the other methods don't meet your needs, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the subject instance.
                Optional:
                    - id (int)
                    - name (str)
                    - description (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.

        Returns:
            Subject: Instance generated from the data provided to the method.
        """
        if validate_data_types(SubjectFactory.TYPES, data):
            return Subject(
                id=data.get('id', None),
                name=data.get('name', None),
                description=data.get('description', None),
            )
        raise TypeError('Types of data is not valid.')
