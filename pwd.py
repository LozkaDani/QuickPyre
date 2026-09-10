import os
def pwd():
    _, cur_dir = str(os.getcwd()).split("QuickPyre", 1)
    if cur_dir == "":
        print("You are at: /")
    else:
        print(f"You are at: {cur_dir}")