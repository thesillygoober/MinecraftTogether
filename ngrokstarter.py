# Ngrok Tunneler Starter (Could be applied to others, give feedback and I will fix)

# SQLite
import sqlite3 as sql
databaseCon = sql.connect("serverdata.db")
dbCursor = databaseCon.cursor()

# Other Imports
from os import system

# Main
try:
    dbCursor.execute("SELECT * FROM tunneler")
    tunnelPath = dbCursor.fetchall()
    print(tunnelPath)
    system(f'"{tunnelPath[0][0]}" tcp 25565')
except:
    print("you were NOT supposed to be here, make an issue on the github page if you see this!")
    input()