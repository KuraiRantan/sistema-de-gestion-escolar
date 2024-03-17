from modules.renderer.attendance_renderer import AttendanceRenderer
from repository.attendance_repository import AttendanceRepository
from repository.student_repository import StudentRepository
from repository.classroom_repository import ClassroomRepository
from repository.subject_repository import SubjectRepository

def fill():
    student_repository = StudentRepository(db)
    classroom_repository = ClassroomRepository(db)
    subject_repository = SubjectRepository(db)
    attendance_repository = AttendanceRepository(db)

    grades = student_repository.get_grades()
    classrooms = classroom_repository.get_all()
    subjects = subject_repository.get_all()
    

    classroom_var = request.post_vars.get('classroom', None)
    subject_var = request.post_vars.get('subject', None)
    grade_var = request.post_vars.get('grade', None)

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
            students_attendances=students_attendances,
            classroom=classroom_name,
            subject=subject_name,
            grade=grade_var
        ), AttendanceRenderer.btn_back_to_form_request_attendance(URL('attendance', 'fill')))
    return element
