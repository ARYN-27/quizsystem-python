from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Admin, Lecturer, Student



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Role', choices=[('student','student'),('admin','admin'),('lecturer','lecturer'),])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

