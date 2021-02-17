# Admin program
# Adds and removes admin

# Admin: addAdmin(), removeAdmin()
# login(ID,password)

# importing and setting up:
import sqlite3
connection = sqlite3.connect("FamTreePrototype.db")
cursor = connection.cursor()

# Dropping for resetting the table
#cursor.execute("DROP TABLE IF EXISTS AdminDetails;")

# Importing hashlib
from hashlib import sha256

# Creating admin table:
cursor.execute("""CREATE TABLE IF NOT EXISTS AdminDetails(adminID INTEGER PRIMARY KEY AUTOINCREMENT, adminName VARHCAR(100),adminEmail VARCHAR(100) UNIQUE, passwordHash VARCHAR(64));""")

# Creating a admin class
class Admin:
    def __init__(self):
        self.adminName = ""
        self.adminEmail = ""
        self.passwordHash = ""

    def addAdmin(self):
        self.adminName = input("Enter the name of the admin: ")
        self.adminEmail = input("Enter the email: ")
        self.passwordHash = sha256(input("Enter the password: ").encode()).hexdigest()
        cursor.execute(""" INSERT INTO AdminDetails(adminName, adminEmail, passwordHash) VALUES("{}","{}","{}");""".format(self.adminName, self.adminEmail,self.passwordHash))
        cursor.execute("COMMIT;")

    def removeAdmin(self, adminID):
        cursor.execute("""
        --sql
        DELETE * FROM AdminDetails WHERE adminID={}
        ;
        """.format(self.adminID))
        cursor.execute("COMMIT;")
        
print("ADMIN PROGRAM")
choice=1
while choice==1 or choice==2:
    choice=int(input("Enter 1 to add data and 2 to remove data and 3 to display data and terminate: "))
    admin = Admin()
    if choice==1: 
        admin.addAdmin()
    elif choice==2:
        admin.removeAdmin()
    else:
        cursor.execute("SELECT * FROM AdminDetails;")
        print(cursor.fetchall())
        break

# Admin login verification
def adminLogin(ID, password):
    cursor.execute("SELECT adminID FROM AdminDetails;")
    adminIDs=list(cursor.fetchall())
    if ID not in adminIDs:
        print("Invalid ID")
    else:
        id_condition=1
        
    cursor.execute("SELECT passwordHash FROM AdminDetails;")
    passwords=list(cursor.fetchall())
    if password not in passwords:
        print("Invalid password")
    else:
        password_conditon=1
        
    if id_condition==1 and password_conditon==1:
        return 1
    else:
        return 0