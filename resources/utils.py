from resources import config as cfg
import zipfile, os, datetime, time, hashlib, src.Client.rsa_keyGen as rsa


def gen_hash_list(dir, pub_key_file):
    for file in os.listdir(dir):
        if file.endswith('.enc'):
            file_hash = get_file_hash(os.path.join(dir,file))
            enc_hash_file = dir + '/' + file + '.hash'
            rsa.encrypt_with_public_key(enc_hash_file , pub_key_file , file_hash.encode())

def get_file_hash(file):
    hash_obj = hashlib.sha256()
    with open(file, 'rb') as f:
        buf = f.read()
        hash_obj.update(buf)
        f.close()
    return hash_obj.hexdigest()

def get_timestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y-%H-%M-%S')
    return str(st)

def create_zip_file(dir):
    zip_file_name = get_timestamp() + '.zip'
    new_zip_file_name = cfg.COMPRESS_FILE_DIR + '\\' + zip_file_name
    zipf = zipfile.ZipFile(new_zip_file_name, 'w', zipfile.ZIP_DEFLATED, allowZip64=True)
    for root, dirs, files in os.walk(dir):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=file)
    zipf.close()

    return new_zip_file_name


def get_user_and_pass_list():

    users = []
    user_email_list = []
    pass_hash_list = []
    try:
        with open(cfg.USERS_SHADOW_FILE,'r') as f:
            for line in f.readlines():
                users.append(line.split(':')[0])
                user_email_list.append(line.split(':')[1])
                pass_hash_list.append(line.split(':')[2].rstrip())
                f.close()

    except FileNotFoundError as e:
        print(e.strerror)

    return users, user_email_list, pass_hash_list
