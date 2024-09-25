How to use EUAP
Firstly, import the file to your code, using the command 'import EUAP.py'.
Then, you have 5 different commands to use. These are:
'Add_User', 'Get_User_Password', 'Get_All_Users', 'Change_User_Password', 'Delete_User'
The add user command is called using: 'Add_User(ExampleUsername, ExamplePassword)'. This is used to add a user to the database. If the user already exists this function will return FileExistsError
The command to get a user password is 'Get_User_Password(ExampleUsername)'. This function returns a user's password. If the user is not found, it will return None.
The command to get all users is 'Get_All_Users()'. This will return a list with each users id, username and password. If the database is empty it will return '[]'
The command to change a users password is 'Change_Users_Password(NewExamplePassword, Username)'. This command will change a users password to the new password given.
the command to delete a user is 'Delete_User(Username)'. This command will delete a users entry in the database.
