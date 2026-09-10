import time
import os
import users
from pathlib import Path
import sys
from datetime import date
import datetime
import subprocess
from utils import write_file, colors, autostart
from users import User
from commands import echo, clear, chost, cd, cat, help, time, date, shutdown, ls, calendar, pwd, whoami, version, rm, touch, history, clear_history, quick, su, exec_app, run_app

class Kernel:
    def __init__(self):
        self.core_path = os.path.dirname(os.path.abspath(__file__))
        self.version = self._load_version(self.core_path)
        self.hostname = self._load_hostname()
        self.kernel_vers = "QuickKernel v. 3.0"
        self.usr_now = None
        self.history_path = os.path.join(os.path.dirname(__file__), "../config/history.quickhist")
    
    def autostart_after_login(self):
        """Просто запускаем все файлы, прописанные в .kvalxarc(home/username/)"""
        autostart.autostart(self.usr_now)

    def _load_hostname(self):
        """Загружаем хостнейм, чтобы изменять или просто показывать его в консоли в будущем."""
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
                
    def load_program_aliases(self):
        """загрузка алиасов для программ, пока не используется"""
        kernel_path = os.path.abspath(__file__)
        apps_dir_path = Path(os.path.join(kernel_path, "../apps/"))
        all_programs = apps_dir_path.iterdir()
    
    def _load_version(self, core_path):
        """Загружаем версию системы(?)"""
        configs_path = os.path.join(core_path, "../config/version.quick")
        with open(configs_path, "r") as f:
            version = f.readline().strip()
        return version
    
    def save_cmd_history(self, cmd):
        """Сохраняем историю команд"""
        try:
            with open(self.history_path, "a") as f:
                hours_mins_seconds_mseconds = datetime.datetime.now().time()
                hours_mins_seconds, mseconds = str(hours_mins_seconds_mseconds).split(".", 1)
                hours, mins_seconds = str(hours_mins_seconds).split(":", 1)
                mins, seconds = str(mins_seconds).split(":", 1)
                f.write(f"{str(datetime.date.today()).replace("-", ".")} {hours}:{mins} | {cmd}\n")
        except Exception as e:
            print(f"Error saving command history: {e}")
    def check_cmd(self, user_input: str) -> None:
        """Проверяем команду на существование."""
        #spliting command on command and args
        parts = user_input.split()
        if not parts:
            return
        #print(parts)
        #print(user_input)
        flags = []
        cmd = parts[0]
        args = parts[1:] if len(parts) > 1 else []
        try:
            if args[0].startswith("-") or args[0].startswith("--"):
                #print(args[0])
                flags = args[0]
                args.remove(args[0])
                #print(args)
                #print(flags)
        except Exception:
            pass
        
        self.save_cmd_history(user_input)
        if cmd == "shutdown":
            shutdown.shutdown_cmd()
        elif cmd == "quick":
            manager = quick.QuickManager(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../apps/"), self.usr_now)
            #print(os.path.join(os.path.abspath(os.path.dirname(__file__))), "/../apps/")
            if "-S" in flags:
                manager.download_required_files(" ".join(args))
            elif "-R" in flags:
                manager.remove_files(" ".join(args))
            elif "-s" or "--search" in flags:
                manager.display_apps_info()
            
            else:
                print("quick: missing flag.")
        elif cmd == "help":
            help.help_cmd()
        elif cmd == "chost":
            chost.chost_cmd(self.hostname, args)
            self.hostname = self._load_hostname()
        elif cmd == "muskat": #пасхалочк
            print("Also try MuskatOS!")
        elif cmd == "echo":
            cmd_without_echo = " ".join(args)
            echo.echo_cmd(args, cmd_without_echo)
        elif cmd == "whoami":
            whoami.whoami(self.usr_now)
        elif cmd == "pwd" or cmd == "whereami":
            pwd.pwd()
        elif cmd == "version":
            version.version(self.version)
        elif cmd == "ls":
            ls.ls_cmd(flags)
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
        elif cmd == "rm":
            rm.rm_cmd(args)
        elif cmd == "touch":
            touch.touch_cmd(args)
        elif cmd == "history":
            history.history_cmd(self.history_path, colors)
        elif cmd == "clear_history":
            clear_history.clear_history_cmd(self.history_path)
        elif cmd == "su":
            self.usr_now = su.su_cmd(args, User, self.usr_now)
        else:
            """Если не ввод не команда - проверяем, программа это или нет."""
            if Path(os.path.join(os.path.dirname(os.path.abspath(__file__))), f"../apps/{cmd}.py").exists():
                try:
                    run_app.run_app(self.usr_now, cmd)
                except Exception as e:
                    print(f"Error: {e}")
            elif Path(user_input).exists():
                try:
                    exec_app.exec_app(user_input)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print(f"{cmd}: command not found.")