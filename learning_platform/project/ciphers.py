import hashlib
import rsa


def MD5_crypt(value):
    result = hashlib.md5(value.encode())
    return result.hexdigest()

def MD5_decrypt(value):
    result = hashlib.md5(value.encode())
    return result.hexdigest()

def SHA256_crypt(value):
    result = hashlib.sha256(value.encode())
    return result.hexdigest()

def SHA256_decrypt(value):
    result = hashlib.sha256(value.encode())
    return result.hexdigest()


def RSA_crypt(value):
    (pubkey, privkey) = rsa.newkeys(512)
    print(privkey)
    print(type(privkey))
    crypto = rsa.encrypt(value.encode('utf8'), pubkey)
    info=[pubkey, privkey, crypto]
    return info

def RSA_decrypt(value,privkey):
    decrypto = rsa.decrypt(value, privkey)
    return decrypto
