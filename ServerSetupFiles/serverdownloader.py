# Server Downloader
# When called from the server setup wizard, it will download the file from the given link

# Imports
import requests
from requests.exceptions import ConnectionError

# Functions
def download_server_file(link: str, outputPath: str):
    """ Downloads a server file from a link """
    pass