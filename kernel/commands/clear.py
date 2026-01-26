import os
def clear_cmd(): 
    if os.name == "nt": #Windows
        os.system("cls")
    elif os.name == "posix": #Unix-like systems
        os.system("clear")