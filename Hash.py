import time
import hashlib
# import bcrypt

key = b"hello"

print(hashlib.sha256(key).hexdigest())

def djb2(key):
    hash_value = 5381
    
    for char in key:
        hash_value = ((hash_value << 5)+hash_value) + char
    return hash_value

print(djb2(key))