<<<<<<< HEAD
from config.config import main_page
from auth.login import Login
from auth.signup import Signup


is_working = True
while is_working:
    print(main_page.get("welcome"))
    print(main_page.get("choices"))
    num = input(main_page.get("input"))
    match num:
        case "1":
            Login()
        case "2":
            obj_signup = Signup()
            obj_signup.signup_func()
        case "3":
            is_working = False
        case other:
            print(main_page.get("invalid_choice"))
=======
from config.config import main_page
from auth.login import Login
from auth.signup import Signup


is_working = True
while is_working:
    print(main_page.get("welcome"))
    print(main_page.get("choices"))
    num = input(main_page.get("input"))
    match num:
        case "1":
            Login()
        case "2":
            obj_signup = Signup()
            obj_signup.signup_func()
        case "3":
            is_working = False
        case other:
            print(main_page.get("invalid_choice"))
>>>>>>> origin/main
