import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('quizsystem_database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(admin_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM Admin WHERE admin_id = ?',
                        (admin_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gmqk7a6m1hm65ogf7rw'

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM Admin').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

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

@app.route('/<int:admin_id>/admin_edit', methods=('GET', 'POST'))
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

@app.route('/<int:admin_id>/delete', methods=('POST',))
def delete(admin_id):
    post = get_post(admin_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM Admin WHERE admin_id = ?', (admin_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))