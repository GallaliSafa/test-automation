import collections
# https://docs.python.org/3/library/typing.html#the-any-type
from typing import Any
import numpy as n



from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService

def is_equal_unordered(value_a: [Any], value_b: [Any]):
    narr1 = n.array([value_a])
    narr2 = n.array([value_b])

    return (narr1 == narr2).all()

def test_list_user_no_user(monkeypatch):
    def mock_get_users(*args):
        return []

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    users = user_service.list_users()

    assert is_equal_unordered(users, [])


def test_list_user_multiple_users(monkeypatch):
    def mock_get_users(*args):
        return [{
            'id': 1,
            'email': 'lolo@gmail.com'
        }, {
            'id': 2,
            'email': 'lala@gmail.com'
        }, {
            'id': 3,
            'email': 'lili@gmail.com'
        }]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    users = user_service.list_users()

    assert is_equal_unordered(users, [
        {
            'id': 1,
            'email': 'lolo@gmail.com'
        }, {
            'id': 2,
            'email': 'lala@gmail.com'
        }, {
            'id': 3,
            'email': 'lili@gmail.com'
        }
    ])



def test_list_user_multiple_users_with_lowercase_check(monkeypatch):
    def mock_get_users(*args):
        return [{
            'id': 1,
            'email': 'MAMA@gmail.com'
        }, {
            'id': 2,
            'email': 'PAPA@hotmail.com'
        }, {
            'id': 3,
            'email': 'TATA@gmail.com'
        }]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    users = user_service.list_users()



    assert is_equal_unordered(users, [
        {
            'id': 1,
            'email': 'mama@gmail.com'
        }, {
            'id': 2,
            'email': 'papi@hotmail.com'
        }, {
            'id': 3,
            'email': 'tata@gmail.com'
        }
    ])