import tkinter as tk
from tkinter import ttk
import requests
import time
from requests.exceptions import ConnectionError

def download_minecraft_server(output_path): # Currently doesn't work with main file, make it work
    url = "https://piston-data.mojang.com/v1/objects/84194a2f286ef7c14ed7ce0090dba59902951553/server.jar"

    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))

        with open(output_path, "wb") as f:
            chunk_size = 1024
            downloaded_size = 0
            start_time = time.time()

            progress_bar["maximum"] = total_size

            for data in response.iter_content(chunk_size):
                downloaded_size += len(data)
                f.write(data)
                progress_bar["value"] = downloaded_size
                speed = downloaded_size / (time.time() - start_time)
                speed_label["text"] = f"Download Speed: {speed / (1024 * 1024):.2f} MB/s"
                root.update_idletasks()

        print("Minecraft server downloaded successfully.")

    except ConnectionError:
        print("Connection error occurred. Failed to download Minecraft server.")

root = tk.Tk()
root.title("Minecraft Server Downloader")

progress_bar = ttk.Progressbar(root, mode="determinate")
progress_bar.pack(pady=10)

speed_label = ttk.Label(root, text="Download Speed: 0 MB/s")
speed_label.pack()

output_path = "minecraft_server.jar"

download_minecraft_server(output_path)

root.mainloop()