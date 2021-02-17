# User Details program
# Gets user details and stores in UserDetails table

# UserDetails: addUserDetails(), removeUser(accountID), displayUsers()

# Importing and connecting
import sqlite3
connection = sqlite3.connect("FamTreePrototype.db")
cursor = connection.cursor()

# Dropping for resetting the table
#cursor.execute("DROP TABLE IF EXISTS UserDetails;")

# Creating user details table if not exists:
cursor.execute("""CREATE TABLE IF NOT EXISTS UserAccounts(accountID INTEGER FOREIGN KEY(accountID) REFERENCES UserAccount(accountID), fname VARCHAR(100) NOT NULL, mname VARCHAR(100), lname VARCHAR(100) NOT NULL, accountEmail VARCHAR(100) FOREIGN KEY (emailID) REFERENCES UserAccount(emailID), DOB VARCHAR(100), bloodgroup VARCHAR(100));""")

# User Account class
class UserDetails:
    def __init__(self):
        self.accountID=0
        self.fname=""
        self.mname=""
        self.lname=""
        self.email=""
        self.DOB=""
        self.bloodgroup=""
    
    def addUserDetails(self):
        print("Enter the details: ")
        self.accountID=int(input("Account ID: "))
        self.fname=input("First name: ")
        self.mname=input("Middle name: ")
        self.lname=input("Last name: ")
        self.email=input("Email: ")
        self.DOB=input("DOB: ")
        cursor.execute("""INSERT INTO UserAccounts (accountID, fname, mname, lname, email, DOB, bloodgroup) VALUES("{}","{}","{}","{}","{}","{}");""".format(self.accountID, self.fname, self.mname, self.lname, self.email, self.DOB))
        cursor.execute("COMMIT;")
        
    def removeUser(self, accountID):
        cursor.execute("DELETE FROM UserAccounts WHERE accountID=={};".format(accountID))
        cursor.execute("COMMIT;")
        
    def displayUsers(self):
        cursor.execute("SELECT * FROM UserAccount;")
        print(cursor.fetchall())