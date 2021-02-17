# Relationship table
# Manages child-parent relationships

# Relationship: addRelationship(), deleteRelationship(relationshipID), displayRelationship()

# Importing and connecting import
import sqlite3
connection = sqlite3.connect("FamTreePrototype.db")
cursor = connection.cursor()

# Dropping for resetting the table
#cursor.execute("DROP TABLE IF EXISTS Relationship;")

# Creating relationship table if not exists
cursor.execute("""CREATE TABLE Relationship(relationshipID INTEGER NOT NULL PRIMARY KEY, parentID INTEGER FOREIGN KEY (parentID) REFERENCES UserAccounts(accountID)), childID FOREIGN KEY (childID) REFERENCES UserAccounts(accountID));""")

# Relatioship class
class Relationship:
    def __init__(self):
        self.relationshipID = 0
        self.parentID = 0
        self.childID = 0
        
    def addRelationship(self):
        self.parentID=int(input("Parent ID: "))
        self.childID=int(input("Child ID: "))
        self.relationshipID= 1000000+(1000*self.parentID)+self.childID
        cursor.execute("""INSERT INTO Relationship(relationshipID, parentID, childID) VALUES("{}","{}","{}");""".format(self.relationshipID, self.parentID, self.childID))
        cursor.execute("COMMIT;")
        
    def deleteRelationship(self, relationshipID):
        cursor.execute("DELETE FROM Relationship WHERE relationshipID={};".format(relationshipID))  
              
    def displayRelationship(self):
        cursor.execute("""SELECT * FROM Relationship;""")
        print(cursor.fetchall())