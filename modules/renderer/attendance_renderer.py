from typing import List
from gluon import URL
from gluon.html import DIV, FORM, SELECT, OPTION, TABLE, TR, TD, TH, LABEL, INPUT, SPAN, H2, SCRIPT, A, BUTTON
from modules.models.classroom import Classroom
from modules.models.subject import Subject
from modules.models.attendance import Attendance
from modules.models.student import Student

class AttendanceRenderer(object):
    """Class that provides methods to render attendance-related views."""
         
    @staticmethod    
    def form_request_attendance( subjects: List[Subject], classrooms: List[Classroom], grades: List[str]) -> DIV:
        """Render a form to request attendance.

        Args:
            subjects (List[Subject]): List of subjects.
            classrooms (List[Classroom]): List of classrooms.
            grades (List[str]): List of grades.

        Returns:
            DIV: Rendered HTML form.
        """
        form = FORM(
            LABEL('Materia:'),
            SELECT(
                *[OPTION(subject.name, _value=subject.id) for subject in subjects],
                _name="subject",
                _id='subject'
            ),
            LABEL('Salón:'),
            SELECT(
                *[OPTION(classroom.name, _value=classroom.id) for classroom in classrooms],
                _name="classroom",
                _id='classroom'
            ),
            LABEL('Grado:'),
            SELECT(
                *[OPTION(g['current_grade'], _value=g['current_grade']) for g in grades],
                _name="grade",
                _id='grade'
            ),
            INPUT(_type='submit', _value="GENERAR ASISTENCIA") if len(subjects)>0 and len(classrooms)>0 and len(grades)>0 else DIV(
                    SPAN('No hay información para salón, materia o grado.')
                ),
            _method='POST'
        )

        return DIV(form, AttendanceRenderer.btn_back_to_form_request_attendance(URL('SGE','default', 'index')))

    @staticmethod
    def table_attendance( attendances: List[Attendance], subject: str, classroom: str, grade: str) -> DIV:
        """Render a table for attendance.

        Args:
            attendances (List[Attendance]): List of attendance instances.
            subject (str): Subject name.
            classroom (str): Classroom name.
            grade (str): Grade name.

        Returns:
            DIV: Rendered HTML table.
        """
        if len(attendances)==0:
            return TABLE(
                TR(TD('No hay estudiantes para listar.'), TD(str(attendances)))
            )
        list_of_td = [[attendance.student.first_name, attendance.student.last_name, attendance.student.gender.value, AttendanceRenderer._generate_radios(attendance)] for attendance in attendances]
        attendance_table = TABLE(
            TR(TH('Nombre(s)'), TH('Apellido(s)'), TH('Género'), TH('Acciones')),
            *[TR(*rows) for rows in list_of_td]
        )
        title = H2(SPAN(f'{subject} - '),SPAN(f'{classroom} - '),SPAN(f'{grade} - '), SPAN(attendances[0].attendance_date))
        script_attendance = SCRIPT(_src=URL('static', 'js/attendance.js'), _type="text/javascript")
        return DIV(title, attendance_table, script_attendance)
    
    @staticmethod
    def btn_back_to_form_request_attendance(href: URL) -> DIV:
        """Render a back button to the attendance request form.

        Args:
            href (URL): URL to navigate back to.

        Returns:
            DIV: Rendered HTML link.
        """
        btn_back = BUTTON('Atrás')
        link = A(btn_back, _href=href)
        return DIV(link)

    @staticmethod
    def _generate_radios(attendance: Attendance) -> FORM:
        """Generate radio buttons for attendance status.

        Args:
            attendance (Attendance): Attendance instance.

        Returns:
            FORM: Rendered HTML form.
        """
        id_hidden = INPUT(_type="hidden", _value=attendance.id, _id="id-attendance")
        div_present = DIV(
            LABEL('Presente',_for="present"),
            INPUT(
                _id="present",
                _name="status",
                _type="radio",
                _value="Present",
                value=attendance.status,
                _onchange="handleChangeAttendanceStatus(event)",
                **{'_data-unknow': ('False' if attendance.status!= 'Unknow' and attendance.status != 'Present' else 'True')}),
        )
        div_absent = DIV(
                LABEL('Ausente',_for="absent"),
                INPUT(
                    _id="absent",
                    _name="status",
                      _type="radio",
                      _value="Absent",
                      value=attendance.status,
                      _onchange="handleChangeAttendanceStatus(event)",
                      **{'_data-unknow': ('False' if attendance.status!= 'Unknow' and attendance.status!='Absent' else 'True')}),
            )
        div_late = DIV(
                LABEL('Tarde',_for="late"),
                INPUT(
                    _id="late",
                    _name="status",
                    _type="radio",
                    _value='Late',
                    value=attendance.status,
                    _onchange="handleChangeAttendanceStatus(event)",
                    **{'_data-unknow': ('False' if attendance.status!= 'Unknow' and attendance.status!='Late' else 'True')})
            
            )
        return FORM(id_hidden, div_present, div_absent, div_late)
