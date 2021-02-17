# User accounts program
# Adds and removes user

# User Account: addUserAccount(), deleteUserAccount(accountID), displayUserAccounts() 

# Importing and connecting
import sqlite3
connection=sqlite3.connect("FamTreePrototype.db")
cursor=connection.cursor()

# Importing hashlib for password hashing
from hashlib import sha256

# Dropping for resetting the table
#cursor.execute("DROP TABLE IF EXISTS UserAccounts;")

# Creating user accounts table if not exists:
cursor.execute("""CREATE TABLE IF NOT EXISTS UserAccounts(accountID INTEGER PRIMARY KEY AUTOINCREMENT, accountName VARCHAR(100), accountEmail VARCHAR(100) UNIQUE, passwordHash VARCHAR(64));""")

# User account class
class UserAccount:
    def __init__(self):
        self.accountName=""
        self.accountEmail=""
        self.passwordHash=""
        
    def addUserAccount(self):
        self.accountName=input("Account name: ")
        self.accountEmail=input("Email ID: ")
        self.passwordHash=sha256(input("Password: ").encode()).hexdigest()
        cursor.execute("""INSERT INTO UserAccounts(accountName, accountEmail, passwordHash) VALUES("{}","{}","{}");""".format(self.accountName, self.accountEmail, self.passwordHash))
        cursor.execute("COMMIT;")
        
    def deleteUserAccount(self, accountID):
        cursor.execute("DELETE FROM UserAccounts WHERE accountID={};".format(accountID))
        cursor.execute("COMMIT;")
        
    def displayUserAccounts(self):
        cursor.execute("SELECT * FROM UserAccounts;")
        print(cursor.fetchall())
        
# User login verification
def userLogin(ID, password):
    cursor.execute("SELECT accountID FROM UserAccounts;")
    adminIDs=list(cursor.fetchall())
    if ID not in adminIDs:
        print("Invalid ID")
    else:
        id_condition=1
        
    cursor.execute("SELECT passwordHash FROM UserAccounts;")
    passwords=list(cursor.fetchall())
    if password not in passwords:
        print("Invalid password")
    else:
        password_conditon=1
        
    if id_condition==1 and password_conditon==1:
        return 1
    else:
        return 0