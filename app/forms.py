from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Admin, Lecturer, Student


class LoginForm(FlaskForm):
    admin_id = StringField('Admin ID', validators=[DataRequired()])
    admin_pwd = StringField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')