
from PyQt5 import QtCore, QtGui, QtWidgets
from src.Client import newAES, rsa_keyGen
from src.DropboxClient import EmailDownloadLink, DownloadAndDecrypt, DropboxClientWindow
import dropbox, zipfile
from resources import config as cfg, utils
import os
from validate_email import validate_email


class Ui_FileClientDialog(QtWidgets.QDialog):

    """
    UI Related methods.
    Method : setupUI
    Param : FileClientDialog Dialog, auth_client variable, passhash variable
    Description :
        Setups all UI elements of FileClientDialog and uses auth_client and passhash objects to
        use them in further operations by different methods.
    """
    def setupUi(self, FileClientDialog, auth_client, passhash):

        self.auth_client = auth_client
        self.passhash = passhash

        #dc = QtWidgets.QDialog()
        #ui = DCW.Ui_DocSelectionDialog()
        #ui.setupUi(dc, self.passhash)
        #

        FileClientDialog.setObjectName("FileClientDialog")
        FileClientDialog.resize(620, 420)
        self.fileSelectionGroupBox = QtWidgets.QGroupBox(FileClientDialog)
        self.fileSelectionGroupBox.setGeometry(QtCore.QRect(10, 10, 600, 400))
        self.fileSelectionGroupBox.setObjectName("fileSelectionGroupBox")

        self.fileListLabel = QtWidgets.QLabel(self.fileSelectionGroupBox)
        self.fileListLabel.setGeometry(QtCore.QRect(20, 30, 120, 25))
        self.fileListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileListLabel.setObjectName("fileListLabel")

        self.selectFileButton = QtWidgets.QPushButton(self.fileSelectionGroupBox)
        self.selectFileButton.setGeometry(QtCore.QRect(140, 30, 120, 25))
        self.selectFileButton.setObjectName("selectFileButton")
        self.selectFileButton.clicked.connect(self.on_selectFileButton_clicked)

        self.fileListWidget = QtWidgets.QListWidget(self.fileSelectionGroupBox)
        self.fileListWidget.setGeometry(QtCore.QRect(20, 70, 550, 220))
        self.fileListWidget.setObjectName("fileListWidget")

        self.userSelectlabel = QtWidgets.QLabel(self.fileSelectionGroupBox)
        self.userSelectlabel.setGeometry(QtCore.QRect(20, 300, 120, 25))
        self.userSelectlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userSelectlabel.setObjectName("userSelectlabel")

        self.selectUserComboBox = QtWidgets.QComboBox(self.fileSelectionGroupBox)
        self.selectUserComboBox.setGeometry(QtCore.QRect(140, 300, 280, 25))
        self.selectUserComboBox.setObjectName("selectUserComboBox")


        self.user_list, self.email_list, self.pass_hash_list = utils.get_user_and_pass_list()

        for user,email in zip(self.user_list,self.email_list):
            self.selectUserComboBox.addItem(user.capitalize() + ' , ' + email)

        self.encryptAndSendButton = QtWidgets.QPushButton(self.fileSelectionGroupBox)
        self.encryptAndSendButton.setGeometry(QtCore.QRect(140, 350, 120, 25))
        self.encryptAndSendButton.setObjectName("encryptAndSendButton")
        self.encryptAndSendButton.clicked.connect(self.upload_and_send)




        self.retranslateUi(FileClientDialog)
        QtCore.QMetaObject.connectSlotsByName(FileClientDialog)

    def retranslateUi(self, FileClientDialog):
        _translate = QtCore.QCoreApplication.translate
        FileClientDialog.setWindowTitle(_translate("FileClientDialog", "Dialog"))
        self.fileSelectionGroupBox.setTitle(_translate("FileClientDialog", "Select Files to Upload"))
        self.selectFileButton.setText(_translate("FileClientDialog", "Select File(s)"))
        self.fileListLabel.setText(_translate("FileClientDialog", "List of selected files"))
        self.encryptAndSendButton.setText(_translate("FileClientDialog", "Encrypt and Send"))
        self.userSelectlabel.setText(_translate("FileClientDialog", "Select User(s) to Send :"))


    """
    Method : on_selectFileButton_clicked
    Description : Selects multiple files for uploading.
    """
    def on_selectFileButton_clicked(self):

        self.file_select_dialog = QtWidgets.QFileDialog()
        self.file_list = self.file_select_dialog.getOpenFileNames(directory=os.path.expanduser(cfg.DESKTOP))
        for file_item in self.file_list:
            # item = QtWidgets.QListWidgetItem(self.fileListWidget)
            # item.setText(i)
            for file in file_item:
                #print(j)
                self.fileListWidget.addItem(os.path.basename(file))

        self.fileListWidget.show()


    """
    Method : upload_and_send()
    Param : self
    Description :
        This method doesn't really do anything important as its name suggests,
        but it's responsible in preparing the next method <encrypt_files> with
        all the necessary parameters to actually execute those operations.
        This method is responsible to encrypt a secret key file with the
        receiver's public key.

    """
    def upload_and_send(self):
        self.client_dict = self.auth_client.account_info()
        # print(self.auth_client.account_info())
        # print(self.client_dict)
        self.client_email = self.client_dict['email']
        self.client_uid = self.client_dict['uid']
        self.client_name_details = self.client_dict['name_details']
        self.client_email_verified = self.client_dict['email_verified']
        self.total_files = self.file_list[0]

        #sec_file = str(os.path.abspath(cfg.SECRET_KEY_FILE)).replace('\\','/')
        #self.total_files.append(sec_file)


        self.selectedUserDetails = self.selectUserComboBox.currentText().split(',')


        if validate_email(self.selectedUserDetails[1]):
            self.pub_key_name = self.selectedUserDetails[0].lower()
            self.pub_key_file = cfg.PUBLIC_KEY_DIR + '\\' + self.pub_key_name.rstrip() + '.public'
            #print(self.pub_key_file)
            if os.path.isfile(self.pub_key_file):

                rsa_keyGen.encrypt_with_public_key(cfg.SECRET_KEY_FILE ,self.pub_key_file, self.passhash.encode())
                self.encrypt_files(self.total_files)

            else:
                print('something went wrong')




    """
        Method : encrypt_files
        Param : list of files <files>
        Description :
            This method takes in a list of files and encrypts them using a secret key.
            Each file is encrypted with AES 256-bit secret key.
            Encrypted Files are temporarily stored within this app's
            directory. Using these encrypted files, a simple compressed file is built
            which also includes a key file which contains the secret key which encrypted
            those files. This secret key file is further encrypted using the receiver's
            public key which the sender has.

    """

    def encrypt_files(self, files):
        #print(self.passhash)

        for file in files:
            if newAES.encrypt_file(file, self.passhash.encode()) is True:
                flag = True
            else:
                flag = False

        if flag is True:

            utils.gen_hash_list(cfg.ENC_FILE_DIR, self.pub_key_file)
            zip_name = utils.create_zip_file(cfg.ENC_FILE_DIR)
            try:

                if os.path.exists(zip_name):
                    with open(zip_name,'rb') as zf:
                        self.auth_client.put_file('/'+os.path.basename(zip_name), zf, overwrite=True)
                        zf.close()

                share_data = self.auth_client.share('/' + os.path.basename(zip_name), short_url=False)
                share_url = share_data['url']

                emaildialog = QtWidgets.QDialog()
                emaildialog_ui = EmailDownloadLink.Ui_EmailDownloadLink()
                emaildialog_ui.setupUi(emaildialog)
                #emaildialog.exec_()
                share_url_text = QtWidgets.QLineEdit(emaildialog)
                share_url_text.setGeometry(QtCore.QRect(100,20,500,25))
                share_url_text.copy()
                share_url_text.setText(share_url)
                share_url_text.show()
                emaildialog.exec_()

            except dropbox.rest.ErrorResponse as e:
                print(e.error_msg)

            succMsg = QtWidgets.QMessageBox()
            succMsg.setText('All files successfully encrypted and uploaded.')
            succMsg.setWindowTitle('Files Encrypted')
            succMsg.exec_()

            """
            Do cleanup of directories where you locally store Encrypted documents and
            zipped files of the encrypted files and the encrypted key file

            """
            for fi in os.listdir(cfg.ENC_FILE_DIR):
                fi_path = os.path.join(cfg.ENC_FILE_DIR,fi)
                try:
                    if os.path.isfile(fi_path):
                        os.remove(fi_path)
                except Exception as e:
                    print(e)

            for fi in os.listdir(cfg.COMPRESS_FILE_DIR):
                fi_path = os.path.join(cfg.COMPRESS_FILE_DIR, fi)
                try:
                    if os.path.isfile(fi_path):
                        os.remove(fi_path)
                except Exception as e:
                    print(e)
