from typing import Callable, Dict
from datetime import datetime
from modules.repository.student_repository import StudentRepository
from modules.factory.student_factory import StudentFactory
from modules.factory.attendance_factory import AttendanceFactory
from modules.repository.attendance_repository import AttendanceRepository

def apply_cors(action: Callable[[], Dict[str, any]]) -> Callable[[tuple, Dict], Dict[str, any]]:
    """Decorator function to apply Cross-Origin Resource Sharing (CORS) headers to the response.

    This decorator adds the necessary headers to allow cross-origin requests from any origin ('*'),
    and specifies the allowed HTTP methods (GET, POST, PUT, DELETE, OPTIONS). Additionally, it sets
    the Content-Type of the response to 'application/json'.

    Args:
        action (function): The original function to be decorated.

    Returns:
        function: The decorated function with CORS headers applied.
    """
    def action_decorate(*args, **kwargs) -> Dict[str, any]:
        """Decorator function to add CORS headers and set Content-Type.

        This inner function sets the necessary CORS headers and Content-Type before executing
        the original function.

        Args:
            *args: Positional arguments to pass to the original function.
            **kwargs: Keyword arguments to pass to the original function.

        Returns:
            Dict[str, function]: The result of the original function.
        """
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
        try:
            if 'birthdate' in vars:
                fecha_str_py = "-".join([f"{int(part):02d}" for part in vars['birthdate'].split("-")])
                fecha_date = datetime.strptime(fecha_str_py, "%Y-%m-%d").date()
                vars['birthdate'] = fecha_date
            student = StudentFactory.create( **vars)
            repository = StudentRepository(db)
            newStudent = repository.add(student)
            response.status = 201
            return dict()
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
        if len(args)>0 and args[0] == 'change-attendance-status': # Validate that the route contains the 'change-attendance-status' argument
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
