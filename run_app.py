import os
from pathlib import Path
import subprocess
import sys
class run_app:
    def __init__(self, usr_now, cmd):
        self.usr_now = usr_now
        self.check_aliases_path()
        self.config = {}
        self.config = self.parse_config(f'../../home/{self.usr_now}/.program_aliases')
        needed_to_launch = self.what_need_to_launch(cmd)
        self.run_app_func(needed_to_launch)
    
    def check_aliases_path(self):
        cfg_path = Path(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../../home/{self.usr_now}/.program_aliases"))
        if not cfg_path.exists():
            try:
                with open(cfg_path, "w") as f:
                    pass
            except Exception as e:
                print(f"Error in creating empty config file on path QuickPyre/home/{self.usr_now}/.program_aliases: {e}")
    
    def parse_config(self, file_path):
        self.config = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, file_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Пропускаем пустые строки и комментарии
                if not line or line.startswith('#'):
                    continue

                # Разделяем по первому знаку '='
                if '=' in line:
                    key, value = line.split('=', 1)
                    self.config.append(
                        {
                            "name": value.strip(),
                            "path": os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../../apps/{value.strip()}.py")
                        },
                    )
                    #self.config[key.strip()] = value.strip()
        #print(self.config)
        return self.config

    def what_need_to_launch(self, cmd):
        for i, file in enumerate(self.config):
            while file["name"] != cmd:
                file = self.config[self.config.index(file)+1]
            if file["name"] == cmd:
                return file["path"]
            else:
                print("This program is not installed/does not exist.")
                #print(file["name"] + "||" + file["path"])
                return None

    def run_app_func(self, path):
        if path == None:
            return
        try:
            subprocess.run([sys.executable, path])
        except Exception as e:
            print(e)

#test = run_app("root", "slowfetch")