from typing import Dict, Union

class Classroom(object):
    """Class that represents the Classroom entity"""

    def __init__(self, id: Union[int, None]=None, name: Union[str, None]=None, capacity: Union[int, None]=None, ubication: Union[str, None]=None) -> None:
        """Constructor of the Classroom class.

        Args:
            id (Union[int, None], optional): Unique classroom record identifier. Defaults to None.
            name (Union[str, None], optional): The name of the classroom. Defaults to None.
            capacity (Union[int, None], optional): The maximum capacity of students in the classroom. Defaults to None.
            ubication (Union[str, None], optional): The location of the classroom within the institution.. Defaults to None.
        """
        self._id = id
        self._name = name
        self._capacity = capacity
        self._ubication = ubication

    @property
    def id(self) -> Union[int, None]:
        """Get the unique identifier of the classroom record."""
        return self._id
    
    @id.setter
    def id(self, value: Union[int, None]) -> None:
        """Set the unique identifier of the classroom record."""
        self._id = value

    @property
    def name(self) -> Union[str, None]:
        """Get the name of the classroom."""
        return self._name
    
    @name.setter
    def name(self, value: Union[str, None]) -> None:
        """Set the name of the classroom."""
        self._name = value

    @property
    def capacity(self) -> Union[int, None]:
        """Get te capacity of the classroom."""
        return self._capacity
    
    @capacity.setter
    def capacity(self, value: Union[int, None]) -> None:
        """Set the capacity of the classroom."""
        self._capacity = value

    @property
    def ubication(self) -> Union[str, None]:
        """Get the ubication of the classroom."""
        return self._ubication
    
    @ubication.setter
    def ubication(self, value: Union[str, None]) -> None:
        """Set the ubication of the classroom"""
        self._ubication = value

    def as_dict(self, include_none_data=False) -> Dict[str, Union[str,int, None]]:
        """Represents class attribute information as a data dictionary.

        Args:
            include_none_data (bool, optional): Indicates whether or not to include data with a value of None in the dict. Defaults to False.

        Returns:
            Dict[str, Union[str,int, None]]: A dictionary with the attributes as key and the corresponding value.
        """
        data = {
            'id': self._id,
            'name': self._name,
            'capacity': self._capacity,
            'ubication': self._ubication
        }
        if not include_none_data:
            data = {key: value for key, value in data.items() if value is not None}

        return data