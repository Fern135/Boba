from django.core.signing import Signer
from django.core import signing 
from django.contrib.auth.hashers import make_password, check_password
from ..util.util import error
signer = Signer()  # cryptography signing


def encrypt(data) -> str:
    return make_password(data)


def checkPassword(password, hashed_password) -> bool:
    if check_password(password, hashed_password):
        return True
    else:
        return False


def sign(data:str) -> str: # returns data as an encrypted string
    try:
        return signer.sign(data)

    except signing.BadSignature:
        return f"{error} * error: tampering detected"


def unSign(data:str) -> str: # returns data as an un-encrypted string
    try:
        return signer.unsign(data)
    except signing.BadSignature:
        return f"{error} * error: tampering detected"


def signObj(obj:object):  # returns obj as an encrypted
    try:
        return signer.sign_object(obj)
    except signing.BadSignature:
        return f"{error} * error: tampering detected"


def unSignObj(obj:object):  # returns obj as an un-encrypted
    try:
        return signer.unsign_object(obj)
    except signing.BadSignature:
        return f"{error} * error: tampering detected"
