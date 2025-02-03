import os
import requests
import uuid
import random
import time
import threading
import json
from datetime import datetime

# Setup Directories and Files
folder_name = "/sdcard/Aqua"
file_names = ["toka.txt", "tokaid.txt", "tokp.txt", "tokpid.txt", "cok.txt", "cokid.txt"]

if not os.path.exists(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")
    except Exception as e:
        print(f"Failed to create folder '{folder_name}': {e}")
else:
    print(f"Folder '{folder_name}' already exists.")

for file_name in file_names:
    file_path = os.path.join(folder_name, file_name)
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                pass
            print(f"File '{file_path}' created.")
        except Exception as e:
            print(f"Failed to create file '{file_path}': {e}")
    else:
        print(f"File '{file_path}' already exists.")

# Logo & Colors
logo = '''
\033[1;96m   ╔═╗╔═╗ ╦ ╦╔═╗  ╔╗ ╔═╗╔═╗╔═╗╔╦╗
\033[1;96m   ╠═╣║═╬╗║ ║╠═╣  ╠╩╗║ ║║ ║╚═╗ ║
\033[1;97m   ╩ ╩╚═╝╚╚═╝╩ ╩  ╚═╝╚═╝╚═╝╚═╝ ╩  {c}「{red}v•1{c}」{r}
'''
red = '\033[1;91m'
blue = '\033[1;94m'
cyan = '\033[1;96m'
c = '\033[1;96m'
w = '\033[1;97m'
reset = '\033[0m'

def linex():
    print(f'  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def clear():
    os.system('clear')
    print(logo)

# Get User Info and Setup
def setup_user_data():
    os.makedirs("data", exist_ok=True)
    create_file_if_not_exists("data/nameaq.xml")
    create_file_if_not_exists("data/passwordaq.xml")

def create_file_if_not_exists(file_path):
    if not os.path.exists(file_path):
        open(file_path, "w").close()

def get_user_input(file_path, prompt_message):
    if os.path.getsize(file_path) > 0:
        with open(file_path, "r") as file_obj:
            return file_obj.readline().strip()
    else:
        user_input = input(prompt_message)
        with open(file_path, "w") as file_obj:
            file_obj.write(user_input)
        return user_input

clear()
uname = get_user_input("data/nameaq.xml", f"Enter your name: ")
upass = get_user_input("data/passwordaq.xml", f"Enter your password: ")

setup_user_data()

# Greet User
def greet_user():
    current_time = datetime.now()
    if current_time.hour < 12:
        print(f"Good morning, {c}{uname}!")
    elif current_time.hour < 18:
        print(f"Good afternoon, {c}{uname}!")
    else:
        print(f"Good evening, {c}{uname}!")

# Main Menu
def menu():
    left_options = [("1", f"START{r}"), ("2", f"REACT"), ("3", f"CREATE PAGE"), ("0", f"{red}EXIT{r}")]
    right_options = [("4", f"FOLLOW"), ("5", f"COMMENT"), ("6", f"SHARE"), ("7", f"RESET")]

    for (left_option, left_desc), (right_option, right_desc) in zip(left_options, right_options):
        print(f"{c}   「{r}{left_option}{c}」{r} {left_desc:<14}     {c}  「{r}{right_option}{c}」{r} {right_desc}")
    linex()
    choice = input(f'Choose an option: ')

    menu_actions = {
        '1': lambda: print("Starting..."),
        '2': lambda: print("Reacting..."),
        '3': lambda: print("Creating Page..."),
        '4': lambda: print(f"Before following get token first."),
        '5': lambda: print("Commenting..."),
        '6': lambda: print("Sharing..."),
        '7': lambda: print("Resetting..."),
        '0': lambda: print('Done logging out.') or exit()
    }
    menu_actions.get(choice, lambda: print('Invalid option.'))()

# Run the script
clear()
greet_user()
menu()
