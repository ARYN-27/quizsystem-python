import sqlite3

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
	return users 