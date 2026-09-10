from pathlib import Path
def cat_cmd(parts):
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