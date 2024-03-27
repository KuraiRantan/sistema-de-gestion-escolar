from typing import Dict, Union

class Subject(object):
    """Class that represents the Subject entity."""

    def __init__(self, id: Union[int, None]=None, name: Union[str, None]=None, description: Union[str, None]=None) -> None:
        """Constructor of the Subject class.

        Args:
            id (Union[int, None], optional): Unique subject record identifier. Defaults to None.
            name (Union[str, None], optional): The name of the subject. Defaults to None.
            description (Union[str, None], optional): The description of the subject. Defaults to None.
        """
        self._id = id
        self._name = name
        self._description = description
    
    @property
    def id(self) -> Union[int, None]:
        """Get the unique identifier of the subject record."""
        return self._id

    @id.setter
    def id(self, value: Union[int, None]) -> None:
        """Set the unique identifier of the subject record."""
        self._id = value

    @property
    def name(self) -> Union[str, None]:
        """Get the name of the subject."""
        return self._name

    @name.setter
    def name(self, value: Union[str, None]) -> None:
        """Set the name of the subject."""
        self._name = value

    @property
    def description(self) -> Union[str, None]:
        """Get the description of the subject."""
        return self._description
    
    @description.setter
    def description(self, value: Union[str, None]) -> None:
        """Set the description of the subject."""
        self._description = value

    def as_dict(self, include_none_data=False) -> Dict[str, Union[int, str, None]]:
        """Represents class attribute information as a data dictionary.

        Args:
            include_none_data (bool, optional): Indicates whether or not to include data with a value of None in the dict. Defaults to False.

        Returns:
            Dict[str, Union[int, str, None]]: A dictionary with the attributes as key and the corresponding value.
        """
        data = {
            'id': self._id,
            'name': self._name,
            'description': self._description
        }
        if not include_none_data:
            data = {key: value for key, value in data.items() if value is not None}

        return data