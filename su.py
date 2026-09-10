import os
from pathlib import Path
import json

def su_cmd(args, User, usr_now):
    if not args:
        print("su: missing operand")
        return usr_now
    
    new_user = args[0]
    file_path = Path(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../usrs/usrs.json"))
    
    #loading users.
    with open(file_path, 'r') as f:
        all_users = json.load(f)
    
    #looking for a user
    user_found = None
    for user in all_users:
        if user["username"] == new_user:
            user_found = user
            break
    
    if user_found is None:
        print(f"su: user {new_user} does not exist.")
        return usr_now
    
    #requesting a password
    password = input(f"{new_user}'s password: ")
    
    #checking the password
    if user_found["password"] == password:
        print(f"Welcome, {new_user}!")
        usr_now = new_user
        return new_user  #returning a new user
    else:
        print("su: Authentication failure")
        return usr_now