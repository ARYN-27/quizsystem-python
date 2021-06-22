from . import db
from datetime import datetime

class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    admin_pwd = db.Column(db.String(20))
    admin_name = db.Column(db.String(30))
    admin_role = db.Column(db.String(64), default='admin')

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    student_name = db.Column(db.String(30))
    student_pwd = db.Column(db.String(20))
    student_email = db.Column(db.String(30))
    student_role = db.Column(db.String(64), default='student')
    student_modify_date = db.Column(db.DateTime)

class Lecturer(db.Model):
    lect_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    lect_name = db.Column(db.String(30))
    lect_pwd = db.Column(db.String(20))
    lect_email = db.Column(db.String(30))
    lect_role = db.Column(db.String(64), default='lecturer')
    lecturer_modify_date = db.Column(db.DateTime)

