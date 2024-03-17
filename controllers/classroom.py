def validate_form(form):
    if not form.vars.name:
        form.errors.name = 'The name field is empty.'
    if not form.vars.capacity:
        form.errors.capacity = 'The capacity field is empty or zero.'
    if not form.vars.ubication:
        form.errors.ubication = 'The ubication field is empty.'
    if form.vars.capacity and int(form.vars.capacity) < 0:
        form.errors.capacity = 'The value is less than zero.'

def manage():
    grid = SQLFORM.grid(
        db.classroom, 
        create=True, 
        editable=True, 
        deletable=True, 
        user_signature=False, # Disable signing so you can perform CRUD actions without logging in. NOT RECOMMENDED.
        orderby=db.classroom.name, # ordered from a to z.,
        onvalidation= lambda form: validate_form(form)
    )
    return locals()
