from resources import config as cfg
from src.Client import newAES, rsa_keyGen
from zipfile import ZipFile
import webbrowser, os, time



def download_and_decrypt(url, private_key_file, code):

    print('Please Save file to app downloads folder')
    webbrowser.open(url)
    time.sleep(30)
    downloads_path = cfg.COMPRESS_FILE_DOWNLOAD_DIR + '\\'
    for file in os.listdir(downloads_path):
        if file.endswith('.zip'):
            zip_name = os.path.join(downloads_path,file)
            if os.path.exists(zip_name):
                zf = ZipFile(zip_name)
                zf.extractall(path=downloads_path)
                zf.close()
                break

    for file in os.listdir(downloads_path):
        if file.endswith('.key'):
            file_to_decrypt = os.path.join(downloads_path,file)
            if os.path.exists(file_to_decrypt):
                secret_key = rsa_keyGen.decrypt_with_private_key(file_to_decrypt,private_key_file, code)

    for file in os.listdir(downloads_path):
        if file.endswith('.enc'):
            file_name = os.path.join(downloads_path,file)
            if os.path.exists(file_name):
                newAES.decrypt_file(file_name,secret_key.encode())

    """
    path = cfg.COMPRESS_FILE_DOWNLOAD_DIR.replace('src\\','')
    for (root, dir, files) in os.walk(path):
        for file in files:
            if '.zip' in file:
                selected_zip_file = os.path.join(root,file)

    zf = zipfile.ZipFile(selected_zip_file,'r')
    zf.extractall(path=root+'\\')
    zf.close()

    for (root, dir, files) in os.walk(path):
        for file in files:

            if '.zip' in file:
                os.remove(os.path.join(root,file))

            if 'secret.key' in file:
                secret_key_dec = rsa_keyGen.decrypt_with_private_key(os.path.join(root,file), private_key_file, code)


    for (root, dir, files) in os.walk(path):
        for file in files:
            if '.enc' in file:
                newAES.decrypt_file(os.path.join(root,file), secret_key_dec.encode())
    """

