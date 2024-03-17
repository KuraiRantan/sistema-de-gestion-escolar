def create():
    response.view = 'student/create.html'
    response.files.append(URL('static', 'js/sge.bundle.min.js'))
    return dict()
