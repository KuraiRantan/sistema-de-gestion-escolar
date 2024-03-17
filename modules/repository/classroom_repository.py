class ClassroomRepository(object):

    def __init__(self, db) -> None:
        self._db = db
        self._classroom_table = db.classroom

    def get_all(self):
        try:
            classrooms = self._db(self._classroom_table.id > 0).select()
            return classrooms
        except Exception as e:
            raise Exception('Classrooms could not be obtained.', e)