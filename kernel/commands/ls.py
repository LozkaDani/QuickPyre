from pathlib import Path
def ls_cmd(): 
    current_dir = Path(".")
    items = list(current_dir.iterdir()) #list of items in dir
    for item in items:
        print(f"{item} DIR") if item.is_dir() else print(f"{item} {item.suffix.upper()}")