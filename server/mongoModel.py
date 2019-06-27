import json
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
from flask_pymongo import PyMongo


builtin_list = list


mongo = None


def _id(id):
    if not isinstance(id, ObjectId):
        return ObjectId(id)
    return id

def init_app(app):
    global mongo

    mongo = PyMongo(app)
    mongo.init_app(app)


# [START read]
def read(email):
    try:
        result = mongo.db.users.find_one({'email': email})
        return result
    except:
        return json.dumps({'error': 'Error Connecting to DB'})
# [END read]


# [START create]
def create(data):
    try:
        user = read(data["email"])
        if not user:
            try:
                user = mongo.db.users.insert_one(data)
                return read(user.inserted_id)
            except:
                return json.dumps({'error': 'Error Connecting to DB'})
        return None
    except:
        return json.dumps({'error': 'Error Connecting to DB'})

    
# [END create]


# [START update]
def update(data, email):
    mongo.db.users.replace_one({'email': email}, data)
    return read(email)
# [END update]


def delete(email):
    mongo.db.users.delete_one({'email': email})