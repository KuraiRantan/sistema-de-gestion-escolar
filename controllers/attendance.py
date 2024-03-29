from modules.renderer.attendance_renderer import AttendanceRenderer
from modules.repository.attendance_repository import AttendanceRepository
from modules.repository.student_repository import StudentRepository
from modules.repository.classroom_repository import ClassroomRepository
from modules.repository.subject_repository import SubjectRepository

def fill():
    # Create instances of the repositories to use.
    student_repository = StudentRepository(db)
    classroom_repository = ClassroomRepository(db)
    subject_repository = SubjectRepository(db)
    attendance_repository = AttendanceRepository(db)

    # Consult all grades, classrooms and subjects.
    grades = student_repository.get_grades()
    classrooms = classroom_repository.get_all()
    subjects = subject_repository.get_all()
    
    # Gets the query values ​​sent by the post method or none if they have not been sent.
    classroom_var = request.post_vars.get('classroom', None)
    subject_var = request.post_vars.get('subject', None)
    grade_var = request.post_vars.get('grade', None)

    # Verify whether the post method was sent or not by validating the variables that were entered. 
    # If yes, the attendance table is built, if not, the form is built to send the query data using the post method.
    element = None
    if classroom_var is None or subject_var is None or grade_var is None:
        element = AttendanceRenderer.form_request_attendance(classrooms=classrooms, subjects=subjects, grades=grades)
    else:
        students = student_repository.get_all_by_grade(grade_var)
        
        attendance_repository.generate_attendances(
            students,
            int(subject_var),
            int(classroom_var),
            grade_var
        )

        students_attendances = attendance_repository.get_list_attendance(
            int(subject_var),
            int(classroom_var),
            grade_var
        )
        
        classroom_name = next((row.name for row in classrooms if row.id == int(classroom_var)), None)
        subject_name = next((row.name for row in subjects if row.id == int(subject_var)), None)

        element = DIV(AttendanceRenderer.table_attendance(
            attendances=students_attendances,
            classroom=classroom_name,
            subject=subject_name,
            grade=grade_var
        ), AttendanceRenderer.btn_back_to_form_request_attendance(URL('attendance', 'fill')))
    return element
