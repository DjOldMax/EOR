import hashlib
import rsa


def MD5(value):
    result = hashlib.md5(value.encode())
    return result.hexdigest()

def SHA256(value):
    result = hashlib.sha256(value.encode())
    return result.hexdigest()

def RSA(value):
    (pubkey, privkey) = rsa.newkeys(512)
    crypto = rsa.encrypt(value.encode('utf8'), pubkey)
    return crypto
