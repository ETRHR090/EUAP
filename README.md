# EUAP
Easy Usernames and Passwords for Python

##########################--How to use EUAP--######################
Firstly, import the file to your code, using the command 'import EUAP.py'.
You have 8 different commands you can use. These are: 'Initialise', Add_User', 'Get_User_Password', 'Get_All_Users', 'Change_User_Password', 'Delete_User', 'UserCheck'.
The Initialise command is to set the files working path, and must be used after it is imported. It is used by calling the command Initialise(ExamplePath). This sets where the file will be used, and changes the directory to there. 
The add user command is called using: 'Add_User(ExampleUsername, ExamplePassword, Userpath)'. This is used to add a user to the database. If the user already exists this function will return FileExistsError 
The command to get a user password is 'Get_User_Password(ExampleUsername)'. This function returns a user's password. If the user is not found, it will return None. 
The command to get all users is 'Get_All_Users()'. This will return a list with each users id, username, password, and Path. If the database is empty it will return '[]' 
The command to change a users password is 'Change_Users_Password(NewExamplePassword, Username)'. This command will change a users password to the new password given. 
The command to delete a user is 'Delete_User(Username)'. This command will delete a users entry in the database. 
The command usercheck checks if a users username and password are correct. The command is 'UserCheck(ExampleUsername, ExamplePassword)'. This will return True if the users username and password are correct and False if either of them are not correct. 
If you open the file with python directly it will display a terminal where you can interact with the terminal directly
##########################--Notes--######################
The 'delete' command does not check if the user exists, and will return an error if the user doesn't exist
