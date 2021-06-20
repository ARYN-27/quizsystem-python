from . import app, db
from flask_login import current_user, login_required, login_user, logout_user
from flask import url_for, redirect, render_template, flash
from app.login_forms import LoginForm
from app.models import Admin, Lecturer, Student, requires_roles


@app.route('/', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('customer'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(admin_id=form.admin_id.data).first()
        lecturer = Lecturer.query.filter_by(lect_id=form.lect_id.data).first()
        student = Student.query.filter_by(student_id=form.student_id.data).first()        
        if admin is None:
            flash('Invalid username')
            return redirect(url_for('signin'))
        login_user(admin, remember=form.remember_me.data)
        return redirect(url_for('admin'))
    return render_template('signin.html', title='Sign In', form=form)



@app.route('/student')
@login_required
@requires_roles('admin', 'student')
def student():
    return render_template('student_landing.html', title="Student Profile")


@app.route('/admin')
@login_required
@requires_roles('admin')
def admin():
    return render_template('admin_landing.html', title="Admin Profile")

@app.route('/lecturer')
@login_required
@requires_roles('admin', 'lecturer')
def lecturer():
    return render_template('lecturer_landing.html', title="Lecturer Profile")


@app.route('/logout')
@login_required
@requires_roles('admin','lecturer','student')
def logout():
    logout_user()
    return redirect(url_for('signin'))
