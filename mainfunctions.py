# Main Functions

# Rewritten for the GUI/Text based clients to work off the same code instead of being split up
# Slightly different than the original text code to fix bad things and to avoid print functions for GUI.

# Imports
import os
from os import system, startfile as sf
import tkinter as tk
from tkinter import filedialog
from time import sleep as wait
import sys

# SQLite
import sqlite3 as sql
databaseCon = sql.connect("serverdata.db")
dbCursor = databaseCon.cursor()

# Functions
def getVersion():
    return "v1.1.2" # Current Version

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