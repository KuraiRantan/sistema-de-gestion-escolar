from gluon import URL
from gluon.html import DIV, FORM, SELECT, OPTION, TABLE, TR, TD, TH, LABEL, INPUT, SPAN, H2, SCRIPT, A, BUTTON

class AttendanceRenderer(object):
         
    @staticmethod    
    def form_request_attendance( subjects, classrooms, grades):
        form = FORM(
            LABEL('Materia:'),
            SELECT(
                *[OPTION(s['name'], _value=s['id']) for s in subjects],
                _name="subject",
                _id='subject'
            ),
            LABEL('Salón:'),
            SELECT(
                *[OPTION(c['name'], _value=c['id']) for c in classrooms],
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
    def table_attendance( students_attendances, subject, classroom, grade):
        if len(students_attendances)==0:
            return TABLE(
                TR(TD('No hay estudiantes para listar.'))
            )
        list_of_td = [[s.student['first_name'], s.student['last_name'], s.student['gender'], AttendanceRenderer._generate_radios(s.attendance)] for s in students_attendances]
        attendance_table = TABLE(
            TR(TH('Nombre(s)'), TH('Apellido(s)'), TH('Género'), TH('Acciones')),
            *[TR(*rows) for rows in list_of_td]
        )
        title = H2(SPAN(f'{subject} - '),SPAN(f'{classroom} - '),SPAN(f'{grade} - '), SPAN(students_attendances[0].attendance['attendance_date']))
        script_attendance = SCRIPT(_src=URL('static', 'js/attendance.js'), _type="text/javascript")
        return DIV(title, attendance_table, script_attendance)
    
    @staticmethod
    def btn_back_to_form_request_attendance(href):
        btn_back = BUTTON('Atrás')
        link = A(btn_back, _href=href)
        return DIV(link)

    @staticmethod
    def _generate_radios(attendance):
        id_hidden = INPUT(_type="hidden", _value=attendance['id'], _id="id-attendance")
        div_present = DIV(
            LABEL('Presente',_for="present"),
            INPUT(
                _id="present",
                _name="status",
                _type="radio",
                _value="Present",
                value=attendance['status'],
                _onchange="handleChangeAttendanceStatus(event)",
                **{'_data-unknow': ('False' if attendance['status']!= 'Unknow' and attendance['status'] != 'Present' else 'True')}),
        )
        div_absent = DIV(
                LABEL('Ausente',_for="absent"),
                INPUT(
                    _id="absent",
                    _name="status",
                      _type="radio",
                      _value="Absent",
                      value=attendance['status'],
                      _onchange="handleChangeAttendanceStatus(event)",
                      **{'_data-unknow': ('False' if attendance['status']!= 'Unknow' and attendance['status']!='Absent' else 'True')}),
            )
        div_late = DIV(
                LABEL('Tarde',_for="late"),
                INPUT(
                    _id="late",
                    _name="status",
                    _type="radio",
                    _value='Late',
                    value=attendance['status'],
                    _onchange="handleChangeAttendanceStatus(event)",
                    **{'_data-unknow': ('False' if attendance['status']!= 'Unknow' and attendance['status']!='Late' else 'True')})
            
            )
        return FORM(id_hidden, div_present, div_absent, div_late)
