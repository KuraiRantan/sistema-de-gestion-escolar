from datetime import date
from modules.utils.validate_fields import fields_are_valid, validate_data_types
from modules.models.student import Student
from modules.models.definitions import Gender, TypeOfIdentifications

class StudentFactory(object):
    """Factory to create student instances.

    This class provides methods to create instances of different types of students depending on the case that is required.
    """
    # Define the expected data types for each key in the data dictionary.
    TYPES = {
            'id': int,
            'type_of_identification': [t.value for t in TypeOfIdentifications],
            'identification': str,
            'first_name': str,
            'last_name': str,
            'birthdate': date,
            'gender': [g.value for g in Gender],
            'address': str,
            'email': str,
            'phone': str,
            'current_grade': str
    }
    # Defines the actions and required fields for each action.
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
    def create(**data:dict) -> Student:
        """Static method that validates the attributes necessary for the creation of new students, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the student instance.
                Required:
                    - type_of_identification (str): TypeOfIdentification
                    - identification (str)
                    - first_name (str)
                    - last_name (str)
                    - birthdate (date)
                    - gender (str): Gender
                    - current_grade (str)

                Optional:
                    - address (str)
                    - email (str)
                    - phone (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Student: Instance generated from the data provided to the method.
        """
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
    def update(**data:dict) -> Student:
        """Static method that validates the attributes necessary for updating students, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the student instance.
                Required:
                    - id (int)
                    - type_of_identification (str): TypeOfIdentification
                    - identification (str)
                    - first_name (str)
                    - last_name (str)
                    - birthdate (date)
                    - gender (str): Gender
                    - current_grade (str)

                Optional:
                    - address (str)
                    - email (str)
                    - phone (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Student: Instance generated from the data provided to the method.
        """
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
    def delete(**data) -> Student:
        """Static method that validates the attributes necessary for the elimination of students, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the student instance.
                Required:
                    - id (int)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Student: Instance generated from the data provided to the method.
        """
        if fields_are_valid(StudentFactory.ACTIONS['delete'], data):
            if validate_data_types(StudentFactory.TYPES, data):
                return Student(
                    id=data.get('id')
                )
            else:
                raise TypeError('Types of data is not valid.')
        else:
            raise ValueError('Required fields are missing.')

    @staticmethod
    def list(**data: dict) -> Student:
        """Static method that validates the attributes necessary to list students, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the student instance.
                Required:
                    - id (int)
                    - type_of_identification (str): TypeOfIdentification
                    - identification (str)
                    - first_name (str)
                    - last_name (str)
                    - birthdate (date)
                    - gender (str): Gender
                    - current_grade (str)

                Optional:
                    - address (str)
                    - email (str)
                    - phone (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.
            ValueError: Error caused by missing attributes for the operation in question.

        Returns:
            Student: Instance generated from the data provided to the method.
        """
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
                raise TypeError('Types of data is not valid.', data)
        else:
            raise ValueError('Required fields are missing.')

    @staticmethod
    def default(**data: dict) -> Student:
        """Static method that receives the attributes you want in case the other methods don't meet your needs, returning an instance ready to be used.

        Args:
            **data (dict): Dictionary containing data to generate the student instance.
                Optional:
                    - id (int)
                    - type_of_identification (str): TypeOfIdentification
                    - identification (str)
                    - first_name (str)
                    - last_name (str)
                    - birthdate (date)
                    - gender (str): Gender
                    - current_grade (str)
                    - address (str)
                    - email (str)
                    - phone (str)

        Raises:
            TypeError: Error produced by sending an attribute with a data type different from the one defined.

        Returns:
            Student: Instance generated from the data provided to the method.
        """
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
