# FamTree Prototype
# Based on CS essentials case study

# Importing other modules
from FamTreePrototypeAdmin import Admin, adminLogin
from FamTreePrototypeSession import SessionLog
from FamTreePrototypeUserAccounts import UserAccount, userLogin
from FamTreePrototypeUserDetails import UserDetails
from FamTreePrototypeRelationship import Relationship

# Importing and connectiong to DB:
import sqlite3
connection=sqlite3.connect("FamTreePrototype.db")
cursor=connection.cursor()

# Login
def signin():
    accountID=input("Enter account ID: ")
    password=input("Enter password: ")
    login=userLogin(accountID, password)
    if login==1:
        pass
    else:
        choice=input("Account does not exist. Signup? (y/n)")
        if choice=='y':
            UserAccount.addUserAccount()
            UserDetails.addUserDetails()
            Relationship.addRelationship()
            sessionLog=SessionLog(accountID)
            sessionLog.start()
        else:
            signin()
            
# Actions
queries = ['1. Display details of a particular user, given name.',
           '2. Find the parent of a particular user.',
           '3. Find the number of children.',
           '4. Find siblings',
           '5. Find head person.',
           '6. Find user with highest number of children',
           '7. Find the cousins',
           '8. Find grandparents',
           '9. Alter details',
           '10. Logout']

# Function 1
def DisplayDetails():
    accountID=input("Enter account ID: ")
    cursor.execute("SELECT * FROM UserDetails WHERE accountID={};".format(accountID))
    print(cursor.fetchone())    
    
# Function 2
def findParent():
    accountID=input("Enter account ID of the child user: ")
    cursor.execute("""SELECT * FROM UserDetails WHERE accountID=(SELECT parentID from Relationship WHERE childID={});""".format(accountID))
    print(cursor.fetchone())
                
# Function 3
def numberOfChildren():
    accountID=input("Enter the account ID of parent user: ")
    cursor.execute("""SELECT COUNT(*) FROM UserDetails WHERE accountID=(SELECT childID from Relationship WHERE parentID={});""".format(accountID))
    print(cursor.fetchone())

# Funtion 4
def findSiblings():
    accountID=input("Enter the account ID of the user: ")
    cursor.execute("""SELECT * FROM UserDetails WHERE accountID=(SELECT childID from Relationship WHERE parentID=(SELECT parentID from Relationship WHERE childID={});""".format(accountID))
    print(cursor.fetchall())
    
# Function 5
def findHead():
    cursor.execute("""SELECT * FROM UserDetails WHERE accountID=(SELECT childID from Relationship WHERE parentID=0);""")
    print(cursor.fetchone())
    
# Find 6
def findMaxChildren():
    cursor.execute("""SELECT MAX(accountID) FROM UserDetails;""")
    max=int(cursor.fetchone())
    maxchild=0
    maxchildindex=0
    for i in range(1,max+1):
        cursor.execute("""SELECT COUNT(*) FROM UserDetails WHERE accountID=(SELECT childID from Relationship WHERE parentID={});""".format(i))
        val=int(cursor.fetchone())
        if val>maxchild:
            maxchild=val
            maxchildindex=i
    cursor.execute("""SELECT * FROM UserDetails WHERE accountID={}""".format(maxchildindex))
    print("The number of children is ", maxchild, " and the parent is: ", (cursor.fetchone()))
    
# Function 7
def findCousins():
    accountID=int(input("Account ID: "))
    cursor.execute("""SELECT * FROM UserDetails WHERE accountID=(SELECT childID from Relationship WHERE parentID=(SELECT childID from Relationship WHERE parentID=(SELECT parentID from Relationship WHERE childID=(SELECT parentID from Relationship WHERE childID={}))));""".format(accountID))
    print(cursor.fetchall())

# Funtion 8
def findGrandParent():
    accountID=int(input("Account ID: "))
    cursor.execute("""SELECT * FROM UserDetails WHERE accountID=(SELECT parentID from Relationship WHERE childID=(SELECT parentID from Relationship WHERE parentID=(SELECT parentID from Relationship WHERE childID={})));""".format(accountID))
    print(cursor.fetchone())
    
# Function 9
def Alter():
    command=input("Enter the SQL comamnd: ")
    cursor.execute(command)
    cursor.execute("COMMIT;");

condition=True
while condition:
    for i in range(len(queries)):
        print(queries[i])
    choice=int("Enter choice number: ")
    
    if choice==1:
        DisplayDetails()
    elif choice==2:
        findParent()
    elif choice==3:
        numberOfChildren()
    elif choice==4:
        findSiblings()
    elif choice==5:
        findHead()
    elif choice==6:
        findMaxChildren()
    elif choice==7:
        findCousins()
    elif choice==8:
        findGrandParent()
    elif choice==9:
        Alter()
    elif choice==10:
        conditon=False
    else:
        print("Enter a valid choice")

