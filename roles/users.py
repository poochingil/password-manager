<<<<<<< HEAD
import json
from config.config import LOGIN_DB_PATH, USER_DATA_DB_PATH
from config.config import user_page

filepath_login = LOGIN_DB_PATH
filepath_user_data = USER_DATA_DB_PATH


# viewing user website and respective passwords
def read_json(username, filename=filepath_user_data):
    file = open(filename)
    data = json.load(file)
    file.close()
    website_container = []
    for websites in data[username]:
        website_container.append(websites)
    return website_container


def add_website(username,uid, website, password, filename=filepath_user_data):

    new_data = {
        "website": website,
        "userid": uid,
        "passwd": password
    }
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data[username].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    return True


class Users:
    def __init__(self, username):
        # user menu
        is_working = True
        while is_working:
            print(user_page.get("Choices"))
            num = input(user_page.get("input"))
            match num:
                case "1":
                    add_website(username)
                case "2":
                    read_json(username)
                case "3":
                    exit()
                case other:
                    print(user_page.get("invalid_choice"))
=======
import json
from config.config import LOGIN_DB_PATH, USER_DATA_DB_PATH
from config.config import user_page

filepath_login = LOGIN_DB_PATH
filepath_user_data = USER_DATA_DB_PATH


# viewing user website and respective passwords
def read_json(username, filename=filepath_user_data):
    file = open(filename)
    data = json.load(file)
    file.close()
    website_container = []
    for websites in data[username]:
        website_container.append(websites)
    return website_container


def add_website(username,uid, website, password, filename=filepath_user_data):

    new_data = {
        "website": website,
        "userid": uid,
        "passwd": password
    }
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data[username].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    return True


class Users:
    def __init__(self, username):
        # user menu
        is_working = True
        while is_working:
            print(user_page.get("Choices"))
            num = input(user_page.get("input"))
            match num:
                case "1":
                    add_website(username)
                case "2":
                    read_json(username)
                case "3":
                    exit()
                case other:
                    print(user_page.get("invalid_choice"))
>>>>>>> origin/main
