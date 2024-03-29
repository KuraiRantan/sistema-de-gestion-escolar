from typing import List
from gluon.dal import DAL
from modules.models.subject import Subject
from modules.factory.subject_factory import SubjectFactory

class SubjectRepository(object):
    """Class that provides methods to interact with the database, specifically with the Subject entity."""

    def __init__(self, db: DAL) -> None:
        """Constructor of the SubjectRepository class.
        
        Args:
            db (DAL): The database connection instance.
        """
        self._db = db
        self._subject_table = db.subject

    def get_all(self) -> List[Subject]:
        """Get all subjects.

        Raises:
            Exception: Error trying to perform the operation.

        Returns:
            list[Subject]: List of all subjects.
        """
        try:
            subjects = self._db(self._subject_table.id > 0).select()
            return [SubjectFactory.list(**subject.as_dict()) for subject in subjects]
        except Exception as e:
            raise Exception('An error occurred while trying to retrieve the subjects.', e)