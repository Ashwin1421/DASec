#!/usr/bin/python3

from Crypto import Random
from Crypto.Cipher import AES
from hashlib import sha256
from resources import config as cfg
import os
"""
An utility to generate secret key and encrypt and decrypt files.
"""

def get_key(code):
    return hash_value(code)

"""
Return hash value of any text.
"""
def hash_value(text):
    hash = hashlib.sha512()
    hash.update(text.encode())
    return hash.hexdigest()

"""
Use padding for AES encryption.
"""
def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

"""
Encryption of a message.
"""
def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

"""
Decryption of a message.
"""
def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

"""
Uses encrypt() method to encrypt contents of any file
and then saves the encrypted file to a predefined directory.
"""
def encrypt_file(file_name, key):

    try:
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
            fo.close()

        hash_key = sha256()
        hash_key.update(key)
        new_key = hash_key.digest()

        #print(new_key)
        enc = encrypt(plaintext, new_key)
        new_file_name = cfg.ENC_FILE_DIR + '\\' + os.path.basename(file_name)
        with open(new_file_name + ".enc", 'wb') as fo:
            fo.write(enc)
            fo.close()

        return True

    except Exception:

        return False
"""
Uses decrypt() method to decrypt contents of an encrypted file
and saves decrypted files to a predefined directory.
"""
def decrypt_file(file_name, key):

    try:
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
            fo.close()

        hash_key = sha256()
        hash_key.update(key)
        new_key = hash_key.digest()

        dec = decrypt(ciphertext, new_key)

        new_file_name = cfg.DEC_FILE_DIR + '\\' + os.path.basename(file_name)
        with open(new_file_name.rstrip('.enc'), 'wb') as fo:
            fo.write(dec)
            fo.close()

        print('Success')
        return True
    except Exception:
        print('Failure')
        return False
