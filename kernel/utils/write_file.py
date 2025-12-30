import os
from pathlib import Path
class write:
    def __init__(self):
        pass
    
    def write_to_file(self, path, text):   # Пример: запись нового хоста, т.е в chost_cmd() вызваем write_to_file(config/hostname.quick, hostname)
        cur_dir = Path.cwd()
        full_path = os.path.join(cur_dir, path)

        with open(full_path, "w") as f:
            f.write(text)