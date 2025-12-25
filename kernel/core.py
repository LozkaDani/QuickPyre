import time
import os
import users
from pathlib import Path
import sys
from datetime import date
import datetime
import asyncio
import subprocess
# Add the path to the directory where the apps folder is located.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Теперь можно импортировать
from apps import slowfetch
# ПЕРЕМЕННЫЕ, VARIABLES


hostname = ""
usr_now = ""
sf = None
ver = ""
# ФУНКЦИИ, FUNCTIONS

def _load_version():
    global ver
    core_dir = os.path.dirname(os.path.abspath(__file__))
    configs_path = os.path.join(core_dir, "../config/version.quick")
    with open(configs_path, "r") as f:
        ver = f.readline()


def hostname_load():
    global hostname
    path_to_core = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(path_to_core, "../config/hostname.quick")

    with open(full_path, "r") as f:
        hostname = f.readline()

def write_to_file(path, text):   # Пример: запись нового хоста, т.е в chost_cmd() вызваем write_to_file(config/hostname.quick, hostname)
    path_to_core = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(path_to_core, "../" + path)

    with open(full_path, "w") as f:
        f.write(text)

def commands_check(cmd):
    global ver
    # Spliting command on command and args
    parts = cmd.split()
    if not parts:
        return

    cmdd = parts[0]
    args = parts[1:] if len(parts) > 1 else []

    if cmdd == "shutdown":
        shutdown_cmd()
    elif cmdd == "startde":
        asyncio.run(startde())
    elif cmdd == "help":
        help_cmd()
    elif cmdd == "chost":
        chost_cmd()
    elif cmdd == "dsserv":
        print("https://discord.gg/N53NPRrkXU --- Yumalaya")
    elif cmdd == "slowfetch":
        fetch = slowfetch.slowfetch_class()
    elif cmdd == "muskat":
        print("Also try MuskatOS!")
    elif cmdd == "echo":
        echo_cmd(args)
    elif cmdd == "whoami":
        print(usr_now)
    elif cmdd == "pwd" or cmdd == "whereami":
        _, cur_dir = str(os.getcwd()).split("QuickPyre", 1)
        if cur_dir == "":
            print("You are at: /")
        else:
            print(f"You are at: {cur_dir}")
        #print(f"You are at: {os.getcwd()}")
    elif cmdd == "version":
        print(ver)
    elif cmdd == "ls":
        ls_cmd()
    elif cmdd == "cd":
        cd_cmd(args)
    elif cmdd == "date":
        print(str(date.today())+" yy/mm/dd format")
    elif cmdd == "time":
        current_date_time = datetime.datetime.now()
        current_time = datetime.datetime.now().time()
        print(current_time)
    else:
        print(f"{cmdd}: command not found.")

async def startde():
    current_dir = Path(".")
    path_to_de_dir = os.path.join(current_dir, "../de/")
    script_path = os.path.join(path_to_de_dir, "quickwindow.py")
    what_os = os.name
    if what_os == "nt": #For windows, but, all code is NOT optimized for Windows
        subprocess.Popen(subprocess.run(["python", script_path]))
    if what_os == "posix": #Unix-like systems.
        subprocess.Popen(
        ["python", script_path],
        start_new_session=True  #For Unix: creates new session
    )

def cd_cmd(args):
    _, cur_dir = str(os.getcwd()).split("QuickPyre", 1)
    try:
        if not args:
            print("cd: missing operand")
        else:
            dir_name = args[0]
            if dir_name == "..":
                if cur_dir != "":
                    os.chdir("..")
                else:
                    print("No changes.")
            else:
                os.chdir(dir_name)
    except Exception as e:
        print(f"cd: {e}")
def ls_cmd(): 
    current_dir = Path(".")
    items = list(current_dir.iterdir()) #list of items in dir
    for item in items:
        print(item)

def echo_cmd(args):
    print(" ".join(args))

def help_cmd(): # help list
    print("="*10 + "BASE CMDS" + "="*10)
    print("shutdown ---> off system.")
    print("help ---> this command, list of commands.")
    print("chost ---> change hostname.")
    print("echo ---> displays text on the screen, echo hello, world!")
    print("pwd, whereami ---> displays where you are.")
    print("whoami ---> displays current user.")
    print("version ---> displays the system version.")
    print("ls ---> list of files or dirs in dir, where is an user.")
    print("cd ---> change directory.")
    print("date ---> displays current date.")
    print("time ---> displays current time.")

    print("startde ---> start DE (de is not completed)")
    print("="*10 + "APPS" + "="*10 )
    print("slowfetch ---> fastfetch analog.")

def shutdown_cmd():
    print("Checking errors...")
    time.sleep(1)
    print("Turning off system parts...")
    time.sleep(2)
    print("Shutdowning system...")
    time.sleep(3)
    exit()


def chost_cmd():
    global hostname
    new_hostname = input("New hostname: ")
    if hostname == new_hostname:
        print("New hostname can't be the same as current.")
        return
    else:
        hostname = new_hostname
        write_to_file("config/hostname.quick", hostname)    

def update(): # update the invitation, system, etc. after executing the command
    hostname_load()

def login_konsole():
    global usr_now
    usrname =  input("Username: ")
    password = input("Password: ")

    user = users.User(usrname, password)
    if user.login() == False: # If an error occurs when logging in, try logging in again.
        login_konsole()
    else:
        usr_now = usrname
    update()

def registration():
    usrname =  input("Username: ")
    password = input("Password: ")
    is_root = input("Is root?(y/n): ")
    if is_root.lower() == "y":
        is_root = True
    else:
        is_root = False
    user = users.User(usrname, password, is_root)
    user.registration()
    update()

def want_reg():
    usr_choice = input("Do you want to register new user? (y/n): ")
    if usr_choice.lower() == "y":
        registration()
        update()
    else:
        update()
# ВЫЗОВЫ ФУНКЦИЙ И Т.Д
print("\n"*65)
hostname_load()
_load_version()
want_reg()
login_konsole()

while True:
    command = input(f"{usr_now}@{hostname}: ")
    commands_check(command)
    update()