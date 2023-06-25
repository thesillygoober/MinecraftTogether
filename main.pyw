#! /usr/bin/python

# Main File
# Used for UI & Server management and to start up other parts of the program like the setup wizard

# Imports
import tkinter as tk
import customtkinter as ctk
from customtkinter import filedialog
import platform
import os
from os import system as callc # call command
import subprocess

# Setup
ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green") 

app = ctk.CTk()
app.title("MinecraftTogether")
app.resizable(False, False)
app.geometry("400x240")

# Variables
selectedServer = tk.StringVar(app)
selectedServer.set("Choose a Server")

tunnelString = tk.StringVar(app)

serverData = {}

DEFAULT_SVDIR = "svdir.txt" # Server List Persistence Filename
DEFAULT_TDIR = "tunnel.txt" # Tunneler Persistence Filename

current_os = platform.system()

# Classes
class directory_handler:
    def split_directory(self, directory: str, split: int):
        """ Take part of a directory and return it """
        return str.split(directory, "/")[split]

    def cut_to_directory(self, directory: str):
        """ Cut directory down to remove the file """
        toPutTogether = directory.split("/")
        toPutTogether.pop(-1)
        
        result = ""
        
        if current_os == "Linux" or current_os == "Darwin":
            #toPutTogether.remove('')
            result = "/"

        for i in toPutTogether:
            if toPutTogether.index(i) != toPutTogether[-1]:
                result += i + "/"
            else:
                result += i
    
        return result
    
    def save_directories(self, directories: dict):
        with open(DEFAULT_SVDIR, 'w') as file:
            for name, path in directories.items():
                file.write(f"{name},{path}\n")
    
    def load_directories(self):
        directories = {}

        with open(DEFAULT_SVDIR, 'r') as file:
            for line in file:
                name, path = line.strip().split(',')
                directories[name] = path

        return directories

    def save_tunneler(self, tunneler: str):
        with open(DEFAULT_TDIR, 'w') as file:
            file.write(tunneler)
    
    def load_tunneler(self):
        tempTunneler = ""

        with open(DEFAULT_TDIR, 'r') as file:
            for line in file:
                tempTunneler = line
        
        return tempTunneler

# Objects
dh = directory_handler()

# Functions
def error_message(msg: str):
    error_window = ctk.CTk()
    error_window.title("MCT Error")
    error_window.resizable(False, False)
    error_window.geometry("200x120")

    error_label = ctk.CTkLabel(master=error_window, text="Error: " + msg, wraplength=200)
    error_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def check_file_compat(fileName: str):
    return (fileName.split(".")[-1] == "bat" and current_os == "Windows") or (fileName.split(".")[-1] == "sh" and (current_os == "Linux" or current_os == "Darwin"))

def get_server_options():
    serverOptions = []

    for i in serverData:
        serverOptions.append(i)
    
    return serverOptions

def add_server():
    fdResult = filedialog.askopenfilename()
    fileName = dh.split_directory(fdResult, -1)
    serverName = dh.split_directory(fdResult, -2)

    if check_file_compat(fileName) and not serverName in serverData:
        serverData[serverName] = fdResult
        server_dropdown = ctk.CTkOptionMenu(master=app, width=200, variable=selectedServer, values=get_server_options())
        server_dropdown.place_forget()
        server_dropdown.place(relx=0.7, rely=0.1, anchor=tk.CENTER)
    elif serverName in serverData and (fileName.split(".")[-1] == "bat" and current_os == "Windows") or (fileName.split(".")[-1] == "sh" and (current_os == "Linux" or current_os == "Darwin")):
        error_message("Server already exists")
    else:
        error_message("Incorrect file type, select .bat or .sh (Check GitHub wiki if confused)")
    
    dh.save_directories(serverData)
    
def remove_server():
    serverData.pop(selectedServer.get())
    dh.save_directories(serverData)
    server_dropdown = ctk.CTkOptionMenu(master=app, width=200, variable=selectedServer, values=get_server_options())
    server_dropdown.place_forget()
    server_dropdown.place(relx=0.7, rely=0.1, anchor=tk.CENTER)
    selectedServer.set("Choose a Server")

def start_server():
    if current_os == "Windows":
        subprocess.Popen(['start', 'cmd', '/c', serverData[selectedServer.get()]], cwd=dh.cut_to_directory(serverData[selectedServer.get()]), shell=True)
        if dh.load_tunneler() != "":
            subprocess.Popen(['start', 'cmd', '/c', dh.load_tunneler()], cwd=dh.cut_to_directory(dh.load_tunneler()), shell=True)
    elif current_os == "Linux":
        subprocess.Popen(['xterm', '-e', 'bash', '-c', serverData[selectedServer.get()]], cwd=dh.cut_to_directory(serverData[selectedServer.get()]))
        subprocess.Popen(['xterm', '-e', 'bash', '-c', dh.load_tunneler()], cwd=dh.cut_to_directory(dh.load_tunneler()))
    elif current_os == "Darwin":
        subprocess.Popen(['open', '-a', 'Terminal.app', serverData[selectedServer.get()]], cwd=dh.cut_to_directory(serverData[selectedServer.get()]))
        subprocess.Popen(['open', '-a', 'Terminal.app', dh.load_tunneler()], cwd=dh.cut_to_directory(dh.load_tunneler()))
    else:
        print("Unsupported operating system.")

def choose_tunneler():
    if tunnelString.get() == "Add Tunneler":
        tunneler = filedialog.askopenfilename()
        
        if check_file_compat(dh.split_directory(tunneler, -1)):
            dh.save_tunneler(tunneler)
            tunnelString.set("Remove Tunneler")
        else:
            error_message("Incorrect file type, select .bat or .sh (Check GitHub wiki if confused)")
    else:
        tunneler = ""
        dh.save_tunneler(tunneler)

        tunnelString.set("Add Tunneler")

# Main
with open(DEFAULT_SVDIR, 'a'): # Creates save file if not already there
    pass
with open(DEFAULT_TDIR, 'a'): # Creates tunneler file if not already there
    pass
serverData = dh.load_directories()
tunneler = dh.load_tunneler()
tunnelString.set(("Add Tunneler" if tunneler == "" else "Remove Tunneler"))

server_dropdown = ctk.CTkOptionMenu(master=app, width=200, variable=selectedServer, values=get_server_options())
server_dropdown.place(relx=0.7, rely=0.1, anchor=tk.CENTER)

start_server_button = ctk.CTkButton(master=app, text="Start Server", command=start_server)
start_server_button.place(relx=0.2, rely=0.1, anchor=tk.CENTER)

add_server_button = ctk.CTkButton(master=app, text="Add Server", command=add_server)
add_server_button.place(relx=0.2, rely=0.25, anchor=tk.CENTER)

remove_server_button = ctk.CTkButton(master=app, text="Remove Server", command=remove_server)
remove_server_button.place(relx=0.2, rely=0.4, anchor=tk.CENTER)

tunneler_button = ctk.CTkButton(master=app, textvariable=tunnelString, command=choose_tunneler)
tunneler_button.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

version_label = ctk.CTkLabel(master=app, text="v2.0.0")
version_label.place(relx=0.925, rely=0.95, anchor=tk.CENTER)

# End
app.mainloop()