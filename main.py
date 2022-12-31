# MinecraftServerTool Main File

# This code may not be optimized very well and there most likely is strange variable naming.
# Go forth at your own risk. (eyeball torture)

# Imports
from os import system, startfile as sf
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
    print("Select an option:\n1) Add Server To List\n2) Start Server From List\n3) Delete Server From List\n4) Change or Remove Tunneler\n5) Exit")
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

    try:
        dbCursor.execute("SELECT * FROM tunneler")
        tunnelerPath = dbCursor.fetchall()
        print(tunnelerPath)
        testVar = tunnelerPath[0][0] # To test if it is there
        if not str.split(tunnelerPath[0][0], "/")[-1] == "ngrok.exe":
            sf(tunnelerPath[0][0])
        else:
            sf("ngrokstarter.py")
    except:
        print("Proceeding with no tunneler.")
    
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
        dbCursor.execute(f'INSERT INTO serverpaths VALUES ("{filePath}", "{repoToGo}")')
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

def cor_tunneler():
    system("cls && title MinecraftTogether - Tunneler Options")
    print("Would you like to change or remove tunneler?\n\n1) Change Tunneler\n2) Remove Tunneler")
    choice = color_input(colorama.Fore.GREEN)

    if choice == "1":
        system("cls && title MinecraftTogether - Changing Tunneler")
        print(colorama.Fore.CYAN + "ATTENTION | Select the tunneler .exe!" + colorama.Fore.WHITE)
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
            dbCursor.execute("CREATE TABLE IF NOT EXISTS tunneler(startfile TEXT, delvalue INTEGER)")
            dbCursor.execute('DELETE FROM tunneler WHERE delvalue = 1')
            dbCursor.execute(f'INSERT INTO tunneler VALUES ("{filePath}", 1)')
            dbCursor.execute("SELECT * FROM tunneler")
            tableContents = dbCursor.fetchall()
            
            print("The tunneler " + str.split(tableContents[0][0], "/")[-1] + " has been selected.")
            wait(2)
        
        init_func()
    elif choice == "2":
        system("cls && title MinecraftTogether - Deleting Tunneler")
        tableContents = dbCursor.fetchall()

        try:
            with databaseCon:
                dbCursor.execute("DELETE FROM tunneler WHERE delvalue = 1")

            print("Successfully removed tunneler from server startup.")
            wait(1)
        except:
            print("Tunneler hasn't been added yet. Try again.")
            wait(1)
            cor_tunneler()

        init_func()
    else:
        print("That is not an option. Try again.\n")
        wait(1)
        cor_tunneler()
    
def check_choice(choice):
    if choice == "1":
        add_server()
    elif choice == "2":
        sns_server()
    elif choice == "3":
        del_server()
    elif choice == "4":
        cor_tunneler()
    elif choice == "5":
        exit()
    else:
        print("\nThat is not an option. Try again.\n")
        wait(1)
        init_func()

# Init
init_func()