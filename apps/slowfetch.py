import os

class Colors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    END = "\033[0m"

class slowfetch_class:
    def __init__(self):
        self.OS_NAME=""
        self.DE=""
        self.VERSION=""
        self.config = {}
        self.config = self.parse_config('../config/slowfetch.cfg')
        self.uptime = self.get_uptime()
        self.slowfetch_out()

    def get_uptime(self):
        try:
            with open('/proc/uptime') as f:
                uptime = float(f.readline().split()[0])
                hrs = int(uptime // 3600)
                mins = int((uptime % 3600) // 60)
                return f"{hrs}h {mins}m"
        except:
            return "Unknown"
    
    def parse_config(self, file_path):
        self.config = {}
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, file_path)
        if not os.path.exists(full_path):
            print("ERROR: NO slowfetch.cfg FILE")
            #print("DOWNLOAD IT WITH: unbound -S slowfetch.cfg")

        with open(full_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Пропускаем пустые строки и комментарии
                if not line or line.startswith('#'):
                    continue

                # Разделяем по первому знаку '='
                if '=' in line:
                    key, value = line.split('=', 1)
                    self.config[key.strip()] = value.strip()

        return self.config


    def slowfetch_out(self):
        global config
        self.OS_NAME = self.config.get('OS_NAME')
        self.DE = self.config.get('DE')
        self.VERSION = self.config.get('VERSION')
        #print(self.OS_NAME, self.WM, self.VERSION)
        #print(f" ___        	    ___          ")
        #print(f"/   \\       	   /   \\         {Colors.LIGHT_GREEN}OS{Colors.END}: {self.OS_NAME}")
        #print(f"|   |              |   |         {Colors.LIGHT_GREEN}Kernel{Colors.END}: In Development...")
        #print(f"| @ |   QuickPyre  | @ |         {Colors.LIGHT_GREEN}Uptime{Colors.END}: {self.uptime}")
        #print(f"|   |              |   |         {Colors.LIGHT_GREEN}DE{Colors.END}: {self.DE}")
        #print(f"\\___/     \\_|_/    \\___/         {Colors.LIGHT_GREEN}Version{Colors.END}: {self.VERSION}")
        #print(f"                                 {Colors.LIGHT_GREEN}Shell{Colors.END}: In Development...")
        print(f"           . ..:.")
        print(f"           .+@..+.")
        print(f"           ++# ***..")
        print(f"         ..*.:*...:.")
        print(f"          -:.+:-+.::")
        print(f"      =   %++%*++=+.:               {Colors.LIGHT_GREEN}OS{Colors.END}: {self.OS_NAME}")
        print(f"      =-... @*=-=+*#@+.             {Colors.LIGHT_GREEN}Kernel{Colors.END}: In Development...")
        print(f"     %.-=*:-=@@@@@@@%*==.           {Colors.LIGHT_GREEN}Uptime{Colors.END}: {self.uptime}")
        print(f"    -#**%:*@         @*-=.          {Colors.LIGHT_GREEN}DE{Colors.END}: {self.DE}")
        print(f"  .-+-====@  @@   .   #...*--       {Colors.LIGHT_GREEN}Version{Colors.END}: {self.VERSION}")
        print(f"  --=.+@@@@@%::@:     @@@@%*..      {Colors.LIGHT_GREEN}Shell{Colors.END}: In Development...")
        print(f" .=#%@@          :::: @    @+-.")   
        print(f".:#*=@  -  .....      @ ::  @=*.    {Colors.CYAN}██{Colors.BLUE}██{Colors.PURPLE}██" f"{Colors.GREEN}██{Colors.END}")
        print(f" =#++@        .. .. @@      @:+-    {Colors.YELLOW}██{Colors.RED}██{Colors.END}")
        print(f".+.=+@ :+: @@ :.-:.       : @+- .")
        print(f" -*@+@   . @  :   ..... -   *--.")
        print(f" .:*%%@@   @  ..:         @@@*..")
        print(f"   .:+#-@@@@ ---::.   @@@@@-.")
        print(f"    .-*%@%*@  :. = @  @@@+:.")
        print(f"        =**@@       @@@..")
        print(f"         .:-*@@@@@@%-")
        print(f"             =:....=")