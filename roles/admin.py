<<<<<<< HEAD
import json
from util.util import user_signup_func
from config.config import admin_page
from config.config import LOGIN_DB_PATH, USER_DATA_DB_PATH


def make_admin():
    new = input(admin_page.get("new_admin_name"))
    with open(LOGIN_DB_PATH, 'r+') as file:
        file_data = json.load(file)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    iterator = 0
    v = 0
    for item in file_data.get("user_details"):
        if item.get('username') == new and item.get('role') == 'admin':
            v += 1
        if item.get('username') == new:
            item['role'] = 'admin'
            break
        iterator += 1
    if iterator == len(file_data.get("user_details")):
        print(admin_page.get("user_not_present"))
    else:
        if v > 0:
            print(admin_page.get("already_admin_message"))
        else:
            print(str(admin_page.get("new_admin_made")).format(new))
    with open(LOGIN_DB_PATH, 'w') as file:
        json.dump(file_data, file, indent=4)


def view_users():
    with open(USER_DATA_DB_PATH, 'r') as file:
        file_data = json.load(file)
        users = []
        for item in file_data:
            print(item)
            users.append(item)
        return users
        file.seek(0)


def remove_user_db(user):
    with open(USER_DATA_DB_PATH, 'r+') as file:
        file_data = json.load(file)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    del file_data[user]
    with open(USER_DATA_DB_PATH, 'w') as file:
        json.dump(file_data, file, indent=4)


def remove_user(user):

    with open(LOGIN_DB_PATH, 'r+') as file:
        file_data = json.load(file)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    iterator = 0
    for item in file_data["user_details"]:
        if item['username'] == user:
            break
        iterator += 1
    if iterator == len(file_data["user_details"]):
        return False
        print(admin_page.get("user_not_present"))
    else:
        remove_user_db(user)
        del file_data["user_details"][iterator]
        print(admin_page.get("user_removed"))
    with open(LOGIN_DB_PATH, 'w') as file:
        json.dump(file_data, file, indent=4)
    return True


class AdminLogin:
    @staticmethod
    def login():
        # admin menu
        print(admin_page.get("welcome"))
        is_working = True
        while is_working:
            print(admin_page.get("choices"))
            num = input(admin_page.get("input"))
            match num:
                case "1":
                    user_signup_func()
                case "2":
                    remove_user()
                case "3":
                    view_users()
                case "4":
                    make_admin()
                case "5":
                    quit()
                case other:
                    print(admin_page.get("error_message"))
=======
import json
from util.util import user_signup_func
from config.config import admin_page
from config.config import LOGIN_DB_PATH, USER_DATA_DB_PATH


def make_admin():
    new = input(admin_page.get("new_admin_name"))
    with open(LOGIN_DB_PATH, 'r+') as file:
        file_data = json.load(file)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    iterator = 0
    v = 0
    for item in file_data.get("user_details"):
        if item.get('username') == new and item.get('role') == 'admin':
            v += 1
        if item.get('username') == new:
            item['role'] = 'admin'
            break
        iterator += 1
    if iterator == len(file_data.get("user_details")):
        print(admin_page.get("user_not_present"))
    else:
        if v > 0:
            print(admin_page.get("already_admin_message"))
        else:
            print(str(admin_page.get("new_admin_made")).format(new))
    with open(LOGIN_DB_PATH, 'w') as file:
        json.dump(file_data, file, indent=4)


def view_users():
    with open(USER_DATA_DB_PATH, 'r') as file:
        file_data = json.load(file)
        users = []
        for item in file_data:
            print(item)
            users.append(item)
        return users
        file.seek(0)


def remove_user_db(user):
    with open(USER_DATA_DB_PATH, 'r+') as file:
        file_data = json.load(file)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    del file_data[user]
    with open(USER_DATA_DB_PATH, 'w') as file:
        json.dump(file_data, file, indent=4)


def remove_user(user):

    with open(LOGIN_DB_PATH, 'r+') as file:
        file_data = json.load(file)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    iterator = 0
    for item in file_data["user_details"]:
        if item['username'] == user:
            break
        iterator += 1
    if iterator == len(file_data["user_details"]):
        return False
        print(admin_page.get("user_not_present"))
    else:
        remove_user_db(user)
        del file_data["user_details"][iterator]
        print(admin_page.get("user_removed"))
    with open(LOGIN_DB_PATH, 'w') as file:
        json.dump(file_data, file, indent=4)
    return True


class AdminLogin:
    @staticmethod
    def login():
        # admin menu
        print(admin_page.get("welcome"))
        is_working = True
        while is_working:
            print(admin_page.get("choices"))
            num = input(admin_page.get("input"))
            match num:
                case "1":
                    user_signup_func()
                case "2":
                    remove_user()
                case "3":
                    view_users()
                case "4":
                    make_admin()
                case "5":
                    quit()
                case other:
                    print(admin_page.get("error_message"))
>>>>>>> origin/main
