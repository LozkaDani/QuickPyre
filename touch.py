import os
from pathlib import Path
def touch_cmd(args):
    path = Path(os.path.abspath(" ".join(args)))
    try:
        if not path.exists():
            with open(path, "w") as f:
                f.write("")
        else:
            print(f"touch: {path} currently exists.")
            return
    except Exception as e:
        print(f"touch: {e}")