# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ashwin\PycharmProjects\DASec\src\DropboxClient\DownloadAndDecrypt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os, resources.config as cfg, zipfile, src.Client.newAES as newAES, src.Client.rsa_keyGen as rsa_keyGen, resources.utils as utils

class Ui_DecryptionDialog(object):
    def setupUi(self, DecryptionDialog, private_key_file, code):
        self.code =code
        self.private_key_file = private_key_file
        DecryptionDialog.setObjectName("DecryptionDialog")
        DecryptionDialog.resize(620, 180)
        self.decryptGroupBox = QtWidgets.QGroupBox(DecryptionDialog)
        self.decryptGroupBox.setGeometry(QtCore.QRect(10, 10, 600, 160))
        self.decryptGroupBox.setObjectName("decryptGroupBox")
        self.descLabel = QtWidgets.QLabel(self.decryptGroupBox)
        self.descLabel.setGeometry(QtCore.QRect(20, 20, 160, 20))
        self.descLabel.setObjectName("descLabel")
        self.downloadedFilePath = QtWidgets.QLineEdit(self.decryptGroupBox)
        self.downloadedFilePath.setGeometry(QtCore.QRect(140, 60, 401, 25))
        self.downloadedFilePath.setObjectName("downloadedFilePath")
        self.decryptButton = QtWidgets.QPushButton(self.decryptGroupBox)
        self.decryptButton.setGeometry(QtCore.QRect(20, 100, 100, 25))
        self.decryptButton.setObjectName("decryptButton")
        self.decryptButton.clicked.connect(self.decrypt_files)
        self.downloadFileBrowser = QtWidgets.QPushButton(self.decryptGroupBox)
        self.downloadFileBrowser.setGeometry(QtCore.QRect(20, 60, 100, 25))
        self.downloadFileBrowser.setObjectName("downloadFileBrowser")
        self.downloadFileBrowser.clicked.connect(self.browse_file)

        self.retranslateUi(DecryptionDialog)
        QtCore.QMetaObject.connectSlotsByName(DecryptionDialog)

    def retranslateUi(self, DecryptionDialog):
        _translate = QtCore.QCoreApplication.translate
        DecryptionDialog.setWindowTitle(_translate("DecryptionDialog", "Decrypt Files"))
        self.decryptGroupBox.setTitle(_translate("DecryptionDialog", "Decrypt Files"))
        self.descLabel.setText(_translate("DecryptionDialog", "Select Downloaded File"))
        self.decryptButton.setText(_translate("DecryptionDialog", "Decrypt"))
        self.downloadFileBrowser.setText(_translate("DecryptionDialog", "Browse"))


    def browse_file(self):
        self.file_dialog = QtWidgets.QFileDialog()
        self.file_path = self.file_dialog.getOpenFileName(directory=os.path.expanduser(cfg.DOWNLOADS))
        self.downloadedFilePath.setText(self.file_path[0])

    def decrypt_files(self):

        if os.path.exists(self.file_path[0]):
            self.file_name = os.path.basename(self.file_path[0])
            extract_path = os.path.join(os.path.expanduser(cfg.DOWNLOADS),self.file_name.rstrip('.zip') +'/')
            zf = zipfile.ZipFile(self.file_path[0])
            zf.extractall(path=extract_path)
            zf.close()

            enc_file_hash_list = []
            if os.path.exists(extract_path):
                for file in os.listdir(extract_path):
                    if file.endswith('.hash'):
                        file_to_decrypt = os.path.join(extract_path,file)
                        if os.path.exists(file_to_decrypt):
                            dec_hash = rsa_keyGen.decrypt_with_private_key(file_to_decrypt, self.private_key_file, self.code)
                            enc_file_hash_list.append(dec_hash)


                for file in os.listdir(extract_path):
                    if file.endswith('.key'):
                        file_to_decrypt = os.path.join(extract_path,file)
                        if os.path.exists(file_to_decrypt):
                            secret_key = rsa_keyGen.decrypt_with_private_key(file_to_decrypt,self.private_key_file,self.code)
                            #print(secret_key)
                            self.decrypt_all_files(secret_key,extract_path,enc_file_hash_list)



        else:
            print('No such file exists')

    def decrypt_all_files(self,secret_key,extract_path,hash_list):

        for file in os.listdir(extract_path):
            if file.endswith('.enc'):
                file_name = os.path.join(extract_path, file)
                file_hash = utils.get_file_hash(file_name)
                if file_hash in hash_list:
                    print('Integrity OK')
                    b = newAES.decrypt_file(file_name, secret_key.encode())

        if b is True:
            succ = QtWidgets.QMessageBox()
            succ.setWindowTitle('Files decrypted successfully')
            succ.setText('All files checked for integrity and decrypted successfully.')
            succ.exec_()
            os.startfile(cfg.DEC_FILE_DIR)
        else:
            fail = QtWidgets.QMessageBox()
            fail.setWindowTitle('Integrity Compromised')
            fail.setText('One or more documents were maliciously modified.')
            fail.exec_()