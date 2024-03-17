from abc import ABC
class Person(ABC):

    def __init__(self, type_of_identification, identification, first_name, last_name, birthdate, gender, address, email, phone) -> None:
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
         def type_of_identification(self):
              return self._type_of_identification
         
         @type_of_identification.setter
         def type_of_identification(self, value):
              self._type_of_identification = value

         @property
         def identification(self):
              return self._identification
         
         @identification.setter
         def identification(self, value):
              self._identification = value
         
         @property
         def first_name(self):
              return self._first_name
         
         @first_name.setter
         def first_name(self, value):
              self._first_name = value

         @property
         def last_name(self):
              return self._last_name
         
         @last_name.setter
         def last_name(self, value):
              self._last_name = value

         @property
         def birthdate(self):
              return self._birthdate
         
         @birthdate.setter
         def birthdate(self, value):
              self._birthdate = value

         @property
         def gender(self):
              return self._gender
         
         @gender.setter
         def gender(self, value):
              self._gender = value

         @property
         def address(self):
              return self._address
         
         @address.setter
         def address(self, value):
              self._address = value

         @property
         def email(self):
              return self._email
         
         @email.setter
         def email(self, value):
              self._email = value

         @property
         def phone(self):
              return self._phone
         
         @phone.setter
         def phone(self, value):
              self._phone = value

         