# Server File Links
# Provides the setup wizard with server file links to download from, can be updated remotely from the github repo through requests from the wizard

paper_links = {
    "1.19.4": "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar"
}

forge_links = {
    "1.19.4": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.19.4-45.1.0/forge-1.19.4-45.1.0-installer.jar"
}

fabric_links = {

}

def get_links():
    """ Returns all links for downloading server files """
    return paper_links, forge_links, fabric_links