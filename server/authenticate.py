import cryptography
import jwt
import time
from os.path import abspath 
from server import get_model
from passlib.hash import sha256_crypt

ISSUER = 'sample-auth-server'
tokenDuration = 900000

global privateKeyPath

privateKeyPath = abspath('private.pem')
with open(privateKeyPath, 'rb') as file:
    private_key = file.read()

def verifyCredentials (email, password, hashedPW):
    isAuth = sha256_crypt.verify(password, hashedPW)
    if isAuth:
        return True
    else:
        return False


def authenticateClient(clientId, clientSecret):
    if(clientId == 'client' and clientSecret == 'secret'):
        return True
    else:
        return False


def generateToken():
    payload = {
        'iss': ISSUER,
        'exp': time.time() + tokenDuration
    }

    access_token = jwt.encode(payload, private_key, algorithm='RS256')

    return access_token.decode()