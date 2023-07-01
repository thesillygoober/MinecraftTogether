# Server Setup Wizard

# Imports
from serverfilelinks import get_links
from serverdownloader import make_server
import tkinter as tk
import customtkinter as ctk

# Links
paper_links, forge_links, fabric_links = get_links()

def server_setup_wizard():
    # Functions
    def setup_button_switcher(val = ""):
        if eulaCheckboxVar.get() == 1 and serverTypeVar.get() != "Choose a Server Type" and serverVersionVar.get() != "Choose a Server Version":
            setup_button.configure(state=tk.NORMAL)
        else:
            setup_button.configure(state=tk.DISABLED)

    def find_link_type(val):
        if val == "Paper (Vanilla)":
            return paper_links
        elif val == "Forge":
            return forge_links
        elif val == "Fabric":
            return fabric_links

    def return_versions(val):
        selectedVersionLinks = find_link_type(val)
        returnLinks = []

        for i in selectedVersionLinks:
            returnLinks.append(i)
    
        server_version_dropdown.configure(values=returnLinks)
        serverVersionVar.set("Choose a Server Version")

    # Setup
    ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("green") 

    app = ctk.CTk()
    app.title("MCT Server Setup")
    app.resizable(False, False)
    app.geometry("300x400")

    serverTypeVar = tk.StringVar()
    serverTypeVar.set("Choose a Server Type")
    serverVersionVar = tk.StringVar()
    serverVersionVar.set("Choose a Server Version")

    eulaCheckboxVar = tk.IntVar()
    eulaCheckboxVar.set(0)

    server_type_label = ctk.CTkLabel(master=app, text="Server Type")
    server_type_label.place(relx=0.5, rely=.28, anchor=tk.CENTER)
    server_type_dropdown = ctk.CTkOptionMenu(master=app, width=250, variable=serverTypeVar, values=["Paper (Vanilla)", "Forge", "Fabric"], command=return_versions)
    server_type_dropdown.place(relx=0.5, rely=.355, anchor=tk.CENTER)

    server_version_label = ctk.CTkLabel(master=app, text="Server Version")
    server_version_label.place(relx=0.5, rely=.48, anchor=tk.CENTER)
    server_version_dropdown = ctk.CTkOptionMenu(master=app, width=250, variable=serverVersionVar, values=[], command=setup_button_switcher)
    server_version_dropdown.place(relx=0.5, rely=.555, anchor=tk.CENTER)

    server_name_label = ctk.CTkLabel(master=app, text="Server Name")
    server_name_label.place(relx=0.5, rely=.08, anchor=tk.CENTER)
    server_name_input = ctk.CTkTextbox(master=app, height=25, width=250)
    server_name_input.place(relx=0.5, rely=.155, anchor=tk.CENTER)

    eula_checkbox = ctk.CTkCheckBox(master=app, text="Click to agree to Minecraft server EULA", variable=eulaCheckboxVar, command=setup_button_switcher)
    eula_checkbox.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def call_make_server():
        selectedVersionLinks = find_link_type(serverTypeVar.get())
        make_server(selectedVersionLinks[serverVersionVar.get()], "server.jar", server_name_input.get("1.0", "end-1c"), app, serverTypeVar.get())

    setup_button = ctk.CTkButton(master=app, width=250, height=70, text="SETUP SERVER", state=tk.DISABLED, command=call_make_server)
    setup_button.place(relx=0.5, rely=0.86, anchor=tk.CENTER)

    # End
    app.mainloop()