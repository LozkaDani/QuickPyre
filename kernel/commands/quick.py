import os
from pathlib import Path
import urllib
import urllib.error
import urllib.request
import shutil
import json
class QuickManager:
    def __init__(self, path_to_apps_dir, usr_now):
        self.usr_now = usr_now
        self.path_to_apps_dir = path_to_apps_dir

    def download_file(self, url, destination):
        try:
            # Создаем директорию, если она не существует
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            
            with urllib.request.urlopen(url) as response:
                with open(destination, 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
            return True
        except urllib.error.URLError as e:
            print(f"Download error: {e}")
            #print(url)
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def find_apps_dir(self):
        current_dir = Path(".")

    def download_required_files(self, app_for_install):
        apps_dir = self.find_apps_dir()
        apps = self.list_apps("apps")
        current_dir = Path(".")
        #github repo base url
        base_url = "https://raw.githubusercontent.com/LozkaDani/QuickPyre-quick-apps/main/"
        
        files = [app["name"] for app in apps if app["type"] == "file"]

        if app_for_install in files:
            files_to_download = [
                {
                    "url": base_url + f"apps/{app_for_install}.py",
                    "destination": os.path.join(current_dir, f"../apps/{app_for_install}.py"),
                    "name": f"{app_for_install}"
                }
            ]
        else:
            print(f"quick: error: target not found: {app_for_install}")
            #print(apps)
            return

        downloaded_count = 0
        total_files = len(files_to_download)
        for i, file_info in enumerate(files_to_download):
            if Path(file_info["destination"]).exists():
                print(f"warning: {app_for_install} is existing on pc -- reinstalling")
                confirm = input("Proceed with installation [Y/n]: ")
                if confirm == "" or confirm.lower() == "y":
                    pass
                else:
                    return
            if self.download_file(file_info["url"], file_info["destination"]):
                print(f"Successfully downloaded: {file_info['name']}")
                # with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../../home/{self.usr_now}/.program_aliases"), "a+") as f:
                #     lines = f.readlines()
                #     print(lines)
                #     if not f"programm_alias={file_info["name"]}" in lines:
                #         f.write(f"\nprogramm_alias={file_info["name"]}")
                alias_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../../home/{self.usr_now}/.program_aliases")
                with open(alias_file, "r") as f:
                    aliases = f.readlines()
                new_alias = f'programm_alias={file_info["name"]}\n'
                #print(aliases)
                #print(new_alias)
                if not new_alias in aliases:
                    with open(alias_file, "a") as f:
                        f.write(new_alias + "\n")
            else:
                print(f"Failed to download: {file_info['name']}")
        
        return downloaded_count == total_files
    
    def remove_files(self, app_for_rem):
        apps_dir = self.find_apps_dir()
        #apps = self.list_apps("apps")
        current_dir = Path(".")
        
        #files = [app["name"] for app in apps if app["type"] == "file"]

        #if app_for_rem in files:
        files_to_remove = [
           {
               "destination": os.path.join(current_dir, f"../apps/{app_for_rem}.py"),
                "name": f"{app_for_rem}"
           }
        ]
        #else:
            #print(f"quick: error: target not found: {app_for_rem}")
            #print(apps)
            #return
        #remove
        for i, file_info in enumerate(files_to_remove):
            if Path(file_info["destination"]).exists():
                confirm = input("Are you sure? [Y/n]: ")
                if confirm == "" or confirm.lower() == "y":
                    pass
                else:
                    return
            else:
                print(f"quick: package {file_info["name"]} not finded.")
        alias_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../../home/{self.usr_now}/.program_aliases")
        with open(alias_file, "r+") as f:
            new_aliases = []
            aliases = f.readlines()
            rem_alias = f'programm_alias={file_info["name"]}\n'
            #print(aliases)
            #print(rem_alias)
            if rem_alias in aliases:
                for line in aliases:
                    if not rem_alias == line:
                        new_aliases.append(line)
                #print(new_aliases)
                #print(rem_alias)
            if new_aliases != []:
                f.write(" ".join(new_aliases))
                os.remove(file_info["destination"])
                    

    def list_apps(self, path):
        "получает список всех приложений в папке apps"
        contents = self.get_repo_contents(path)
        if contents is None:
            print("Не удалось получить список приложений")
            return []
        
        apps = []
        for item in contents:
            if item['type'] == 'file' and item['name'].endswith('.py'):
                app_name = item['name'][:-3]  #Убираем .py
                apps.append({
                    'name': app_name,
                    'type': 'file',
                    'size': item['size']
                })
            elif item['type'] == 'dir':
                apps.append({
                    'name': item['name'],
                    'type': 'folder',
                    'size': 'idk'
                })
        
        return apps
    
    def display_apps_info(self):
        "Отображает информацию о всех доступных приложениях"
        apps = self.list_apps("apps")
        #system = self.list_apps("system")
        
        print(f"{len(apps)} apps found:")
        print("-" * 50)
        
        files_in_apps = [app for app in apps if app['type'] == 'file']
        folders_in_apps = [app for app in apps if app['type'] == 'folder']
        
        print("apps/")
        if files_in_apps:
            print(f"  Files ({len(files_in_apps)}):")
            for app in files_in_apps:
                size_str = f"{app['size']} bytes" if app['size'] > 0 else "N/A"
                print(f"        {app['name']} ({size_str})")
        
        if folders_in_apps:
            print(f"\nFolders ({len(folders_in_apps)}):")
            for app in folders_in_apps:
                print(f"        {app['name']}")
        
        return apps
    def get_repo_contents(self, path=""):
        # # #содержимое папки в гитхаб репо.
        # # # нужен путь до самой папки (тоесть apps или system)
        # # # возвращает список словарей с инфой
        # # # было взято у ии, извините(
        #GitHub API url
        api_url = f"https://api.github.com/repos/LozkaDani/QuickPyre-quick-apps/contents/{path}"
        
        try:
            req = urllib.request.Request(api_url)
            #добавляем заголовок User-Agent, т.к. GitHub API требует его
            req.add_header('User-Agent', 'Mozilla/5.0')
            
            with urllib.request.urlopen(req) as response:
                data = response.read()
                items = json.loads(data)
                
                result = []
                for item in items:
                    result.append({
                        'name': item['name'],
                        'type': item['type'],  # 'file' или 'dir'
                        'path': item['path'],
                        'download_url': item.get('download_url'),  # Только для файлов
                        'size': item.get('size', 0)  # Размер в байтах
                    })
                return result
                
        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
            return None
        except urllib.error.URLError as e:
            print(f"URL Error: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            return None
        except Exception as e:
            print(f"Error getting repo contents: {e}")
            return None
