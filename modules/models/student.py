from modules.models.person import Person
from modules.models.definitions import Gender, TypeOfIdentifications

class Student(Person):

    def __init__(self,id=None, type_of_identification=None, identification=None, first_name=None, last_name=None, birthdate=None, gender=None, address=None, email=None, phone=None, current_grade=None) -> None:
        # Validar y convertir el género a enum
        if gender:
            try:
                gender = Gender(gender)
            except ValueError:
                raise ValueError("Valor de género no válido")
        else:
            gender = None

        if type_of_identification:
            try:
                type_of_identification = TypeOfIdentifications(type_of_identification)
            except ValueError:
                raise ValueError("Valor de tipo de identificacion no válido")
        else:
            type_of_identification = None
        
        super().__init__(type_of_identification, identification, first_name, last_name, birthdate, gender, address, email, phone)
        self._id = id
        self._current_grade = current_grade

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def current_grade(self):
        return self._current_grade
    
    @current_grade.setter
    def current_grade(self, value):
        self._current_grade = value

    def as_dict(self, include_none_data=False):
        data = {
            'id': self._id,
            'type_of_identification': self._type_of_identification.value,
            'identification': self._identification,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'birthdate': self._birthdate,
            'gender': self._gender.value,
            'address': self._address,
            'email': self._email,
            'phone': self._phone,
            'current_grade': self._current_grade
        }

        if not include_none_data:
            data = {key: value for key, value in data.items() if value is not None}

        return data
