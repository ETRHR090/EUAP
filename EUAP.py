#swift.py
import sqlite3
import os
DBName = "EUAP.db"
def EUAP_Change(Value):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''UPDATE SETTINGS SET VAL = ? WHERE INFO = "EUAP_Enabled"''', [Value])
    conn.commit()
    conn.close()
def GetFile(File, Location):
    import os
    try:
        os.system("pip install wget")
        import wget # type: ignore
        wget.download(File, Location)
    except:
        return ConnectionError
def Add_User(Username, Password):
    import sqlite3
    import os
    DBName = "EUAP.db"
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
    import sqlite3
    DBName = "EUAP.db"
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
    import sqlite3
    DBName = "EUAP.db"
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT)''')
    c.execute("SELECT * FROM EUAP")
    AllUsers = c.fetchall()
    c.close()
    return AllUsers
def Change_User_Password(NewPassword, Username):
    import sqlite3
    DBName = "EUAP.db"
    conn = sqlite3.connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT)''')
    c.execute("UPDATE EUAP SET Password = ? WHERE Username = ?", [NewPassword, Username])
    conn.commit()
    conn.close()
def Delete_User(Username):
    import sqlite3
    DBName = "EUAP.db"
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT)''')
    c.execute("DELETE FROM EUAP WHERE Username = ?", [Username])
    conn.commit()
    c.close()
