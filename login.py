import sqlite3
from flask import Blueprint, render_template, redirect, url_for, request, flash
#from werkzeug.security import generate_password_hash, check_password_hash #Hashing Elements
#from flask_login import login_user, logout_user, login_requiredfrom . import db
from . import db


def get_db_connection(): #DB Connection
    conn = sqlite3.connect('quizsystem_database.db')
    conn.row_factory = sqlite3.Row
    return conn

def insertUser(admin_id,admin_pwd):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO Admin (admin_id,admin_pwd) VALUES (?,?)", (admin_id,admin_pwd))
    con.commit()
    con.close()

def retrieveUsers():
	con = get_db_connection()
	cur = con.cursor()
	cur.execute("SELECT admin_id, admin_pwd FROM Admin")    
	users  = cur.fetchall()
	con.close()
	return render_template('admin_landing.html')