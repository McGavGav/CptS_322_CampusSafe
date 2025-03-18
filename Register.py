import json
import os

## initial basic writeup for registering a user within a database
## right now checks for an 8 digit variable -- to replicate a wsuID
## needs work on error handling but basic function is okay so far.

USER_DB = "users.json"

def load_users():
    if not os.path.exists(USER_DB):
        return {}
    with open(USER_DB, "r") as file:
        return json.load(file)

def save_users(users):
    with open(USER_DB, "w") as file:
        json.dump(users, file, indent=4)

def is_valid_id(user_id, users):
    return user_id.isdigit() and len(user_id) == 8 and user_id not in users

def register_user():
    users = load_users()
    
    user_id = input("Enter an 8-digit unique User ID: ")
    if not is_valid_id(user_id, users):
        print("Invalid or already taken User ID. Try again.")
        return
    
    last_name = input("Enter Last Name: ").strip()
    first_name = input("Enter First Name: ").strip()
    
    users[user_id] = {"last_name": last_name, "first_name": first_name}
    save_users(users)
    print("User registered successfully!")

if __name__ == "__main__":
    register_user()
