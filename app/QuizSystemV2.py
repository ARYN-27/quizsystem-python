import sqlite3
import flask
from flask_login import current_user, login_required, login_user, logout_user
from app.models import Admin, Student, Lecturer
from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.forms import LoginForm
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
#from werkzeug.security import generate_password_hash, check_password_hash, abort
from . import app, db

def get_db_connection(): #DB Connection
    conn = sqlite3.connect('quizsystem_database.db')
    conn.row_factory = sqlite3.Row
    return conn

#app = flask(__name__)
#app.config['SECRET_KEY'] = 'gmqk7a6m1hm65ogf7rw' 

def get_post(admin_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM Admin WHERE admin_id = ?',
                        (admin_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_post(lect_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM Lecturer WHERE lect_id = ?',
                        (lect_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_post(student_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM Student WHERE student_id = ?',
                        (student_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

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

@app.route('/')
def index():
    conn = get_db_connection()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/admin_landing') #Admin Landing Page
#@requires_roles('admin')
def admin_landing():
    conn = get_db_connection()
    conn.close()
    return render_template('admin_landing.html')

@app.route('/lecturer_landing') #Lecturer Landing Page
def lecturer_landing():
    conn = get_db_connection()
    conn.close()
    return render_template('lecturer_landing.html')

@app.route('/student_landing') #Student Landing Page
def student_landing():
    conn = get_db_connection()
    conn.close()
    return render_template('student_landing.html')

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

#ADMIN SEGMENT
#Creating Admins
@app.route('/admin_create', methods=('GET', 'POST'))
def admin_create():
    if request.method == 'POST':
        admin_id = request.form['admin_id']
        admin_name = request.form['admin_name']
        admin_pwd = request.form['admin_pwd']

        if not admin_name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO Admin (admin_id, admin_name, admin_pwd) VALUES (?, ?, ?)',
                         (admin_id, admin_name, admin_pwd))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('admin_create.html')

#Editing and Deleting Admin 
@app.route('/<int:admin_id>/admin_edit', methods=('GET', 'POST')) #Editing
def admin_edit(admin_id):
    post = get_post(admin_id)

    if request.method == 'POST':
        admin_id = request.form['admin_id']
        admin_name = request.form['admin_name']
        admin_pwd = request.form['admin_pwd']

        if not admin_id:
            flash('ID is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE Admin SET admin_name = ?, admin_pwd = ?'
                         ' WHERE admin_id = ?',
                         (admin_name, admin_pwd, admin_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('admin_edit.html', post=post)

@app.route('/<int:admin_id>/delete', methods=('POST',)) #Deleting 
def admin_delete(admin_id):
    post = get_post(admin_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM Admin WHERE admin_id = ?', (admin_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['admin_id']))
    return redirect(url_for('index'))

#LECTURER SEGMENT
#Creating Lecturer
@app.route('/lecturer_create', methods=('GET', 'POST'))
def lecturer_create():
    if request.method == 'POST':
        lect_id = request.form['lect_id']
        lect_name = request.form['lect_name']
        lect_email = request.form['lect_email']
        lect_pwd = request.form['lect_pwd']
        admin_id = request.form['admin_id']

        if not lect_name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO Lecturer (lect_id, lect_name, lect_email, lect_pwd, admin_id) VALUES (?, ?, ?, ?, ?)',
                         (lect_id, lect_name, lect_email, lect_pwd, admin_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('lecturer_create.html')

#Editing and Deleting Lecturer
@app.route('/<int:lect_id>/lecturer_edit', methods=('GET', 'POST')) #Editing
def lecturer_edit(lect_id):
    post = get_post(lect_id)

    if request.method == 'POST':
        lect_id = request.form['lect_id']
        lect_name = request.form['lect_name']
        lect_email = request.form['lect_email']
        lect_pwd = request.form['lect_pwd']
        admin_id = request.form['admin_id']

        if not lect_id:
            flash('ID is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE Lecturer SET lect_name = ?, lect_email = ?, lect_pwd = ?, admin_id = ?'
                         ' WHERE lect_id = ?',
                         (lect_name, lect_email, lect_pwd, admin_id, lect_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('lecturer_edit.html', post=post)

@app.route('/<int:lect_id>/lecturer_delete', methods=('POST',)) #Deleting 
def lecturer_delete(lect_id):
    post = get_post(lect_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM Lecturer WHERE lect_id = ?', (lect_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['lect_id']))
    return redirect(url_for('index'))

#STUDENT SEGMENT
#Creating Student
@app.route('/student_create', methods=('GET', 'POST'))
def student_create():
    if request.method == 'POST':
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        student_email = request.form['student_email']
        student_pwd = request.form['student_pwd']        
        admin_id = request.form['admin_id']

        if not student_name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO Student (student_id, student_name, student_email, student_pwd, admin_id) VALUES (?, ?, ?, ?, ?)',
                         (student_id, student_name, student_email, student_pwd, admin_id))
            conn.close()
            return redirect(url_for('index'))
    return render_template('student_create.html')

#Editing and Deleting Student
@app.route('/<int:student_id>/student_edit', methods=('GET', 'POST')) #Editing
def student_edit(student_id):
    post = get_post(student_id)

    if request.method == 'POST':
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        student_email = request.form['student_email']
        student_pwd = request.form['student_pwd']
        admin_id = request.form['admin_id']

        if not student_id:
            flash('ID is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE Student SET student_name = ?, student_email = ?, student_pwd = ?, admin_id = ?'
                         ' WHERE student_id = ?',
                         (student_name, student_email, student_pwd, admin_id, student_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('student_edit.html', post=[post])

@app.route('/<int:student_id>/student_delete', methods=('POST',)) #Deleting 
def student_delete(student_id):
    post = get_post(student_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM Student WHERE student_id = ?', (student_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['student_id']))
    return redirect(url_for('index'))

