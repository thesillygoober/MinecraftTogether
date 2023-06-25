# Server Setup Wizard
# Used for setting up servers easily

# Imports
from serverfilelinks import get_links
from serverdownloader import download_server_file
import tkinter as tk
import customtkinter as ctk

# Setup
ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green") 

app = ctk.CTk()
app.title("MCT Server Setup")
app.resizable(False, False)
app.geometry("200x500")

# Variables
paper_links = {}
forge_links = {}
fabric_links = {}

# Main
paper_links, forge_links, fabric_links = get_links()

# End
app.mainloop()