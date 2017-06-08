from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from resources import config as cfg

def decrypt_with_private_key(file_to_be_decrypted, private_key_file, code):
    with open(file_to_be_decrypted, 'rb') as f:
        private_key = RSA.import_key(
            open(private_key_file).read(),
            passphrase=code)
        enc_session_key, nonce, tag, ciphertext = [f.read(x)
                                                   for x in (private_key.size_in_bytes(),
                                                             16, 16, -1)]

        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        decrypted_data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        print('Success')
        return decrypted_data.decode()



def encrypt_with_public_key(encrypted_file, public_key_file, data_to_be_encrypted):

    with open(encrypted_file,'wb') as f:
        pub_key = RSA.import_key(open(public_key_file).read())
        session_key = get_random_bytes(16)
        cipher_rsa = PKCS1_OAEP.new(pub_key)
        f.write(cipher_rsa.encrypt(session_key))

        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data_to_be_encrypted)

        f.write(cipher_aes.nonce)
        f.write(tag)
        f.write(ciphertext)
        f.close()
        print('Success : ',encrypted_file)

def gen_key(code, private_key_file, public_key_file):
    __key = RSA.generate(cfg.RSA_SIZE)
    private_key = __key.exportKey(passphrase=code, pkcs=cfg.RSA_PKCS_FORMAT, protection=cfg.RSA_ALGORITHM)
    with open(private_key_file, 'wb') as prf:
        prf.write(private_key)
    with open(public_key_file, 'wb') as pubf:
        pubf.write(__key.publickey().exportKey())

#decrypt_with_private_key('C:\\Users\\Ashwin\\PycharmProjects\\DASec\\downloads\\compressed_files\\secret.key','C:\\Users\\Ashwin\\PycharmProjects\\DASec\\resources\\keys\\private\\ashwin.private','ashwinjoshi124@gmail.com')