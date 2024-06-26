import os

import pymongo as pm

LOCAL = "0"
CLOUD = "1"

USERS_DB = 'databasesplusoneDB'

client = None

MONGO_ID = '_id'


# def connect_db():
#     """
#     This provides a uniform way to connect to the DB across all uses.
#     Returns a mongo client object... maybe we shouldn't?
#     Also set global client variable.
#     We should probably either return a client OR set a
#     client global.
#     """
#     global client
#     if client is None:  # not connected yet!
#         print("Setting client because it is None.")
#         if os.environ.get("CLOUD_MONGO", LOCAL) == CLOUD:
#             password = os.environ.get("MONGODB_PASSWORD")
#             if not password:
#                 raise ValueError('You must set your password '
#                                  + 'to use Mongo in the cloud.')
#             print("Connecting to Mongo in the cloud.")
#             client = pm.MongoClient(f'mongodb+srv://cm5685:{password}'
#                                     + '@databasesplusone.zrimlpx.mongodb.net'
#                                     + '/?retryWrites=true&w=majority',
#                                     connectTimeoutMS=30000,
#                                     socketTimeoutMS=None, connect=False,
#                                     maxPoolsize=1)
#         else:
#             print("Connecting to Mongo locally.")
#             client = pm.MongoClient()


# connect to MongoDB
def connect_db():
    global client
    if client is None:
        print("Setting client because it is None.")
        mongodb_uri = os.environ.get("MONGODB_URI")
        if mongodb_uri:
            print("Connecting to MongoDB.")
            client = pm.MongoClient(mongodb_uri)
        else:
            raise ValueError("MONGODB_URI environment variable is not set.")


def insert_one(collection, doc, db=USERS_DB):
    """
    Insert a single doc into collection.
    """
    print(f'{db=}')
    return client[db][collection].insert_one(doc)


def fetch_one(collection, filt, db=USERS_DB):
    """
    Find with a filter and return on the first doc found.
    """
    for doc in client[db][collection].find(filt):
        if MONGO_ID in doc:
            # Convert mongo ID to a string so it works as JSON
            doc[MONGO_ID] = str(doc[MONGO_ID])
        return doc


def del_one(collection, filt, db=USERS_DB):
    """
    Find with a filter and return on the first doc found.
    """
    client[db][collection].delete_one(filt)


def delete_all(collection, db=USERS_DB):
    """
    Delete all documents in the specified collection.
    """
    result = client[db][collection].delete_many({})
    return result.deleted_count


def fetch_all(collection, db=USERS_DB):
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret


def fetch_all_filtered(collection, filt={}, db=USERS_DB):
    ret = []
    for doc in client[db][collection].find(filt):
        doc.pop(MONGO_ID, None)
        ret.append(doc)
    return ret


def fetch_all_as_dict(key, collection, db=USERS_DB):
    ret = {}
    for doc in client[db][collection].find():
        doc[MONGO_ID] = str(doc[MONGO_ID])
        ret[doc[key]] = doc
    return ret


def update_doc(collection, filters, update_dict, db=USERS_DB):
    return client[db][collection].update_one(filters, {'$set': update_dict})
