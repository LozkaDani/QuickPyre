#Наконец-то разделяю ядро и shell
import os
import getpass
from users import User
from utils.colors import Colors
try:
    from kernel import Kernel
except ImportError as ie:
    print("ERROR: CAN'T IMPORT KERNEL. {ie}")
    exit(1)

kernel = Kernel()


usr_now = kernel.usr_now
hostname = kernel.hostname
shell_vers = "KvalxaShell v. 1.2.4"
kernel.shell = shell_vers

def on_start():
    print("           . ..:.")
    print("           .+@..+.")
    print("           ++# ***..")
    print("         ..*.:*...:.")
    print("          -:.+:-+.::")
    print("      =   %++%*++=+.:")
    print("      =-... @*=-=+*#@+.")
    print("     %.-=*:-=@@@@@@@%*==.")
    print("    -#**%:*@         @*-=.")
    print("  .-+-====@  @@   .   #...*--")
    print("  --=.+@@@@@%::@:     @@@@%*..")
    print(" .=#%@@          :::: @    @+-.")
    print(".:#*=@  -  .....      @ ::  @=*.")
    print(" =#++@        .. .. @@      @:+-")
    print(".+.=+@ :+: @@ :.-:.       : @+- .")
    print(" -*@+@   . @  :   ..... -   *--.")
    print(" .:*%%@@   @  ..:         @@@*..")
    print("   .:+#-@@@@ ---::.   @@@@@-.")
    print("    .-*%@%*@  :. = @  @@@+:.")
    print("        =**@@       @@@..")
    print("         .:-*@@@@@@%-")
    print("             =:....=")


    print(f"\n\nKernel: {kernel.kernel_vers}")
    print(f"Shell: {shell_vers}\n")

    print(
        f"{Colors.CYAN}██{Colors.BLUE}██{Colors.PURPLE}██"
        f"{Colors.GREEN}██{Colors.YELLOW}██{Colors.RED}██"
        f"{Colors.END}\n"
    )

def update(): # обновляем хост, юзернейм и т.д
    global hostname, usr_now
    kernel.hostname = kernel._load_hostname()
    hostname = kernel.hostname
    usr_now = kernel.usr_now

def login_konsole():
    global usr_now
    login = input("Login: ")
    password = getpass.getpass("Password: ") #getpass не показывает даже звездочками введенные символы.

    user = User(login, password, False)
    if user.login() == False:
        login_konsole()
    else:
        usr_now = login
        kernel.usr_now = usr_now
        kernel.is_loginned = 1
        kernel.autostart_after_login()
    update()

def registration():
    while True:
        login = input("Login: ")
        password = getpass.getpass("Password: ")

        user = User(login, password, False)
        if login == "" or password == "":
            print("Invalid input. Login or password can't be empty.")
        else:    
            if user.registration() == False:
                pass
            else:
                update()
                break

def want_reg():
    while True:
        usr_choice = input("Do you want to register new user? (y/n)(s for turn off system): ")
        if usr_choice.lower() == "y":
            registration()
            update()
            break
        elif usr_choice.lower() == "n":
            update()
            break
        elif usr_choice.lower() == "s":
            exit()
        else:
            print("Invalid input. Please enter 'y', 'n' or 's'.")

on_start()
want_reg()
login_konsole()
kernel.save_cmd_history(f"User {usr_now} has logged in successfully.")

while True:
    try:
        if os.name != "nt":
            _, path = str(os.getcwd()).split("QuickPyre", 1)
            if path == "":
                path = "/"
            color_usr = f"{Colors.GREEN}{usr_now}{Colors.END}"   #разукрашиваем юзернейм и хостнейм
            color_host = f"{Colors.BLUE}{hostname}{Colors.END}"
            cmd = input(f"{color_usr}@{color_host} {path}: ")
        else:
            cmd = input(f"{usr_now}@{hostname} {path}: ")
        #if cmd == "shut": #FOR DEBUG: fast shutdown
        #    exit()
        kernel.check_cmd(cmd) #проверяем и выполняем команду
        update()
    except KeyboardInterrupt as ki:
        print("")
        continue

#Also try MuskatOS!