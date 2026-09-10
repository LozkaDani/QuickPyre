import sys
from pathlib import Path
import subprocess
def exec_app(path):
    if Path(path).exists():
        try:
            subprocess.run([sys.executable, path])
        except Exception as e:
            print(e)