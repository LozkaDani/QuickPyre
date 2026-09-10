import os
def cd_cmd(args):
        _, cur_dir = str(os.getcwd()).split("QuickPyre", 1)
        try:
            if not args:
                print("cd: missing operand")
            else:
                dir_name = args[0]
                if dir_name == "..":
                    if cur_dir != "":
                        os.chdir("..")
                    else:
                        print("No changes.")
                else:
                    os.chdir(dir_name)
        except Exception as e:
            print(f"cd: {e}")
