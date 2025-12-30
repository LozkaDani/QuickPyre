import time
import os
import users
from pathlib import Path
import sys
from datetime import date
import datetime
import asyncio
import subprocess
from utils import write_file
#import rglob

# Add the path to the directory where the apps folder is located.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from apps import slowfetch
except ImportError as ie:
    print(f"Failed to import slowfetch: {ie}")

class Kernel:
    def __init__(self):
        self.core_path = os.path.dirname(os.path.abspath(__file__))
        self.version = self._load_version(self.core_path)
        self.hostname = self._load_hostname()
        self.kernel_vers = "QuickKernel v. 0.5.7"
        self.usr_now = None

    def _load_hostname(self):
        cur_dir = Path.cwd()
        #full_path = os.path.join(cur_dir, "../config/hostname.quick")
        while cur_dir:
            for file in cur_dir.rglob("config/hostname.quick"):
                if file.exists():
                    with open(file, "r") as f:
                        hostname = f.readline().strip()
                        #print(hostname)
                    return hostname
            if cur_dir == "QuickPyre":
                break

            if cur_dir.parent == cur_dir:
                break
            cur_dir = cur_dir.parent
        print("ERROR: No hostname.quick file. Can't save hostname...")                
                

    
    def _load_version(self, corep):
        configs_path = os.path.join(corep, "../config/version.quick")
        with open(configs_path, "r") as f:
            version = f.readline().strip()
        return version
    
    def check_cmd(self, input):
        # Spliting command on command and args
        parts = input.split()
        if not parts:
            return

        cmd = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        if cmd == "shutdown":
            self.shutdown_cmd()
        elif cmd == "startde":
            asyncio.run(self.startde())
        elif cmd == "help":
            self.help_cmd()
        elif cmd == "chost":
            self.chost_cmd()
        elif cmd == "dsserv":
            print("https://discord.gg/N53NPRrkXU --- Yumalaya")
        elif cmd == "slowfetch":
            fetch = slowfetch.slowfetch_class()
        elif cmd == "muskat":
            print("Also try MuskatOS!")
        elif cmd == "echo":
            self.echo_cmd(args)
        elif cmd == "whoami":
            print(self.usr_now)
        elif cmd == "pwd" or cmd == "whereami":
            _, cur_dir = str(os.getcwd()).split("QuickPyre", 1)
            if cur_dir == "":
                print("You are at: /")
            else:
                print(f"You are at: {cur_dir}")
            #print(f"You are at: {os.getcwd()}")
        elif cmd == "version":
            print(self.version)
        elif cmd == "ls":
            self.ls_cmd()
        elif cmd == "cd":
            self.cd_cmd(args)
        elif cmd == "date":
            print(str(date.today())+" yy/mm/dd format")
        elif cmd == "time":
            current_date_time = datetime.datetime.now()
            current_time = datetime.datetime.now().time()
            print(current_time)
        elif cmd == "clear":
            if os.name == "nt": #Windows
                print(" "*100)
            elif os.name == "posix": #Unix-like systems
                os.system("clear")
        elif cmd == "cat":
            if len(parts) < 2:
                print("cat: missing operand")
                return
            self.cat_cmd(parts)
        else:
            print(f"{cmd}: command not found.")
        
    def cat_cmd(self, parts):
        filename = " ".join(parts[1:])
        filepath = Path(filename)

        if not filepath.exists():
            print(f"cat: {filename}: No such file or directory")
            return

        if filepath.is_dir():
            print(f"cat: {filename}: Is a directory")
            return
        
        try:
            with open(filepath, "r") as f:
                content = f.read()
                print(content)
        except Exception as e:
            print(f"cat: error reading file: {e}")

    async def startde(self):
        current_dir = Path.cwd()
    
        #ищем файл, поднимаясь вверх по директориям
        while current_dir:
            #ищем в папке и подпапках где щас программа de/quickwindow.py

            for file in current_dir.rglob("de/quickwindow.py"):
                if file.exists():
                    #файл найден -- запускаем
                    if os.name == "nt":
                        subprocess.Popen(["python", str(file)])
                    else:
                        subprocess.Popen(["python", str(file)], start_new_session=True)
                    return
            
            #если папка щас это папка проекта, а de не найден: 
            if current_dir.name == "QuickPyre":
                break
            
            
            if current_dir.parent == current_dir:  #если программа уже в корне: выводим что файла нет.
                break
            
            current_dir = current_dir.parent #идем на папку выше
        
        print("startde: failed to find QuickWindow")

    def chost_cmd(self):
        new_hostname = input("New hostname: ")
        current_dir = Path.cwd()
        if self.hostname == new_hostname:
            print("New hostname can't be the same as current.")
            return
        while current_dir:
            self.hostname = new_hostname.strip()
            for file in current_dir.rglob("config/hostname.quick"):
                if file.exists():
                    write_to_f = write_file.write()
                    write_to_f.write_to_file(os.path.abspath(file), self.hostname)
                    return
                
            if current_dir.name == "QuickPyre":
                break
            if current_dir.parent == current_dir:
                break
            current_dir = current_dir.parent
        self.hostname = self._load_hostname()

    def update(self): # update the invitation, system, etc. after executing the command
        hostname_load()



    def help_cmd(self): # help list
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
        print("clear ---> clears terminal.")
        print("cat ---> displays text from file.")

        print("startde ---> start DE (de is not completed)")
        print("="*10 + "APPS" + "="*10 )
        print("slowfetch ---> fastfetch analog.")

    def shutdown_cmd(self):
        print("Checking errors...")
        time.sleep(1)
        print("Turning off system parts...")
        time.sleep(2)
        print("Shutdowning system...")
        time.sleep(3)
        exit()


    def cd_cmd(self, args):
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
    def ls_cmd(self): 
        current_dir = Path(".")
        items = list(current_dir.iterdir()) #list of items in dir
        for item in items:
            print(item)

    def echo_cmd(self, args):
        print(" ".join(args))

        


# kernel = Kernel()
# kernel.check_cmd("date")
# kernel.check_cmd("time")
# kernel.check_cmd("version")
# kernel.check_cmd("pwd")
# kernel.check_cmd("help")
# kernel.check_cmd("echo hey world")
# kernel.check_cmd("startde")
# kernel.check_cmd("cd utils")
# kernel.check_cmd("ls")
# kernel.check_cmd("chost")
# kernel.check_cmd("shutdown")