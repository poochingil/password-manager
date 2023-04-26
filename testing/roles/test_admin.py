<<<<<<< HEAD
from roles.admin import view_users
from config.config import USER_DATA_DB_PATH


def test_val():
    user_list = view_users()

    assert user_list[0] == "qwerty"
=======
from roles.admin import view_users
from config.config import USER_DATA_DB_PATH


def test_val():
    user_list = view_users()

    assert user_list[0] == "qwerty"
>>>>>>> origin/main
