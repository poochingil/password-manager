<<<<<<< HEAD
import json
import getpass
import hashlib
from config.config import SALT, USER_DATA_DB_PATH, LOGIN_DB_PATH
from config.config import util_page
from models import RoleMappingModel

file_login_path = LOGIN_DB_PATH
file_user_data_path = USER_DATA_DB_PATH


def write_json(new_data, filepath=file_login_path):
    with open(filepath, 'r+') as file:
        file_data = json.load(file)
        file_data["user_details"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
        return True


def initialize_db(username):
    default_list = {username: []}
    with open(file_user_data_path, 'r+') as file:
        file_data = json.load(file)
        file_data.update(default_list)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    new_data = {}
    with open(file_user_data_path, 'r+') as file:
        file_data = json.load(file)
        file_data[username].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


def user_signup_func(username, password):
    # user made by admin

    with open(file_user_data_path, 'r') as file:
        file_data = json.load(file)
        user_list = []
        for item in file_data:
            user_list.append(item)
        if username in user_list:
            return False
            print(util_page.get("user_existing"))

            file.seek(0)

    salt = SALT
    database_password = password + salt
    hashed = hashlib.sha512(database_password.encode())
    user_data = {"username": username,
                 "password": hashed.hexdigest(),
                 "role": "user"}
    initialize_db(username)
    if write_json(user_data):
        return True
    return False
    print(util_page.get("new_user_confirmation"))


def isAdmin(user_id):
    if RoleMappingModel.query.filter_by(user_id=user_id).first().role_id == 1:
        return True
    else:
        return False
=======
import json
import getpass
import hashlib
from config.config import SALT, USER_DATA_DB_PATH, LOGIN_DB_PATH
from config.config import util_page
from models import RoleMappingModel

file_login_path = LOGIN_DB_PATH
file_user_data_path = USER_DATA_DB_PATH


def write_json(new_data, filepath=file_login_path):
    with open(filepath, 'r+') as file:
        file_data = json.load(file)
        file_data["user_details"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
        return True


def initialize_db(username):
    default_list = {username: []}
    with open(file_user_data_path, 'r+') as file:
        file_data = json.load(file)
        file_data.update(default_list)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    new_data = {}
    with open(file_user_data_path, 'r+') as file:
        file_data = json.load(file)
        file_data[username].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


def user_signup_func(username, password):
    # user made by admin

    with open(file_user_data_path, 'r') as file:
        file_data = json.load(file)
        user_list = []
        for item in file_data:
            user_list.append(item)
        if username in user_list:
            return False
            print(util_page.get("user_existing"))

            file.seek(0)

    salt = SALT
    database_password = password + salt
    hashed = hashlib.sha512(database_password.encode())
    user_data = {"username": username,
                 "password": hashed.hexdigest(),
                 "role": "user"}
    initialize_db(username)
    if write_json(user_data):
        return True
    return False
    print(util_page.get("new_user_confirmation"))


def isAdmin(user_id):
    if RoleMappingModel.query.filter_by(user_id=user_id).first().role_id == 1:
        return True
    else:
        return False
>>>>>>> origin/main
