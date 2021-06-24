from . import db,login
from flask_login import UserMixin, current_user
from datetime import datetime
from functools import wraps

class Admin(db.Model,UserMixin):
    admin_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    admin_pwd = db.Column(db.String(20))
    admin_name = db.Column(db.String(30))
    admin_role = db.Column(db.String(64), default='admin')
    
    def __repr__(self):
        return '<User {}>'.format(self.admin_name)

@login.user_loader
def load_user(id):
    user = Admin.query.filter_by(admin_id=id).first()
    return user


class Student(db.Model,UserMixin):
    student_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    student_name = db.Column(db.String(30))
    student_pwd = db.Column(db.String(20))
    student_email = db.Column(db.String(30))
    student_role = db.Column(db.String(64), default='student')
    student_modify_date = db.Column(db.DateTime)

class Lecturer(db.Model,UserMixin):
    lect_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    lect_name = db.Column(db.String(30))
    lect_pwd = db.Column(db.String(20))
    lect_email = db.Column(db.String(30))
    lect_role = db.Column(db.String(64), default='lecturer')
    lecturer_modify_date = db.Column(db.DateTime)

def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                # Redirect the user to an unauthorized notice!
                return "You are not authorized to access this page"
            return f(*args, **kwargs)
        return wrapped
    return wrapper