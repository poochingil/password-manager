<<<<<<< HEAD
from auth.signup import InitialiseDb
import json


def test_initialise_db():
    InitialiseDb("new_user", "testing\mock_db\mock_user_data.json")
    with open("testing\mock_db\mock_user_data.json", 'r') as file:
        file_data = json.load(file)

    var = file_data
    website_list = var["new_user"]

    assert website_list == [{}]
=======
from auth.signup import InitialiseDb
import json


def test_initialise_db():
    InitialiseDb("new_user", "testing\mock_db\mock_user_data.json")
    with open("testing\mock_db\mock_user_data.json", 'r') as file:
        file_data = json.load(file)

    var = file_data
    website_list = var["new_user"]

    assert website_list == [{}]
>>>>>>> origin/main
