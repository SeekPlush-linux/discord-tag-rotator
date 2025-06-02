import requests
import time
from rich import print
from datetime import datetime
import random
import json

VERSION = "v1.3.0"

with open("config.json") as f:
    config = json.load(f)

tags = config['tags']
tag_names = [name for name in tags.keys()]
tag_ids = [i for i in tags.values()]
delay = config['delay']

def change_tag(id: int, index: int):
    headers = {
        "Accept": "*/*",
        "Authorization": config['token']
    }
    payload = {
        "identity_guild_id": id,
        "identity_enabled": True
    }
    while True:
        try:
            response = requests.put("https://discord.com/api/v9/users/@me/clan", headers=headers, json=payload, timeout=10)
            break
        except requests.exceptions.Timeout:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[bright_black]{current_time}[/] [bright_red]Timed out. Retrying...[/]")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if response.status_code == 200:
        print(f"[bright_black]{current_time}[/] [bright_green]Changed to [bold]\"{tag_names[index]}\"[/].[/]")
    else:
        print(f"[bright_black]{current_time}[/] [bright_red]An error occured: Status Code {response.status_code}[/]")
        print(f"[bright_red]Content: [/] {response.content}")

print(f"[bright_cyan]Discord Server Tag Rotator {VERSION} by @SeekPlush-linux[/]")
time.sleep(1)
print("[bright_yellow]Starting...[/]")
index = random.randint(-1, len(tag_names)-2)
error_caught = False
while True:
    try:
        index += 1 if not error_caught else 0
        error_caught = False
        try:
            tag_id = tag_ids[index]
            tag_name = tag_names[index]
        except IndexError:
            index = 0
            tag_id = tag_ids[index]
            tag_name = tag_names[index]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[bright_black]{current_time}[/] [bright_yellow]Changing to [bold]\"{tag_name}\"[/]...[/]")
        change_tag(tag_id, index)
        print(f"[bright_yellow]Sleeping for {delay} seconds...[/]")
        time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[bold bright_red]Exiting...[/]")
        exit(0)
    except Exception as e:
        error_caught = True
        print(f"\n[bold red]Error:[/] {e}")
        print("[bold bright_red]Retrying in 5 seconds...[/]")
        time.sleep(5)
