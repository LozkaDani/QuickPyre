from pathlib import Path
import os
from utils import write_file
def chost_cmd(hostname, args):
    #new_hostname = input("New hostname: ")
    current_dir = Path.cwd()
    if hostname == " ".join(args):
        print("New hostname can't be the same as current.")
        return
    while current_dir:
        for file in current_dir.rglob("config/hostname.quick"):
            if file.exists():
                write_to_f = write_file.write()
                write_to_f.write_to_file(os.path.abspath(file), " ".join(args))
                return
                
        if current_dir.name == "QuickPyre":
            break
        if current_dir.parent == current_dir:
            break
        current_dir = current_dir.parent