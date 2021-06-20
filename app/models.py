from flask_login import UserMixin, current_user
from . import db, login
from functools import wraps

class Admin(UserMixin, db.Model):
    admin_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    admin_pwd = db.Column(db.String(30))
    admin_name = db.Column(db.String(20))
    role = db.Column(db.String(64), default='admin')
    
    def __repr__(self):
        return '<Admin {}>'.format(self.admin_id)

@login.user_loader
def load_user(admin_id):
    user = Admin.query.filter_by(admin_id=admin_id).first()
    return user

class Lecturer(UserMixin, db.Model):
    lect_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    lect_pwd = db.Column(db.String(20))
    lect_name = db.Column(db.String(50))
    lect_email = db.Column(db.String(20))
    lecturer_modify_date = db.Column(db.TIMESTAMP)
    role = db.Column(db.String(64), default='lecturer')
    admin_id = db.Column(db.Integer(), db.ForeignKey('Admin.admin_id', ondelete='CASCADE'))
    
    def __repr__(self):
        return '<Lecturer {}>'.format(self.lect_id)
    
@login.user_loader
def load_user(lect_id):
    user = Admin.query.filter_by(lect_id=lect_id).first()
    return user
 
class Student(UserMixin, db.Model):
    student_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    student_pwd = db.Column(db.String(20))
    student_name = db.Column(db.String(50))
    student_email = db.Column(db.String(20))
    student_modify_date = db.Column(db.TIMESTAMP)
    role = db.Column(db.String(64), default='student')
    admin_id = db.Column(db.Integer(), db.ForeignKey('Admin.admin_id', ondelete='CASCADE')) 

    def __repr__(self):
        return '<Student {}>'.format(self.student_id)

@login.user_loader
def load_user(student_id):
    user = Admin.query.filter_by(student_id=student_id).first()
    return user

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

