from typing import Union
from abc import ABC
from datetime import date
from modules.models.definitions import TypeOfIdentifications, Gender

class Person(ABC):
    """
    Abstract class that represents the person entity.
    """

    def __init__(self, type_of_identification: Union[TypeOfIdentifications, None], identification: Union[str, None], first_name: Union[str, None], last_name: Union[str, None], birthdate: Union[date, None], gender: Union[Gender, None], address: Union[str, None], email: Union[str, None], phone: Union[str, None]) -> None:
        """Constructor of the Person class.

        Args:
            type_of_identification (Union[TypeOfIdentifications, None]): The type of identification of the person.
            identification (Union[str, None]): The identification number of the person.
            first_name (Union[str, None]): The first name(s) of the person.
            last_name (Union[str, None]): The last name(s) of the person.
            birthdate (Union[date, None]): The birthdate of the person.
            gender (Union[Gender, None]): The gender of the person.
            address (Union[str, None]): The residential address of the person.
            email (Union[str, None]): The contact email of the person.
            phone (Union[str, None]): The telephone contact of the person.
        """
        self._type_of_identification = type_of_identification
        self._identification = identification
        self._first_name = first_name
        self._last_name = last_name
        self._birthdate = birthdate
        self._gender = gender
        self._address = address
        self._email = email
        self._phone = phone

    @property
    def type_of_identification(self) -> Union[TypeOfIdentifications, None]:
        """Get the person's ID type."""
        return self._type_of_identification
         
    @type_of_identification.setter
    def type_of_identification(self, value: Union[TypeOfIdentifications, None]) -> None:
        """Set the person's ID type."""
        self._type_of_identification = value

    @property
    def identification(self) -> Union[str, None]:
        """Get the person's identification number."""
        return self._identification
         
    @identification.setter
    def identification(self, value: Union[str, None]) -> None:
        """Set the person's identification number."""
        self._identification = value
         
    @property
    def first_name(self) -> Union[str, None]:
        """Get the person's first name."""
        return self._first_name
         
    @first_name.setter
    def first_name(self, value: Union[str, None]) -> None:
        """Set the person's first name."""
        self._first_name = value

    @property
    def last_name(self) -> Union[str, None]:
        """Get the person's last name."""
        return self._last_name
         
    @last_name.setter
    def last_name(self, value: Union[str, None]) -> None:
        """Set the person's last name."""
        self._last_name = value

    @property
    def birthdate(self) -> Union[date, None]:
        """Get the person's birthdate."""
        return self._birthdate
        
    @birthdate.setter
    def birthdate(self, value: Union[date,  None]) -> None:
        """Set the person's birthdate."""
        self._birthdate = value

    @property
    def gender(self) -> Union[Gender, None]:
        """Get the person's gender."""
        return self._gender
        
    @gender.setter
    def gender(self, value: Union[Gender, None]) -> None:
        """Set the person's gender."""
        self._gender = value

    @property
    def address(self) -> Union[str, None]:
        """Get the person's address."""
        return self._address
         
    @address.setter
    def address(self, value: Union[str, None]) -> None:
        """Set the person's address."""
        self._address = value

    @property
    def email(self) -> Union[str, None]:
        """Get the person's email."""
        return self._email
         
    @email.setter
    def email(self, value: Union[str, None]) -> None:
        """Set the person's email."""
        self._email = value

    @property
    def phone(self) -> Union[str, None]:
        """Get the person's phone."""
        return self._phone
         
    @phone.setter
    def phone(self, value: Union[str,  None]) -> None:
        """Set the person's phone."""
        self._phone = value