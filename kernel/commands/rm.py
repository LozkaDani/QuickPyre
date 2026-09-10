import shutil
import os
from pathlib import Path
def rm_cmd(args):
    path = Path(os.path.abspath(" ".join(args)))
    try:
        if not path.exists():
            print("rm: path doesn't exists.")
            return
        else:
            if path.is_dir():
                shutil.rmtree(path)
                print(f"rm: Directory '{path}' removed.")
            else:
                path.unlink()
                print(f"File '{path}' removed.")
    except Exception as e:
        print(f"rm: {e}")