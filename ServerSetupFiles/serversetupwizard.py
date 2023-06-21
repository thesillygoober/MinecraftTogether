# Server Setup Wizard
# Used for setting up servers easily

# Imports
from serverfilelinks import get_links
from serverdownloader import download_server_file

# Variables
paper_links = {}
forge_links = {}
fabric_links = {}

# Main
paper_links, forge_links, fabric_links = get_links()