def validate_form(form):
    if not form.vars.name:
        form.errors.name = 'The field name is empty.'

def manage():
    grid = SQLFORM.grid(
        db.subject, 
        create=True, 
        editable=True, 
        deletable=True, 
        user_signature=False, # Disable signing so you can perform CRUD actions without logging in. NOT RECOMMENDED.
        orderby=~db.subject.name, # ordered from z to a
        onvalidation= lambda form: validate_form(form)
    )
    return locals()
