import os
class slowfetch_class:
    def __init__(self):
        self.OS_NAME=""
        self.DE=""
        self.VERSION=""
        self.config = {}
        self.config = self.parse_config('../config/slowfetch.cfg')
        self.slowfetch_out()


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
        print(f" ___        	    ___          ")
        print(f"/   \       	   /   \         OS: {self.OS_NAME}")
        print(f"|   |              |   |         DE: {self.DE}")
        print(f"| @ |   QuickPire  | @ |         VERSION: {self.VERSION}")
        print(f"|   |              |   |         ")
        print(f"\___/     \_|_/    \___/         ")
        print("")
        print("")
        print("")