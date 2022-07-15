import hashlib


def MD5(value):
    result = hashlib.md5(value.encode())
    return result.hexdigest()

def SHA256(value):
    result = hashlib.sha256(value.encode())
    return result.hexdigest()

