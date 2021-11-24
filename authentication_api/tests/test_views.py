import django
django.setup()
from random import randint
from django.test import Client
import string

client = Client()


# ################# AUX_FUNCTIONS #######################
def credentials_creater() -> dict:
    """ This method just creates random credentials """
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


# ################# TEST_FUNCTIONS #######################
def test_view_auth_create_admin_user():
    """ This method creates a new random admin user """
    user = credentials_creater()
    user.update(is_admin=True)
    print(user)
    response = client.post('/api_authentication/class_method/create_user/', user)
    assert response.status_code == 201, response.content.decode()


def test_view_auth_create_no_admin_user():
    """ This method creates a new random admin user """
    user = credentials_creater()
    user.update(is_admin=False)
    print(user)
    response = client.post('/api_authentication/class_method/create_user/', user)
    assert response.status_code == 201, response.content.decode()


if __name__ == '__main__':
    test_view_auth_create_admin_user()
