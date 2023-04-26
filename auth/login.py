<<<<<<< HEAD
import getpass
import json
import hashlib
from roles.users import Users
from roles.admin import AdminLogin
from config.config import SALT, ATTEMPTS, LOGIN_DB_PATH
from config.config import login_page

file_login_path = LOGIN_DB_PATH
admin = "admin"
user = "user"


class Login:
    @staticmethod
    def login(password):

        salt = SALT
        database_password = password + salt
        hashed = hashlib.sha512(database_password.encode())
        return hashed

=======
import getpass
import json
import hashlib
from roles.users import Users
from roles.admin import AdminLogin
from config.config import SALT, ATTEMPTS, LOGIN_DB_PATH
from config.config import login_page

file_login_path = LOGIN_DB_PATH
admin = "admin"
user = "user"


class Login:
    @staticmethod
    def login(password):

        salt = SALT
        database_password = password + salt
        hashed = hashlib.sha512(database_password.encode())
        return hashed

>>>>>>> origin/main
