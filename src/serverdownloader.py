# Server File Downloader

# Imports
import requests
import threading
from requests.exceptions import ConnectionError
import tkinter as tk
import customtkinter as ctk
import os
import platform
from time import sleep as wait

# Functions
def make_server(url: str, outputPath: str, serverName: str, win: ctk.CTk, type: str):
    """ Downloads a server file from a link """

    # Setup
    ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("green") 

    app = ctk.CTkToplevel(win)
    app.title("MCT Downloader")
    app.resizable(False, False)
    app.geometry("200x100")

    progress = tk.DoubleVar()

    progress_bar = ctk.CTkProgressBar(master=app, width=150, variable=progress)
    progress_bar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    progress_label = ctk.CTkLabel(master=app, text="Downloading Server File")
    progress_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    svdir = open("svdir.txt", 'r+')

    # Downloader and stuff (i suck at coding)
    def download_server_file():
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0

        os.mkdir(serverName)
        serverPath = f"{serverName}/"

        with open(f"{serverPath}{outputPath}", 'wb') as file:
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                downloaded_size += len(data)
                progress.set(float((downloaded_size / total_size)))

        progress_label.configure(text="Setting Up Server")
        progress.set(0.0)

        current_os = platform.system()
        extForOS = "bat"
        startFileDir = ""

        if current_os == "Linux" or current_os == "Darwin":
            extForOS = "sh"

        wait(0.1)
        if type == "Forge":
            with open(f"{serverPath}server.jar") as file:
                os.chdir(os.path.dirname(file.name))
                os.system(f"java -jar server.jar --installServer")
                startFileDir = os.path.abspath(file.name)  
            
            with open("eula.txt", 'w') as file:
                file.write("eula=true")
        elif type != "Forge":
            with open(f"{serverPath}run.{extForOS}", 'a') as file:
                os.system(f"chmod +x {os.path.abspath(file.name)}")
                startFileDir = os.path.abspath(file.name)
            
            with open(f"{serverPath}run.{extForOS}", 'w') as file:
                file.writelines(["#! /bin/bash\n", "java -Xmx4G -jar server.jar nogui"])

            with open(f"{serverPath}eula.txt", 'w') as file:
                file.write("eula=true")
        

        directories = {}

        for line in svdir:
            name, path = line.strip().split(',')
            directories[name] = path
        
        directories[serverName] = startFileDir
        
        for name, path in directories.items():
            svdir.write(f"{name},{path}\n")

        svdir.close()
        
        progress.set(1.0)
        progress_label.configure(text="Server done, added to list")


    downloader_thread = threading.Thread(target=download_server_file)
    downloader_thread.start()
    app.mainloop()
    downloader_thread.join()
        