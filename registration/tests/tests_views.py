from random import randint
import string


# ################## AUX_TEST_FUNCTION ##################
def credentials_creater() -> dict:
    str_lower = list(string.ascii_lowercase)
    all_char = list(string.hexdigits)
    word = ''
    password = ''
    while True:
        word += str_lower[randint(0, 25)]
        password += all_char[randint(0, len(all_char) - 1)]
        if len(word) == 10:
            return {
                'email': f'{word}@gmail.com',
                'username': word,
                'password': password,
                'password2': password
            }


# ################## TEST_VIEWS #########################

def test_isert_a_user():
    pass


def test_update_a_user():
    pass


def test_delete_a_user():
    pass


def test_get_a_user():
    pass


def test_lis_a_users():
    pass


def test_filter_a_user_info():
    pass
