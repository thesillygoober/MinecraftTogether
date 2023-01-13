# MinecraftServerTool Main File

# This code may not be optimized very well and there most likely is strange variable naming.
# Go forth at your own risk. (eyeball torture)

# Imports
import os
from os import system, startfile as sf
import shutil
import tkinter as tk
from tkinter import filedialog
from time import sleep as wait
import sys

# SQLite
import sqlite3 as sql
databaseCon = sql.connect("serverdata.db")
dbCursor = databaseCon.cursor()

# Colorama
import colorama
colorama.init()

# Variables
version = "v1.0.1" # Change for update

# Functions
def resource_path(relative_path): # PyInstaller Support
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def color_print(color, text):
    """ Print out text with a certain color """
    print(color + text + colorama.Fore.WHITE)

def color_input(color):
    """ Input function that colors the text """
    returnInput = input(color)
    print(colorama.Fore.WHITE)
    return returnInput

def checkForGit():
    """ Checks if git is installed to path """
    if shutil.which("git") == None:
        color_print(colorama.Fore.YELLOW, "WARNING | Git is not installed on this machine,\n          so auto-updating a server from a remote\n          repository will not be available.\n")

def init_func():
    """ Initializes the MinecraftTogether Client """
    system("cls && title MinecraftTogether - Menu")
    print(f"MinecraftTogether Client {version}\n------------------------------------------")
    checkForGit()
    print("Select an option:\n1) Manage Servers\n2) Change or Remove Tunneler\n3) Exit")
    choice = color_input(colorama.Fore.GREEN)
    check_choice(choice)

def mng_server():
    """ Starts the server manager """
    system("cls && title MinecraftTogether - Managing Servers")
    print("Server Management Options\n\n1) Add Server from List\n2) Start Server from List\n3) Delete Server from List")
    choice = color_input(colorama.Fore.GREEN)

    if choice == "1":
        add_server()
    elif choice == "2":
        sns_server()
    elif choice == "3":
        del_server()
    else:
        print("That is not an option. Try again.")
        wait(1)
        mng_server()

def cut_fptd(filePath, numToStop): # Cut File Path To Directory
    """ Cuts the directory down to a specific index """
    returnString = ""
    splitString = str.split(filePath, "/")
    stopFunc = False

    for subStr in splitString:
        if subStr == splitString[numToStop*-1]:
            stopFunc = True
        if not stopFunc:
            returnString += subStr + "/"
    
    return returnString

def start_server(filePath): # Needs an update, originally intended to just be with the directory and not the start file
    """ Start a server from a file path """
    directory = cut_fptd(filePath, 1)

    try:
        dbCursor.execute("SELECT * FROM tunneler")
        tunnelerPath = dbCursor.fetchall()
        print(tunnelerPath)
        testVar = tunnelerPath[0][0] # To test if it is there
        if not str.split(tunnelerPath[0][0], "/")[-1] == "ngrok.exe":
            sf(tunnelerPath[0][0])
        else:
            sf(resource_path("ngrokstarter.py"))
    except:
        print("Proceeding with no tunneler.")
    
    system(f"cls && title MinecraftTogether - Running Server && cd \"{directory}\" && \"{filePath}\"")

def add_server():
    """ Add a server to the serverdata database """
    system("cls && title MinecraftTogether - Adding Server")
    color_print(colorama.Fore.CYAN, "ATTENTION | Select the file that starts the server!")
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
    if shutil.which("git") != None:
        color_print(colorama.Fore.CYAN, "\nATTENTION | Server folder needs to have the same name as the repository.")
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
    """ Sync server if applicable and use start server function """
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
                if shutil.which("git") != None and servers[int(serverChoice)-1][1] != "":
                    try:
                        system(f"cd {cut_fptd(servers[int(serverChoice)-1][0], 2)} && git clone {servers[int(serverChoice)-1][1]}")
                        start_server(servers[int(serverChoice)-1][0])
                    except:
                        print(f"Would you like to proceed without cloning from a remote repository? We couldn't pull from {servers[int(serverChoice)-1][1]}.\n\n1) Yes\n2) No")
                        choice = color_input(colorama.Fore.GREEN)
                        if choice == "1":
                            start_server(servers[int(serverChoice)-1][0])
                        elif choice == "2":
                            print("Press enter to go back to the menu.")
                            input()
                        else:
                            print("That was not an option, press enter to go back to menu.")
                            input()
                else:
                    start_server(servers[int(serverChoice)-1][0])
    except:
        system("cls")
        print("No servers found. Press enter to go back to menu.")
        input()
        init_func()

    init_func()

def del_server():
    """ Delete server from the database """
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
    """ Change or remove a tunneler """
    system("cls && title MinecraftTogether - Tunneler Options")
    print("Would you like to change or remove tunneler?\n\n1) Change Tunneler\n2) Remove Tunneler")
    choice = color_input(colorama.Fore.GREEN)

    if choice == "1":
        system("cls && title MinecraftTogether - Changing Tunneler")
        color_print(colorama.Fore.CYAN, "ATTENTION | Select the tunneler .exe!")
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
    """ Init function choice function, should probably be implemented into init_func """
    if choice == "1":
        mng_server()
    elif choice == "2":
        cor_tunneler()
    elif choice == "3":
        sys.exit()
    else:
        print("\nThat is not an option. Try again.\n")
        wait(1)
        init_func()

# Init
init_func()