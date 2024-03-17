class Classroom(object):

    def __init__(self, id=None, name=None, capacity=None, ubication=None) -> None:
        self._id = id
        self._name = name
        self._capacity = capacity
        self._ubication = ubication

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
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def ubication(self):
        return self._ubication
    
    @ubication.setter
    def ubication(self, value):
        self._ubication = value

    def as_dict(self):
        return {
            'id': self._id,
            'name': self._name,
            'capacity': self._capacity,
            'ubication': self._ubication
        }
    
    def as_dict(self, include_none_data=False):
        data = {
            'id': self._id,
            'name': self._name,
            'capacity': self._capacity,
            'ubication': self._ubication
        }
        if not include_none_data:
            data = {key: value for key, value in data.items() if value is not None}

        return data