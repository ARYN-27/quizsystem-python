from flask_login import UserMixin
from . import db

class Admin(UserMixin, db.Model):
    admin_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    admin_pwd = db.Column(db.String(30))
    admin_name = db.Column(db.String(20))
    role = db.Column(db.String(64), default='admin')

class Lecturer(UserMixin, db.Model):
    lect_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    lect_pwd = db.Column(db.String(20))
    lect_name = db.Column(db.String(50))
    lect_email = db.Column(db.String(20))
    lecturer_modify_date = db.Column(db.TIMESTAMP)
    role = db.Column(db.String(64), default='lecturer')
    admin_id = db.Column(db.Integer(), db.ForeignKey('Admin.admin_id', ondelete='CASCADE'))
 
class Student(UserMixin, db.Model):
    student_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    student_pwd = db.Column(db.String(20))
    student_name = db.Column(db.String(50))
    student_email = db.Column(db.String(20))
    student_modify_date = db.Column(db.TIMESTAMP)
    role = db.Column(db.String(64), default='student')
    admin_id = db.Column(db.Integer(), db.ForeignKey('Admin.admin_id', ondelete='CASCADE')) 
    