class SubjectRepository(object):

    def __init__(self, db) -> None:
        self._db = db
        self._subject_table = db.subject

    def get_all(self):
        try:
            subjects = self._db(self._subject_table.id > 0).select()
            return subjects
        except Exception as e:
            raise Exception('An error occurred while trying to retrieve the subjects.', e)