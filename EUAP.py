import os
#EUAP V1.0.4
FileDir = os.getcwd()
import sqlite3
import os
DBName = "EUAP.db"
SetName = "Settings.db"
def Add_User(Username, Password, UserPath):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT, UserPath TEXT)''')
    c.execute('SELECT * FROM EUAP WHERE Username = ?', [Username])
    if c.fetchall() != []:
        return FileExistsError
    else:
       
       c.execute('INSERT INTO EUAP(Username, Password, UserPath) VALUES(?, ?, ?)', [Username, Password, UserPath])
       conn.commit()
       conn.close()
def Get_User_Password(Username):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT, UserPath TEXT)''')
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
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT, UserPath TEXT)''')
    c.execute("SELECT * FROM EUAP")
    AllUsers = c.fetchall()
    c.close()
    return AllUsers
def Change_User_Password(NewPassword, Username):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT, UserPath TEXT)''')
    c.execute("UPDATE EUAP SET Password = ? WHERE Username = ?", [NewPassword, Username])
    conn.commit()
    conn.close()
def Delete_User(Username):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT, UserPath TEXT)''')
    c.execute("DELETE FROM EUAP WHERE Username = ?", [Username])
    conn.commit()
    c.close()
def UserCheck(Username, Password):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT, UserPath TEXT)''')
    c.execute("SELECT * FROM EUAP WHERE Username = ? AND Password = ?", [Username, Password])
    if c.fetchall() == []:
        c.close()
        return False
    else:
        c.close()
        return True
def GetUserPath(Username):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT, UserPath TEXT)''')
    c.execute("Select UserPath from EUAP where Username = ?", [Username])
def UserCount():
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute("Select * FROM EUAP")
    return len(c.fetchall())
def GetUsernames():
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS EUAP
             (id INTEGER PRIMARY KEY, Username TEXT, Password TEXT, UserPath TEXT)''')
    c.execute("SELECT Username FROM EUAP")
    return c.fetchall()
while __name__ == "__main__":
    Mode = input("(1)Add User\n(2)Get User Password\n(3)Get All Users\n(4)Change User Password\n(5)Delete User\n(6)User Check\n(7)Get User Path\n(8)User Count\n(9)Get All Usernames\n(0)Exit\n")
    if Mode == "1":
        Add_User(input("Username:\n"), input("Password:\n"), input("Path:\n"))
    elif Mode == "2":
        input(Get_User_Password(input("Username:\n")))
    elif Mode == "3":
        print(Get_All_Users())
    elif Mode == "4":
        Change_User_Password(input("New Password:\n", input("User:\n")))
    elif Mode == "5":
        Delete_User(input("Username:\n"))
    elif Mode == "6":
        input(UserCheck(input("Username:\n"), input("Password:\n")))
    elif Mode == "7":
        GetUserPath(input("Username:\n"))
    elif Mode == "8":
        input(UserCount())
    elif Mode == "9":
        input(GetUsernames())
    elif Mode == "0":
        exit()