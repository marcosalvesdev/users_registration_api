import django
django.setup()
import json
import string
from datetime import date
from random import randint
from rest_framework.test import RequestsClient
from registration_app.aux_functions.validators_aux_methods import (
    CpfAuxMethods,
)

client = RequestsClient()


# ################## AUX_TEST_FUNCTION ##################

def create_a_name() -> dict:
    vowels = ['a', 'e', 'i', 'o', 'u']
    parts = ['first_name', 'second_name', 'last_name', 'fullname']
    parts_name = {}
    full_name = list()
    for part in parts:
        if part == 'fullname':
            parts_name.update({part: ' '.join(name.capitalize() for name in full_name)})
            break
        name_part = ''.join(
            [string.ascii_letters[randint(0, 25)] + vowels[randint(0, 4)] for _ in range(0, 3)])
        full_name.append(name_part)
        parts_name.update({part: name_part.capitalize()})

    return parts_name


def generate_phone_number(ddd) -> str:
    n = str(ddd) if type(ddd) is int else ddd
    number = f"{n}{''.join([string.hexdigits[randint(0, 8)] for _ in range(0, 9)])}"
    return number


def create_a_new_user() -> dict:
    cpf = ''.join(CpfAuxMethods.cpf_generator())
    name = create_a_name()
    birthday = date(randint(1993, 2015), randint(1, 12), randint(1, 30)).isoformat()
    first_name = f"{name['first_name']} {name['second_name']}"
    phone = generate_phone_number(44)
    data = {
        "cpf": cpf,
        "first_name": first_name,
        "last_name": name.get('last_name'),
        "fullname": name.get('fullname'),
        "birthday": birthday,
        "email": f'{"".join(list(first_name)).lower().replace(" ", "")}@gmail.com',
        "phone": phone
    }
    '''for k, v in data.items():
        print(f'{k}: {v}')'''

    return data


def create_a_mail() -> str:
    email = f'{"".join([string.ascii_letters[randint(0, 24)] for _ in range(0, 6)])}.gmail.com'
    return email


TOKEN = f'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NzU4OTY1LCJpYXQi' \
        f'OjE2Mzc3NTcxNjUsImp0aSI6IjhhYjcwNjA3M2YyNzQwZTk4OGU0OGZmYTE1MmE1YWFhIiwidXNlcl9pZCI6Imt2bm1xdnJwdHUifQ._' \
        f'Fc1HdqVgl0Hm360c8LwCtRsbnuyEd_EPv7dkKGXixc'

# GENERIC USER
user_data = create_a_new_user()


# ################## TEST_VIEWS #########################
def test_list_all_users():
    url = r'http://127.0.0.1:8000/registration/list_user/'
    response = client.get(
        url=url,
        headers={
            'Authorization': TOKEN
        }
    )

    break_line = True
    for user in json.loads(response.content.decode()):
        if break_line:
            print('\n')
            break_line = False
        print(user)

    assert response.status_code == 200


def test_isert_a_user():
    url = r'http://127.0.0.1:8000/registration/regiser_user/'
    response = client.post(
        url=url,
        json=user_data,
        headers={
            'Authorization': TOKEN
        }
    )

    print('\n')
    print(response.content.decode())
    assert response.status_code == 201


def test_update_a_user():
    new_user_data = create_a_new_user()
    user_data.update({'first_name': new_user_data.get('first_name')})
    user_data.update({'last_name': new_user_data.get('last_name')})

    url = rf'http://127.0.0.1:8000/registration/update_user/{user_data["cpf"]}'
    response = client.put(
        url=url,
        json=user_data,
        headers={
            'Authorization': TOKEN
        }
    )

    print('\n')
    print(response.content.decode())
    assert response.status_code == 200


def test_get_a_user():
    url = rf'http://127.0.0.1:8000/registration/retrieve_user/{user_data["cpf"]}'
    response = client.get(
        url=url,
        headers={
            'Authorization': TOKEN
        }
    )

    print('\n')
    print(response.content.decode())
    assert response.status_code == 200



def test_filter_a_user_info():
    data = {
        "user_id": user_data["cpf"],
        "field": ["first_name", "last_name"]
    }
    url = rf'http://127.0.0.1:8000/registration/filter_in_users/'
    response = client.post(
        url=url,
        json=data,
        headers={
            'Authorization': TOKEN
        }
    )

    print('\n')
    print(response.content.decode())
    assert response.status_code == 200


def test_delete_a_user():
    url = rf'http://127.0.0.1:8000/registration/delete_user/{user_data["cpf"]}'
    response = client.delete(
        url=url,
        headers={
            'Authorization': TOKEN
        }
    )

    print(response.content.decode())
    assert response.status_code == 204
