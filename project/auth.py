from .models import Admin, Student, Lecturer
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login_post():
    admin_id = request.form.get('admin_id')
    admin_pwd = request.form.get('admin_pwd')
    remember = True if request.form.get('remember') else False

    admin = Admin.query.filter_by(admin_id=admin_id).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not admin or not check_password_hash(admin.password, admin_pwd):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('main.profile'))

@auth.route('/logout')
def logout():
    return 'Logout'