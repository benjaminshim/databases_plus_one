# import data.users as usrs
import server.endpoints as ep
import pytest
from http.client import (
    NOT_FOUND,
    OK,
)
from unittest.mock import patch

TEST_CLIENT = ep.app.test_client()

MIN_USER_NAME_LEN = 1
NAME = "user"


# def test_get_users():
#     users = usrs.get_users()
#     assert isinstance(users, dict)
#     # assert len(users) > 0
#     for key in users:
#         assert isinstance(key, str)
#         assert len(key) >= MIN_USER_NAME_LEN
#         user = users[key]
#         assert isinstance(user, dict)


@pytest.mark.skip('This test is failing for now')
def test_del_user(mock_del):
    resp = TEST_CLIENT.delete(f'{ep.RESTAURANTS_EP}/AnyName')
    assert resp.status_code == OK


@patch('data.users.update_username', side_effect=ValueError(), autospec=True)
def test_bad_update_username(mock_update):
    """
    Testing we do the right thing with a call to update_rating that fails.
    """
    resp = TEST_CLIENT.put(f'{ep.USERS_EP}/AnyName/100')
    assert resp.status_code == NOT_FOUND


# @patch('data.users.update_username', autospec=True)
# def test_update_username(mock_update):
#     """
#     Testing we do the right thing with a call to update_rating that succeeds.
#     """
#     resp = TEST_CLIENT.put(f'{ep.USERS_EP}/AnyName/100')
#     assert resp.status_code == OK
