# Server File Links

paper_links = {
    "1.20.1": "https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/60/downloads/paper-1.20.1-60.jar",
    "1.19.4": "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar",
    "1.18.2": "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar",
    "1.17.1": "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar",
    "1.16.5": "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar",
    "1.15.2": "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar",
    "1.14.4": "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar",
    "1.13.2": "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar",
    "1.12.2": "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar",
    "1.11.2": "https://api.papermc.io/v2/projects/paper/versions/1.11.2/builds/1106/downloads/paper-1.11.2-1106.jar",
    "1.10.2": "https://api.papermc.io/v2/projects/paper/versions/1.10.2/builds/918/downloads/paper-1.10.2-918.jar",
    "1.9.4": "https://api.papermc.io/v2/projects/paper/versions/1.9.4/builds/775/downloads/paper-1.9.4-775.jar",
    "1.8.8": "https://api.papermc.io/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar"
}

forge_links = {
    "1.20.1": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.1-47.0.35/forge-1.20.1-47.0.35-installer.jar",
    "1.19.4": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.19.4-45.1.0/forge-1.19.4-45.1.0-installer.jar",
    "1.18.2": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.18.2-40.2.9/forge-1.18.2-40.2.9-installer.jar",
    "1.17.1": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.17.1-37.1.1/forge-1.17.1-37.1.1-installer.jar",
    "1.16.5": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.16.5-36.2.39/forge-1.16.5-36.2.39-installer.jar",
    "1.15.2": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.15.2-31.2.57/forge-1.15.2-31.2.57-installer.jar",
    "1.14.4": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.14.4-28.2.26/forge-1.14.4-28.2.26-installer.jar",
    "1.13.2": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.13.2-25.0.223/forge-1.13.2-25.0.223-installer.jar",
    "1.12.2": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2860/forge-1.12.2-14.23.5.2860-installer.jar",
    "1.11.2": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.11.2-13.20.1.2588/forge-1.11.2-13.20.1.2588-installer.jar",
    "1.10.2": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.10.2-12.18.3.2511/forge-1.10.2-12.18.3.2511-installer.jar",
    "1.9.4": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.9.4-12.17.0.2317-1.9.4/forge-1.9.4-12.17.0.2317-1.9.4-installer.jar",
    "1.8.9": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.8.9-11.15.1.2318-1.8.9/forge-1.8.9-11.15.1.2318-1.8.9-installer.jar",
    "1.7.10": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.7.10-10.13.4.1614-1.7.10/forge-1.7.10-10.13.4.1614-1.7.10-installer.jar"
}

fabric_links = {
    "1.20.1": "https://meta.fabricmc.net/v2/versions/loader/1.20.1/0.14.21/0.11.2/server/jar",
    "1.19.4": "https://meta.fabricmc.net/v2/versions/loader/1.19.4/0.14.21/0.11.2/server/jar",
    "1.18.2": "https://meta.fabricmc.net/v2/versions/loader/1.18.2/0.14.21/0.11.2/server/jar",
    "1.17.1": "https://meta.fabricmc.net/v2/versions/loader/1.17.1/0.14.21/0.11.2/server/jar",
    "1.16.5": "https://meta.fabricmc.net/v2/versions/loader/1.16.5/0.14.21/0.11.2/server/jar",
    "1.15.2": "https://meta.fabricmc.net/v2/versions/loader/1.15.2/0.14.21/0.11.2/server/jar",
    "1.14.4": "https://meta.fabricmc.net/v2/versions/loader/1.14.4/0.14.21/0.11.2/server/jar"
}

def get_links():
    """ Returns all links for downloading server files """
    return paper_links, forge_links, fabric_links