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
    crypto = rsa.encrypt(value.encode('utf8'), pubkey)
    info=crypto
    return info,privkey

def RSA_decrypt(value,privkey):
    decrypto = rsa.decrypt(value, privkey)
    return decrypto

# res = RSA_crypt('hello')
# print(RSA_crypt('hello'))
# res_=RSA_decrypt(res[0], res[1])
# print(res_)