#swift.py
import sqlite3
import os
DBName = "EUAP.db"
def Add_User(Username, Password):
    import os
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT)''')
    c.execute('SELECT * FROM EUAP WHERE Username = ?', [Username])
    UserCheck = c.fetchall()
    if UserCheck != []:
        return FileExistsError
    else:
       c.execute('INSERT INTO EUAP(Username, Password) VALUES(?, ?)', [Username, Password])
       conn.commit()
       conn.close()
def Get_User_Password(Username):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT)''')
    c.execute('SELECT Password FROM EUAP WHERE Username = ?', [Username])
    Password = c.fetchall()
    c.commit()
    c.close()
    if Password == []:
        return None
    else:
        return Password
def Get_All_Users():
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT)''')
    c.execute("SELECT * FROM EUAP")
    AllUsers = c.fetchall()
    c.close()
    return AllUsers
def Change_User_Password(NewPassword, Username):
    conn = sqlite3.connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT)''')
    c.execute("UPDATE EUAP SET Password = ? WHERE Username = ?", [NewPassword, Username])
    conn.commit()
    conn.close()
def Delete_User(Username):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT)''')
    c.execute("DELETE FROM EUAP WHERE Username = ?", [Username])
    conn.commit()
    c.close()
def UserCheck(Username, Password):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute("SELECT * FROM EUAP WHERE Username = ? AND Password = ?", [Username, Password])
    if c.fetchall() == []:
        return False
    else:
        return True
    