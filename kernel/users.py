import json
import os
from pathlib import Path
class User:
    def __init__(self, username, password=None, is_root=False):
        self.username = username
        self.password = password
        self.is_root = is_root
    
    def login(self):
        users_dir = Path("./usrs/")
        users_file = users_dir / "usrs.json"

        if not users_file.exists():
            print("ERROR: NO usrs.json FILE.")
            print(users_file)
            return False
        users = self._load_users(users_file)

        user_found = None
        if users == []:
            print("Login error: no any users registrated.")
            #want_reg()
            users = self._load_users(users_file)
        for user in users:
            if user["username"] == self.username:
                user_found = user
                break
        if user_found is None:
            print("Login error: this user in NOT exist")
            #login_konsole()
            return False

        if user_found["password"] == self.password:
            print(f"Welcome, {self.username}!")
            global usr_now
            usr_now = self.username
            print("\nType <help> for list of commands.\n")
            return True
        else:
            print("Login error: incorrect password")
            #login_konsole()
            return False


    def registration(self):
        users_dir = Path("./usrs")
        users_file = users_dir / "usrs.json"
        users = self._load_users(users_file)
        
        if any(u["username"] == self.username for u in users):
            print("Registration error: there is an user with this name.")
            return False

        users.append({
            "username": self.username,
            "password": self.password,
            "isroot": self.is_root
        })
        self._save_users(users_file, users)
        print(f"User {self.username} registered successfully.")
        os.mkdir(f"../home/{self.username}")

    def _load_users(self, file_path):
        if file_path.exists():
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    return data
            except json.JSONDecodeError as e:
                print(f"Error reading users file: {e}")
                return []
        return []

    def _save_users(self, file_path, users):
        with open(file_path, 'w') as f:
            json.dump(users, f, indent=4)