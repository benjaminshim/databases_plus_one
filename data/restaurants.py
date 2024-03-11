"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
import random

import data.db_connect as dbc
import data.users as usrs
import data.restaurants as restaurants


BIG_NUM = 10000000000000
ID_LEN = 24
MOCK_ID = '0' * ID_LEN

RATING = 'rating'
TEST_RESTAURANT_NAME = 'Restaurant'

NAME = 'name'
RESTAURANT_COLLECT = 'restaurants'

USER_NAME = "User"
USER_ID = "_id"

TEST_RESTAURANT_FLDS = {
    TEST_RESTAURANT_NAME: 'Test name',
    RATING: 0,
}


restaurants = {
    'Papa Johns': {
        RATING: 5,
    },
    TEST_RESTAURANT_NAME: {
        RATING: 5,
    },
}


users = {
    10000: {
        NAME: "James"
    },
    10001: {
        NAME: "Jessie"
    },
}


def _get_test_name():
    name = 'test'
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)


def get_test_restaurant():
    test_rest = {}
    test_rest[TEST_RESTAURANT_NAME] = _get_test_name()
    test_rest[RATING] = 0
    return test_rest


def fetch_pets():
    """
    A function to return all pets in the data store.
    """
    return {"tigers": 2, "lions": 3, "zebras": 1}


def get_restaurants() -> dict:
    # dbc.connect_db()
    # return dbc.fetch_all_as_dict(NAME, RESTAURANT_COLLECT)
    dbc.connect_db()
    try:
        restaurants_dict = dbc.fetch_all_as_dict(NAME, RESTAURANT_COLLECT)
        return restaurants_dict
    except Exception as e:  # Consider a more specific exception based on your db_connect module
        print(f"Error fetching restaurants: {e}")
        return {}  # Or handle the error as appropriate


def _gen_id() -> str:
    _id = random.randint(0, BIG_NUM)
    _id = str(_id)
    _id = _id.rjust(ID_LEN, '0')
    return _id


def add_restaurant(name: str, rating: int) -> bool:
# def add_restaurant(name: str, description: str, owner_id: str, state: str, city: str, address: str, zip_code: str) -> bool:
    restaurants = {}
    if exists(name):
        raise ValueError(f'Duplicate restaurant name: {name=}')
    if not name:
        raise ValueError('Restaurant name may not be blank')
    restaurants[NAME] = name
    restaurants[RATING] = rating
    dbc.connect_db()
    _id = dbc.insert_one(RESTAURANT_COLLECT, restaurants)
    # restaurants[name] = {RATING: rating}
    return _id is not None
    # if exists(name):  # This function needs to be adapted to check using both name and owner or just owner
    #     raise ValueError(f'Duplicate restaurant name: {name}')
    # if not name:
    #     raise ValueError('Restaurant name may not be blank')

    # search_id = _gen_id()  # Assuming _gen_id generates a sufficiently unique identifier for public use
    
    # restaurant_document = {
    #     "search_id": search_id,
    #     "name": name,
    #     "description": description,
    #     "owner_id": owner_id,
    #     "state": state,
    #     "city": city,
    #     "address": address,
    #     "zip_code": zip_code,
    #     # "rating": rating, # this can be done through reviews
    # }
    
    # dbc.connect_db()
    # _id = dbc.insert_one(RESTAURANT_COLLECT, restaurant_document)
    # return _id is not None


def add_user(name: str, id: int) -> bool:
    users = {}
    if id in users:
        raise ValueError(f'Duplicate user id: {id=}')
    if not id:
        raise ValueError('Users are not allowed to be entered without ids')
    users[USER_ID] = _gen_id()
    users[USER_NAME] = name
    dbc.connect_db()
    _id = dbc.insert_one(usrs.USERS_COLLECT, users)
    return _id is not None


def del_restaurant(name: str):
    if exists(name):
        return dbc.del_one(RESTAURANT_COLLECT, {NAME: name})
    else:
        raise ValueError(f'Delete failure: {name} not in database.')


def del_user(id: int):
    if exists(id):
        del users[id]
    else:
        raise ValueError(f'Delete failure: {id} is not in users.')


def exists(name: str) -> bool:
    dbc.connect_db()
    return dbc.fetch_one(RESTAURANT_COLLECT, {NAME: name})


def update_rating(name: str, rating: int) -> bool:
    if not exists(name):
        raise ValueError(f'Update failure: {name} not in database.')
    else:
        dbc.connect_db()
        return dbc.update_doc(RESTAURANT_COLLECT, {NAME: name},
                              {RATING: rating})