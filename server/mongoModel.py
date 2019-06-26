from bson.objectid import ObjectId
from bson.json_util import dumps, loads
from flask_pymongo import PyMongo


builtin_list = list


mongo = None


def _id(id):
    if not isinstance(id, ObjectId):
        return ObjectId(id)
    return id


# [START from_mongo]
def from_mongo(data):
    """
    Translates the MongoDB dictionary format into the format that's expected
    by the application.
    """
    if not data:
        return None
    print(data)
    data['_id'] = str(data['_id'])
    return data
# [END from_mongo]


def init_app(app):
    global mongo

    mongo = PyMongo(app)
    mongo.init_app(app)


# [START read]
def read(email):
    result = mongo.db.users.find_one({'email': email})
    return result
# [END read]

# [START create]
def create(data):
    user = read(data["email"])
    if not user:
        user = mongo.db.users.insert_one(data)
        return read(user.inserted_id)
    return user
# [END create]


# [START update]
def update(data, email):
    mongo.db.users.replace_one({'email': email}, data)
    return read(email)
# [END update]


def delete(email):
    mongo.db.users.delete_one({'email': email})