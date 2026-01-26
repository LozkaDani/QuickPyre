import time
import os
import users
from pathlib import Path
import sys
from datetime import date
import datetime
import subprocess
from utils import write_file
from commands import echo, clear, chost, cd, cat, help, time, date, shutdown, ls, calendar, pwd, whoami, version
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
        self.kernel_vers = "QuickKernel v. 1.4.0"
        self.usr_now = None

    def _load_hostname(self):
        cur_dir = Path.cwd()
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
                

    
    def _load_version(self, core_path):
        configs_path = os.path.join(core_path, "../config/version.quick")
        with open(configs_path, "r") as f:
            version = f.readline().strip()
        return version
    
    def check_cmd(self, user_input):
        #spliting command on command and args
        parts = user_input.split()
        if not parts:
            return

        cmd = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        if cmd == "shutdown":
            shutdown.shutdown_cmd()
        elif cmd == "help":
            help.help_cmd()
        elif cmd == "chost":
            chost.chost_cmd(self.hostname, args)
            self.hostname = self._load_hostname()
        elif cmd == "slowfetch":
            fetch = slowfetch.slowfetch_class()
        elif cmd == "muskat": #пасхалочк
            print("Also try MuskatOS!")
        elif cmd == "echo":
            echo.echo_cmd(args)
        elif cmd == "whoami":
            whoami.whoami(self.usr_now)
        elif cmd == "pwd" or cmd == "whereami":
            pwd.pwd()
        elif cmd == "version":
            version.version(self.version)
        elif cmd == "ls":
            ls.ls_cmd()
        elif cmd == "cd":
            cd.cd_cmd(args)
        elif cmd == "date":
            date.date_cmd()
        elif cmd == "time":
            time.time_cmd()
        elif cmd == "clear":
            clear.clear_cmd()
        elif cmd == "cat":
            if len(parts) < 2:
                print("cat: missing operand")
                return
            cat.cat_cmd(parts)
        elif cmd == "calendar":
            calendar.calendar_cmd()
        else:
            print(f"{cmd}: command not found.")
        


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
