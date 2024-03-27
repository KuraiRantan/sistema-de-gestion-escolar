from typing import Dict, Union
from datetime import date
from modules.models.person import Person
from modules.models.definitions import Gender, TypeOfIdentifications

class Student(Person):
    """Class that represents the Student entity.

    Args:
        Person (Person): Abstract class Person
    """

    def __init__(self,id: Union[int, None]=None, type_of_identification: Union[TypeOfIdentifications, None]=None, identification: Union[str, None]=None, first_name: Union[str, None]=None, last_name: Union[str, None]=None, birthdate: Union[date, None]=None, gender: Union[Gender, None]=None, address: Union[str, None]=None, email: Union[str, None]=None, phone: Union[str, None]=None, current_grade: Union[str, None]=None) -> None:
        """Constructor of the Student class.

        Args:
            id (Union[int, None], optional): Unique student record identifier. Defaults to None.
            type_of_identification (Union[TypeOfIdentifications, None], optional): The type of identification of the student. Defaults to None
            identification (Union[str, None], optional): The identification number of the student. Defaults to None
            first_name (Union[str, None], optional): The first name(s) of the student. Defaults to None
            last_name (Union[str, None], optional): The last name(s) of the student. Defaults to None
            birthdate (Union[date, None], optional): The birthdate of the student. Defaults to None
            gender (Union[Gender, None], optional): The gender of the student. Defaults to None
            address (Union[str, None], optional): The residential address of the student. Defaults to None
            email (Union[str, None], optional): The contact email of the student. Defaults to None
            phone (Union[str, None], optional): The telephone contact of the student. Defaults to None
            current_grade (Union[str, None], optional): The grade the student is in. Defaults to None
        
        Raises:
            ValueError: Error if the gender passed to the constructor is not defined in the Gender enum.
            ValueError: Error if the type of identification passed to the constructor is not defined in the TypeOfIdentification enum.
        """
        # Validar y convertir el género a enum
        if gender:
            try:
                gender = Gender(gender)
            except ValueError:
                raise ValueError("Value for gender invalid.")
        else:
            gender = None

        if type_of_identification:
            try:
                type_of_identification = TypeOfIdentifications(type_of_identification)
            except ValueError:
                raise ValueError("Value for type of identification invalid.")
        else:
            type_of_identification = None
        
        super().__init__(type_of_identification, identification, first_name, last_name, birthdate, gender, address, email, phone)
        self._id = id
        self._current_grade = current_grade

    @property
    def id(self) -> Union[int, None]:
        """Get the unique identifier of the student record."""
        return self._id
    
    @id.setter
    def id(self, value: Union[int, None]) -> None:
        """Set the unique identifier of the student record."""
        self._id = value

    @property
    def current_grade(self) -> Union[str, None]:
        """Get the grade the student is in."""
        return self._current_grade
    
    @current_grade.setter
    def current_grade(self, value: Union[str, None]) -> None:
        """Set the grade the student is in."""
        self._current_grade = value

    def as_dict(self, include_none_data: bool=False) -> Dict[str, Union[str, None, int, date]]:
        """Represents class attribute information as a data dictionary.

        Args:
            include_none_data (bool, optional): Indicates whether or not to include data with a value of None in the dict. Defaults to False.

        Returns:
            Dict[str, Union[str, None, int, date]]: A dictionary with the attributes as key and the corresponding value.
        """
        data = {
            'id': self._id,
            'type_of_identification': None if self._type_of_identification is None else self._type_of_identification.value,
            'identification': self._identification,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'birthdate': self._birthdate,
            'gender': None if self._gender is None else self._gender.value,
            'address': self._address,
            'email': self._email,
            'phone': self._phone,
            'current_grade': self._current_grade,
        }

        if not include_none_data:
            data = {key: value for key, value in data.items() if value is not None}

        return data