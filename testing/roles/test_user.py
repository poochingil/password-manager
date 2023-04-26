<<<<<<< HEAD
from roles.users import add_website
import json


def test_add_website():
    add_website("qwerty", "testing\mock_db\mock_user_data.json")
    with open("testing\mock_db\mock_user_data.json", 'r') as file:
        file_data = json.load(file)

    var = file_data
    website_list = var["qwerty"]
    var1 = website_list.pop()
    assert var1["website"] == "google.com"
=======
from roles.users import add_website
import json


def test_add_website():
    add_website("qwerty", "testing\mock_db\mock_user_data.json")
    with open("testing\mock_db\mock_user_data.json", 'r') as file:
        file_data = json.load(file)

    var = file_data
    website_list = var["qwerty"]
    var1 = website_list.pop()
    assert var1["website"] == "google.com"
>>>>>>> origin/main
