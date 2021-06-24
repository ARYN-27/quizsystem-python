from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.widgets.core import PasswordInput
from app.models import User


class LoginForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('admin','Admin'),('lecturer','Lecturer'),('student','Student')], default=1)
    submit = SubmitField('Register')

    def validate_username(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email.')
        
    def validate_password(self, password):
        user = User.query.filter_by(password=password.data).first()
        if user is not None:
            raise ValidationError('Please use a different password.')
