# FamTreePrototype Session Logs
# Keeps track of session details

# SessionLog: start(), end(), addSession(), showSessionLog()

# Import and connect
import sqlite3
connection = sqlite3.connect("FamTreePrototype.db")
cursor = connection.cursor()

# Importing datetime for use in timestamp
import datetime

# Dropping for resetting the table
#cursor.execute("DROP TABLE IF EXISTS SessionLog;")

# Creating session log table if not exists:
cursor.execute("""CREATE TABLE IF NOT EXISTS SessionLog(sessionID INTEGER PRIMARY KEY AUTOINCREMENT, accountID VARHCAR(100) FOREIGN KEY (accountID) REFERENCES UserAccounts(accountID) ,start_timestamp VARCHAR(100), end_timestamp VARCHAR(64));""")

# Session log class:
class SessionLog:
    def __init__(self,accountID):
        self.sessionID=0
        self.accountID=accountID
        self.start_timestamp=""
        self.end_timestamp=""
        
    def start(self):
        self.start_timestamp = datetime.datetime.now()
        
    def end(self):
        self.end_timestamp = datetime.datetime.now()
        
    def addSession(self):
        cursor.execute("""INSERT INTO SessionLog(accountID,start_timestamp,end_timestamp) VALUES("{}","{}","{}");""".format(self.accountID,self.start_timestamp,self.end_timestamp))
        cursor.execute("COMMIT;")
        
    def showSessionLog(self):
        cursor.execute("SELECT * FROM SessionLog;")
        print(cursor.fetchall())
        
    