<<<<<<< HEAD
import getpass
import json
import hashlib
from auth.login import Login
from config.config import signup_page
from config.config import SALT, LOGIN_DB_PATH, USER_DATA_DB_PATH

file_login_path = LOGIN_DB_PATH
file_user_data_path = USER_DATA_DB_PATH


class InitialiseDb:
    def __init__(self, username, file_user_data_path):
        default_list = {username: []}
        with open(file_user_data_path, 'r+') as file:
            file_data = json.load(file)
            file_data.update(default_list)
            file.seek(0)
            json.dump(file_data, file, indent=4)

        new_data = {}
        with open(file_user_data_path, 'r+', encoding="utf-8") as file:
            file_data = json.load(file)
            file_data[username].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)


class Signup:
    @staticmethod
    def write_json(new_data, filepath=file_login_path):
        with open(filepath, 'r+') as file:
            file_data = json.load(file)
            file_data["user_details"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
            print(signup_page.get("new_user_confirmation"))
            return True

    @staticmethod
    def signup_func(username, password, email, phone_number):
        # with open(file_user_data_path, 'r', encoding="utf-8") as file:
        #         file_data = json.load(file)
        #         user_list = []
        #         for item in file_data:
        #             user_list.append(item)
        #         if username in user_list:
        #             return False
        salt = SALT
        database_password = password + salt
        hashed = hashlib.sha512(database_password.encode())
        user_data = {"username": username,
                     "password": hashed.hexdigest(),

                     "email": email,
                     "phone_number": phone_number}

        return user_data
=======
import getpass
import json
import hashlib
from auth.login import Login
from config.config import signup_page
from config.config import SALT, LOGIN_DB_PATH, USER_DATA_DB_PATH

file_login_path = LOGIN_DB_PATH
file_user_data_path = USER_DATA_DB_PATH


class InitialiseDb:
    def __init__(self, username, file_user_data_path):
        default_list = {username: []}
        with open(file_user_data_path, 'r+') as file:
            file_data = json.load(file)
            file_data.update(default_list)
            file.seek(0)
            json.dump(file_data, file, indent=4)

        new_data = {}
        with open(file_user_data_path, 'r+', encoding="utf-8") as file:
            file_data = json.load(file)
            file_data[username].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)


class Signup:
    @staticmethod
    def write_json(new_data, filepath=file_login_path):
        with open(filepath, 'r+') as file:
            file_data = json.load(file)
            file_data["user_details"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
            print(signup_page.get("new_user_confirmation"))
            return True

    @staticmethod
    def signup_func(username, password, email, phone_number):
        # with open(file_user_data_path, 'r', encoding="utf-8") as file:
        #         file_data = json.load(file)
        #         user_list = []
        #         for item in file_data:
        #             user_list.append(item)
        #         if username in user_list:
        #             return False
        salt = SALT
        database_password = password + salt
        hashed = hashlib.sha512(database_password.encode())
        user_data = {"username": username,
                     "password": hashed.hexdigest(),

                     "email": email,
                     "phone_number": phone_number}

        return user_data
>>>>>>> origin/main
