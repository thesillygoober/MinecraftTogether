# MinecraftServerTool Main File

# Imports
from os import system
import shutil
import tkinter as tk
from tkinter import filedialog
from time import sleep as wait

# SQLite
import sqlite3 as sql
databaseCon = sql.connect("serverdata.db")

# Colorama
import colorama
colorama.init()

# Variables
isGitInstalled = False

# Functions
def checkForGit():
    if shutil.which("git") == None:
        print(colorama.Fore.YELLOW + "WARNING | Git is not installed on this machine,\n          so auto-updating a server from a remote\n          repository will not be available.\n" + colorama.Fore.WHITE)
    else:
        isGitInstalled = True

def init_func():
    system("cls")
    print("b0nk's MinecraftServerTool\n------------------------------------------")

    checkForGit()

    print("Select an option:\n1) Add Server To List\n2) Start Server From List\n3) Delete Server From List")
    choice = input()
    check_choice(choice)

def startServer(filePath): # Needs an update, originally intended to just be with the directory and not the start file
    system("cls && cd \"" + filePath + "\" &&" + "\"" + filePath + "/start.bat\"")

def add_server():
    system("cls")
    print(colorama.Fore.CYAN + "ATTENTION | Select the file that starts the server!" + colorama.Fore.WHITE)
    wait(1)
    print("Liftoff in 3..")
    wait(1)
    print("Liftoff in 2..")
    wait(1)
    print("Liftoff in 1..")
    wait(1)

    root = tk.Tk()
    root.withdraw()
    filePath = filedialog.askopenfilename()

    with databaseCon:
        dbCursor = databaseCon.cursor()
        dbCursor.execute("CREATE TABLE IF NOT EXISTS serverpaths(startfile TEXT)")
        dbCursor.execute(f'INSERT INTO serverpaths VALUES ("{filePath}")') # Single quotes because of filePath double quotes
        dbCursor.execute("SELECT * FROM serverpaths")
        tableContents = dbCursor.fetchall()
        print("The server " + str.split(tableContents[-1][0], "/")[-2] + " has been added to the list.")
    
    wait(3)
    init_func()

def sns_server():
    system("cls")
    print("Select a server to start:\n") # Add some code after this that reads the servers and yktr

    with databaseCon:
        dbCursor = databaseCon.cursor()
        dbCursor.execute("SELECT * FROM serverpaths")
        servers = dbCursor.fetchall()
        for server in servers:
            print(str.split(server[0], "/")[-2])

    input()

def check_choice(choice):
    if choice == "1":
        add_server()
    elif choice == "2":
        sns_server()

# Init
init_func()