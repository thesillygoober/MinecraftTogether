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
dbCursor = databaseCon.cursor()

# Colorama
import colorama
colorama.init()

# Variables
isGitInstalled = False

# Functions
def color_input(color):
    returnInput = input(color)
    print(colorama.Fore.WHITE)
    return returnInput

def checkForGit():
    if shutil.which("git") == None:
        print(colorama.Fore.YELLOW + "WARNING | Git is not installed on this machine,\n          so auto-updating a server from a remote\n          repository will not be available.\n" + colorama.Fore.WHITE)
    else:
        isGitInstalled = True

def init_func():
    system("cls && title MinecraftTogether - Menu")
    print("MinecraftTogether Client\n------------------------------------------")

    checkForGit()

    print("Select an option:\n1) Add Server To List\n2) Start Server From List\n3) Delete Server From List\n4) Exit Client")
    choice = color_input(colorama.Fore.GREEN)
    check_choice(choice)

def cut_fptd(filePath): # Cut File Path To Directory
    returnString = ""
    splitString = str.split(filePath, "/")

    for subStr in splitString:
        if not subStr == splitString[-1]:
            returnString += subStr + "/"
    
    return returnString

def start_server(filePath): # Needs an update, originally intended to just be with the directory and not the start file
    directory = cut_fptd(filePath)
    system(f"cls && title MinecraftTogether - Running Server && cd \"{directory}\" && \"{filePath}\"")

def add_server():
    system("cls && title MinecraftTogether - Adding Server")
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

    repoToGo = ""
    if isGitInstalled:
        print("Add a repository to clone from (leave empty for none): ")
        repoToGo = color_input(colorama.Fore.GREEN)
        repoToGo = repoToGo.replace(" ", "")
    
    if repoToGo == "":
        print("Proceeding with no remote repository.")
    else:
        print("Proceeding with " + repoToGo + ", if it errors whilst starting, come back here and fix this value.")

    wait(2)

    with databaseCon:
        dbCursor.execute("CREATE TABLE IF NOT EXISTS serverpaths(startfile TEXT, repo TEXT)")
        dbCursor.execute(f'DELETE FROM serverpaths WHERE startfile = "{filePath}"')
        dbCursor.execute(f'INSERT INTO serverpaths VALUES ("{filePath}", "{repoToGo}")') # Single quotes because of filePath double quotes
        dbCursor.execute("SELECT * FROM serverpaths")
        tableContents = dbCursor.fetchall()

        print("The server " + str.split(tableContents[-1][0], "/")[-2] + " has been added to the list.")
    
    wait(1)
    init_func()

def sns_server():
    system("cls && title MinecraftTogether - Starting Server")
    try:
        print("Select a server to start:\n")

        with databaseCon:
            dbCursor = databaseCon.cursor()
            dbCursor.execute("SELECT * FROM serverpaths")
            servers = dbCursor.fetchall()
            testVar = servers[0][0] # Tests if a server exists, except statement catches
            number = 1
            for server in servers:
                print(str(number) + ") " + str.split(server[0], "/")[-2])
                number += 1
            
            serverChoice = color_input(colorama.Fore.GREEN)
            if int(serverChoice) > number or int(serverChoice) < 1:
                print("That is not an option. Try again.\n")
                wait(1)
                sns_server()
            else:
                start_server(servers[int(serverChoice)-1][0])
    except:
        system("cls")
        print("No servers found. Press enter to go back to menu.")
        input()
        init_func()

    init_func()

def del_server():
    system("cls && title MinecraftTogether - Deleting Server")
    print("Select a server to delete:\n")

    try:
        with databaseCon:
            dbCursor.execute("SELECT * FROM serverpaths")
            servers = dbCursor.fetchall()
            testVar = servers[0][0] # Tests if a server exists, except statement catches
            number = 1
            for server in servers:
                print(str(number) + ") " + str.split(server[0], "/")[-2])
                number += 1

            serverChoice = color_input(colorama.Fore.GREEN)
            if int(serverChoice) > number or int(serverChoice) < 1:
                print("That is not an option. Try again.\n")
                wait(1)
                del_server()
            else:
                dbCursor.execute(f'DELETE FROM serverpaths WHERE startfile = "{servers[int(serverChoice)-1][0]}"')
                print(f'Succesfully deleted {str.split(servers[int(serverChoice)-1][0], "/")[-2]}')
                wait(1)
        init_func()
    except:
        system("cls")
        print("No servers found. Press enter to go back to menu.")
        input()
        init_func()
    
def check_choice(choice):
    if choice == "1":
        add_server()
    elif choice == "2":
        sns_server()
    elif choice == "3":
        del_server()
    elif choice == "4":
        exit()
    else:
        print("\nThat is not an option. Try again.\n")
        wait(1)
        init_func()

# Init
init_func()