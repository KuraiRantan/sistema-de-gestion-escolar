from repository.student_repository import StudentRepository
from factory.student_factory import StudentFactory
from factory.attendance_factory import AttendanceFactory
from repository.attendance_repository import AttendanceRepository

def apply_cors(action):
    def action_decorate(*args, **kwargs):
        response.view = 'generic.json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Origin'] = 'GET,POST,PUT,DELETE,OPTIONS'
        response.headers['Content-Type'] = 'application/json'
        return action(*args, **kwargs)
    return action_decorate

@request.restful()
@apply_cors
def student():
    def POST(*agrs, **vars):
        response.view = 'generic.json'
        try:
            student = StudentFactory.create( **vars)
            repository = StudentRepository(db)
            newStudent = repository.add(student)
            response.status = 201
            return newStudent.as_dict()
        except Exception as e:
            response.status = 500
            return {'error': str(e)}
    def OPTIONS(*args, **vars):
        return locals()
    return locals()

@request.restful()
@apply_cors
def attendance():
     def POST(*args, **vars):
          attendance_repository = AttendanceRepository(db)
          if len(args)>0 and args[0] == 'change-attendance-status':
            id=vars.get('id',None)
            status = vars.get('status', None)
            if id is not None and status is not None:
                attendance = AttendanceFactory.default(id=int(id), status=status)
                attendance_repository.update_status(attendance)
                response.status=200
                return  dict(message='Todo ok')
            response.status=400
            return dict(args=args, vars=vars, message= 'Datos invalidos')
          else:
            return dict(agrs= args, message= 'Ruta INvalida')
     
     def OPTIONS(*agrs, **vars):
         return locals()
     
     return locals()
