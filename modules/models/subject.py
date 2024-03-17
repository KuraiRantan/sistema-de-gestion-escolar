class Subject(object):

    def __init__(self, id=None, name=None, description=None) -> None:
        self._id = id
        self._name = name
        self._description = description
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value

    def as_dict(self, include_none_data=False):
        data = {
            'id': self._id,
            'name': self._name,
            'description': self._description
        }
        if not include_none_data:
            data = {key: value for key, value in data.items() if value is not None}

        return data