#! /usr/bin/python

# Imports
import tkinter as tk
import customtkinter as ctk
from customtkinter import filedialog
import platform
from os import system as callc # call command

# SQLite
import sqlite3 as sql
database_connection = sql.connect("serverdata.db")
database_cursor = database_connection.cursor()

# Setup
ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green") 

app = ctk.CTk()
app.title("MinecraftTogether")
app.resizable(False, False)
app.geometry("400x240")

selectedServer = tk.StringVar(app)
selectedServer.set("Choose a Server")
serverOptions = []
fileDirectories = []

current_os = platform.system()

# Functions
def cut_directory(directory, cut):
    return str.split(directory, "/")[cut]

def error_message(msg):
    error_window = ctk.CTk()
    error_window.title("MCT Error")
    error_window.resizable(False, False)
    error_window.geometry("200x120")

    error_label = ctk.CTkLabel(master=error_window, text="Error: " + msg, wraplength=200)
    error_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def add_server():
    fdResult = filedialog.askopenfilename()
    fileName = cut_directory(fdResult, -1)
    serverName = cut_directory(fdResult, -2)

    if (fileName.split(".")[-1] == "bat" and current_os == "Windows") or (fileName.split(".")[-1] == "sh" and (current_os == "Linux" or current_os == "Darwin")) and not serverName in serverOptions:
        serverOptions.append(serverName)
        fileDirectories.append(fdResult)
        server_dropdown = ctk.CTkOptionMenu(master=app, width=200, variable=selectedServer, values=serverOptions)
        server_dropdown.place_forget()
        server_dropdown.place(relx=0.7, rely=0.1, anchor=tk.CENTER)
    elif serverName in serverOptions and (fileName.split(".")[-1] == "bat" and current_os == "Windows") or (fileName.split(".")[-1] == "sh" and (current_os == "Linux" or current_os == "Darwin")):
        error_message("Server already exists")
    else:
        error_message("Incorrect file type, select .bat or .sh")
    
def remove_server():
    firstIndex = serverOptions.index(selectedServer.get())
    serverOptions.pop(firstIndex)
    fileDirectories.pop(firstIndex)
    selectedServer.set("Choose a Server")

def start_server():
    callc(fileDirectories[serverOptions.index(selectedServer.get())])

# Main
server_dropdown = ctk.CTkOptionMenu(master=app, width=200, variable=selectedServer, values=serverOptions)
server_dropdown.place(relx=0.7, rely=0.1, anchor=tk.CENTER)

start_server_button = ctk.CTkButton(master=app, text="Start Server", command=start_server)
start_server_button.place(relx=0.2, rely=0.1, anchor=tk.CENTER)

add_server_button = ctk.CTkButton(master=app, text="Add Server", command=add_server)
add_server_button.place(relx=0.2, rely=0.25, anchor=tk.CENTER)

remove_server_button = ctk.CTkButton(master=app, text="Remove Server", command=remove_server)
remove_server_button.place(relx=0.2, rely=0.4, anchor=tk.CENTER)

tunneler_button = ctk.CTkButton(master=app, text="Tunneler")
tunneler_button.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

version_label = ctk.CTkLabel(master=app, text="v2.0.0")
version_label.place(relx=0.925, rely=0.95, anchor=tk.CENTER)

# End
app.mainloop()
