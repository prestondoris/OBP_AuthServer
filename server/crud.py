import json
from .model import get_model
from .authenticate import (
    authenticateUserCredentials,
    authenticateClient, 
    generateAccessToken, 
    tokenDuration
)
from flask import Blueprint, request
from passlib.hash import sha256_crypt

crud = Blueprint('crud', __name__)
