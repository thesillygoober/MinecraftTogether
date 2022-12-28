# MinecraftServerTool Main File

# Imports
from os import system
import shutil
import tkinter as tk
from tkinter import filedialog
from time import sleep as wait

# Colorama
import colorama
colorama.init()

# Variables
isGitInstalled = False

# Functions
def checkForGit():
    if shutil.which("git") == None:
        print(colorama.Fore.YELLOW + "WARNING | Git is not installed on this machine,\n          so auto-updating a server from a remote\n          repository will not be available." + colorama.Fore.WHITE)
    else:
        isGitInstalled = True

def startServer(file_path):
    system("cls && cd \"" + file_path + "\" &&" + "\"" + file_path + "/start.bat\"")

def addServer():
    system("cls")
    print(colorama.Fore.CYAN + "ATTENTION | Select the server folder!" + colorama.Fore.WHITE)
    wait(1)
    print("Liftoff in 3..")
    wait(1)
    print("Liftoff in 2..")
    wait(1)
    print("Liftoff in 1..")
    wait(1)

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()

    pass # Find b0nkus_db and add the code here or rewrite it (please no)

def snsServer():
    print("Select a server to start:") # Add some code after this that reads the servers and yktr

# Init
print("b0nk's MinecraftServerTool\n------------------------------------------")

checkForGit()

print("\nSelect an option:\n1) Add Server To MST\n2) Sync & Start Server")
choice = input()

if choice == "1":
    addServer()
elif choice == "2":
    snsServer()