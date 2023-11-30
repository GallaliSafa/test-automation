from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService
import collections


def test_list_users_ids(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_users(*args):
        return [
            {'id': '1', 'email': 'mama@gmail.com'},
            {'id': '2', 'email': 'papa@hotmail.com'},
            {'id': '3', 'email': 'tata@gmail.com'}
        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    ids = user_service.list_users()

    assert ids == ['1', '2','3']
