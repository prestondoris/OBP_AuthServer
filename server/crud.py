import json
from server import get_model
from .authenticate import (
    verifyCredentials,
    authenticateClient, 
    generateToken, 
    tokenDuration
)
from flask import Blueprint, request
from passlib.hash import sha256_crypt

crud = Blueprint('crud', __name__)

@crud.route('/authenticate', methods=["POST"])
def read():
    email = request.form.get('email')
    password = request.form.get('password')
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')
    
    if None in [email, password, client_id, client_secret]:
        return json.dumps({
            "error": "invalid request"
        }), 400

    if not authenticateClient(client_id, client_secret):
        return json.dumps({
            "error", "Access Denied - client not authorized"
        }), 401
    
    user = get_model().read(email)
    print(user)
    if user:
        if not verifyCredentials(user['email'], password, user['password']):
            return json.dumps({
                "error": "Access Denied - invalid credentials"
            }), 401
        
        return returnToken(user)
    else:
        return json.dumps({
            "error": "User does not exist"
        }), 401
        


@crud.route('/register', methods=["POST"])
def create():
    email = request.form.get('email')
    password = hashPassword(request.form.get('password'))
    firstName = request.form.get('fName')
    lastName = request.form.get('lName')
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')
    
    if None in [email, password, firstName, lastName, client_id, client_secret]:
        return json.dumps({
            "error": "invalid request"
        }), 400
    
    if not authenticateClient(client_id, client_secret):
        return json.dumps({
        "error", "Access Denied - client not authorized"
    }), 401

    data = {
        'email': email,
        'password': password,
        'firstName': firstName,
        'lastName': lastName
    }
    user = get_model().create(data)
    print(user)
    if user:        
        return returnToken(user)
    else:
        return json.dumps({
            "error": "An error occurred adding the user to the DB."
        }), 401


# @crud.route('/updateUser', methods=['POST'])
# def updateUser():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     firstName = request.form.get('firstName')
#     lastName = request.form.get('lastName')
#     client_id = request.form.get('client_id')
#     client_secret = request.form.get('client_secret')

#     if None in [email, password, firstName, lastName, client_id, client_secret]:
#         return json.dumps({
#             "error": "invalid request"
#         }), 400

#     if not authenticateClient(client_id, client_secret):
#         return json.dumps({
#             "error", "Access Denied - client not authorized"
#         }), 401

#     user = get_model.read(email)
#     if user:
#         if not verifyCredentials(user['email'], password, user['password']):
#             return json.dumps({
#                 "error": "Access Denied - invalid credentials"
#             }), 401
            
#         data = {
#             'email': email,
#             'firstName': user['firstName'],
#             'lastName': user['lastName']
#         }
#         user = get_model().update(data, email)
#         return json.dumps({
#             'success': 'The password for ' + email + ' was reset'
#         }), 200
#     else:
#         return json.dumps({
#             "error": "User does not exist"
#         }), 401


@crud.route('/updatepassword', methods=["POST"])
def updatePW():
    email = request.form.get('email')
    oldPassword = request.form.get('oldPassword')
    newPassword = hashPassword(request.form.get('newPassword'))
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')

    if None in [email, oldPassword, newPassword, client_id, client_secret]:
        return json.dumps({
            "error": "invalid request"
        }), 400

    if not authenticateClient(client_id, client_secret):
        return json.dumps({
            "error", "Access Denied - client not authorized"
        }), 401

    user = get_model.read(email)
    if user:
        if not verifyCredentials(user['email'], oldPassword, user['password']):
            return json.dumps({
                "error": "Access Denied - invalid credentials"
            }), 401
            
        data = {
            'email': email,
            'password': newPassword
        }
        user = get_model().update(data, email)
        return json.dumps({
            'success': 'The password for ' + email + ' was reset'
        }), 200
    else:
        return json.dumps({
            "error": "User does not exist"
        }), 401
    

@crud.route('/delete', methods=["POST"])
def delete():
    email = request.form.get('email')
    password = request.form.get('password')
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')

    if None in [email, client_id, client_secret]:
        return json.dumps({
        "error": "invalid request"
    }), 400

    if not authenticateClient(client_id, client_secret):
        return json.dumps({
            "error", "Access Denied - client not authorized"
        }), 401

    get_model().delete(email)



def returnToken(user):
    authToken = generateToken()
    return json.dumps({
        'access_token': authToken,
        'token_type': 'JWT',
        'expires_in': tokenDuration,
        'firstName': user['firstName'],
        'lastName': user['lastName']
    })

def hashPassword(pw):
    return sha256_crypt.encrypt(pw)

