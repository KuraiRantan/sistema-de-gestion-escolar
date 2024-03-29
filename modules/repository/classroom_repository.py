from typing import List
from gluon.dal import DAL
from modules.models.classroom import Classroom
from modules.factory.classroom_factory import ClassroomFactory

class ClassroomRepository(object):
    """Class that provides methods to interact with the database, specifically with the Classroom entity."""
    
    def __init__(self, db: DAL) -> None:
        """Constructor of the ClassroomRepository class.

        Args:
            db (DAL): The database connection instance.
        """
        self._db = db
        self._classroom_table = db.classroom

    def get_all(self) -> List[Classroom]:
        """Get all the classrooms.

        Raises:
            Exception: Error trying to perform the operation.

        Returns:
            List[Classroom]: List of all classrooms.
        """
        try:
            classrooms = self._db(self._classroom_table.id > 0).select()
            return [ClassroomFactory.list(**classroom.as_dict()) for classroom in classrooms]
        except Exception as e:
            raise Exception('Classrooms could not be obtained.', e)
