import requests
import random
import time
import os
from colorama import init, Fore
import datetime

init(autoreset=True)

LOGO = r"""
░██████╗░██████╗░░█████╗░██╗░░░██╗██████╗░  ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
██╔════╝░██╔══██╗██╔══██╗██║░░░██║██╔══██╗  ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
██║░░██╗░██████╔╝██║░░██║██║░░░██║██████╔╝  █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██║░░╚██╗██╔══██╗██║░░██║██║░░░██║██╔═══╝░  ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║╚█████╔╝╚██████╔╝██║░░░░░  ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░░░░  ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def check_group(group_id):
    url = f"https://groups.roblox.com/v1/groups/{group_id}"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        data = r.json()
        return {
            "id": group_id,
            "name": data.get("name", "Unknown"),
            "open": data.get("publicEntryAllowed", False),
            "members": data.get("memberCount", 0),
            "owner": data.get("owner")
        }
    except:
        return None

def format_elapsed(start_time):
    elapsed_seconds = time.time() - start_time
    hours, rem = divmod(elapsed_seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    milliseconds = (seconds % 1) * 1000
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int(milliseconds):03}"

def main():
    clear()
    print(Fore.CYAN + LOGO)
    
    min_id = int(input("Min Group ID to check: "))
    max_id = int(input("Max Group ID to check: "))
    checks = int(input("How many groups to check: "))
    delay = float(input("Delay between checks (seconds): "))
    
    save_file = input("Save found groups to found_groups.txt? (y/n): ").lower() == "y"
    
    found_groups = []
    clear()
    print(Fore.CYAN + LOGO)
    print(Fore.CYAN + f"Searching {checks} groups between IDs {min_id} - {max_id}...\n")

    found_count = 0
    start_time = time.time()

    for _ in range(checks):
        gid = random.randint(min_id, max_id)
        
        elapsed_str = format_elapsed(start_time)
        print(Fore.CYAN + f"\rChecking Group ID: {gid} | Elapsed Time: {elapsed_str}", end="")

        result = check_group(gid)
        if result and result['open'] and result['members'] == 0 and result['owner'] is None:
            print()  # Move to next line to print found group
            print(Fore.GREEN + f"[FOUND] ID: {result['id']} | {result['name']} | Members: {result['members']} | Open: {result['open']}")
            found_count += 1
            found_groups.append(result)

        time.sleep(delay)

    if save_file and found_groups:
        with open("found_groups.txt", "w", encoding="utf-8") as f:
            for g in found_groups:
                f.write(f"{g['id']} | {g['name']} | Members: {g['members']} | Open: {g['open']}\n")
        print(Fore.BLUE + f"\nSaved {len(found_groups)} groups to found_groups.txt")

    print(Fore.BLUE + f"\nDone! Found {found_count} groups matching criteria.")

if __name__ == "__main__":
    main()
