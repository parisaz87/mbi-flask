from functools import wraps
from flask import g, flash, redirect, url_for, request


def requires_login(f, admin=False):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.reporter is None:
            flash(u'You need to be signed in to access that page.', 'warning')
            return redirect(url_for('reporting.login', next=request.path))
        if admin:
            if g.reporter.email not in app.ADMINS:
                flash(u'Only administrators can access that page.', 'error')
        return f(*args, **kwargs)
    return decorated_function
