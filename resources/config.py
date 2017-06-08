from os.path import abspath, expanduser

"""
A simple configuration python file which
has all sorts of constants which are
used throughout our application.

"""

DESKTOP = '~\Desktop'
DOCUMENTS = '~\Documents'
DOWNLOADS = '~\Downloads'
PUBLIC_KEY_DIR = abspath('..\\resources\\keys\\public')
PRIVATE_KEY_DIR = abspath('..\\resources\\keys\\private')
SECRET_KEY_FILE = abspath('..\\uploads\\encrypted_files\\secret.key')
WINDOW_ICON = abspath('..\\resources\\dropbox.png')
USERS_SHADOW_FILE = abspath('..\\resources\\users.shadow')
ENC_FILE_DIR = abspath('..\\uploads\\encrypted_files')
DEC_FILE_DIR =  'C:\\Users\\Ashwin\\PycharmProjects\\DASec\\downloads\\decrypted_files'
COMPRESS_FILE_DIR = abspath('..\\uploads\\compressed_files')
COMPRESS_FILE_DOWNLOAD_DIR = 'C:\\Users\\Ashwin\\PycharmProjects\\DASec\\downloads\\compressed_files'
RSA_SIZE = 4096
RSA_ALGORITHM = "scryptAndAES256-CBC"
RSA_PKCS_FORMAT = 8
