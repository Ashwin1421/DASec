# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ashwin\PycharmProjects\DASec\src\DropboxClient\DropboxClientWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src.DropboxClient import DropboxClient, FileClient, QuestionDialog, DecryptClient, DownloadDecrypt
from src.Client import rsa_keyGen
from resources import config as cfg
import os


class Ui_DocSelectionDialog(object):
    def setupUi(self, DocSelectionDialog, passhash):
        self.passhash = passhash

        DocSelectionDialog.setObjectName("DocSelectionDialog")
        DocSelectionDialog.resize(620, 320)
        self.dropboxGroupBox = QtWidgets.QGroupBox(DocSelectionDialog)
        self.dropboxGroupBox.setGeometry(QtCore.QRect(10, 10, 600, 300))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.dropboxGroupBox.setFont(font)
        self.dropboxGroupBox.setObjectName("dropboxGroupBox")

        self.connectDropboxAccount = QtWidgets.QPushButton(self.dropboxGroupBox)
        self.connectDropboxAccount.setGeometry(QtCore.QRect(30, 130, 160, 25))
        self.connectDropboxAccount.setObjectName("connectDropboxAccount")
        self.connectDropboxAccount.clicked.connect(self.on_connectDropboxAccount_clicked)

        self.authLabel = QtWidgets.QLabel(self.dropboxGroupBox)
        self.authLabel.setGeometry(QtCore.QRect(30, 210, 160, 25))
        self.authLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.authLabel.setObjectName("authLabel")

        self.authText = QtWidgets.QLineEdit(self.dropboxGroupBox)
        self.authText.setGeometry(QtCore.QRect(200, 210, 340, 25))
        self.authText.setObjectName("authText")

        self.dropboxInstLabel = QtWidgets.QLabel(self.dropboxGroupBox)
        self.dropboxInstLabel.setGeometry(QtCore.QRect(20, 30, 520, 91))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)

        self.dropboxInstLabel.setFont(font)
        self.dropboxInstLabel.setObjectName("dropboxInstLabel")

        self.authLink = QtWidgets.QLabel(self.dropboxGroupBox)
        self.authLink.setGeometry(QtCore.QRect(30, 180, 160, 25))
        self.authLink.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.authLink.setObjectName("authLink")

        self.getAccessToken = QtWidgets.QPushButton(self.dropboxGroupBox)
        self.getAccessToken.setGeometry(QtCore.QRect(200, 240, 75, 25))
        self.getAccessToken.setObjectName("getAccessToken")
        self.getAccessToken.clicked.connect(self.on_getAccessToken_clicked)

        self.connectDropboxAccount.raise_()
        self.authText.raise_()
        self.authLabel.raise_()
        self.dropboxInstLabel.raise_()
        # self.authLink.raise_()
        # self.getAccessToken.raise_()

        self.retranslateUi(DocSelectionDialog)
        QtCore.QMetaObject.connectSlotsByName(DocSelectionDialog)

    def closeUi(self, DocSelectionDialog):
        DocSelectionDialog.close()

    def retranslateUi(self, DocSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        DocSelectionDialog.setWindowTitle(_translate("DocSelectionDialog", "Dropbox Client"))
        self.dropboxGroupBox.setTitle(_translate("DocSelectionDialog", "Dropbox Connection"))
        self.connectDropboxAccount.setText(_translate("DocSelectionDialog", "Generate Authorization Link"))
        self.authLabel.setText(_translate("DocSelectionDialog", "Paste Authorization Code Here :"))
        self.dropboxInstLabel.setText(_translate("DocSelectionDialog",
                                                 "1. Once you push the \"Connect Dropbox\" button, your browser will open a page.\n"
                                                 "2. You will be prompted to Log into your Dropbox Account.\n"
                                                 "3. Copy the Authorization Code presented to you and paste it down here."))
        self.authLink.setText(_translate("DocSelectionDialog", "Authorization Link :"))
        self.getAccessToken.setText(_translate("DocSelectionDialog", "Go"))

    """
    Method : on_connectDropboxAccount_clicked
    Param : self
    Description :
        This method generates a URL for authorizing our app
        to use the user's Dropbox Account.
    """
    def on_connectDropboxAccount_clicked(self):
        self.authURL = DropboxClient.get_auth_url(self)
        self.authURL_label = QtWidgets.QLabel(self.dropboxGroupBox)
        self.authURL_label.setGeometry(QtCore.QRect(200, 180, 340, 25))
        # print(self.authURL)
        self.authURL_new = '<a href="' + self.authURL + '\">' + self.authURL + '</a>'
        self.authURL_label.setText(self.authURL_new)
        self.authURL_label.show()
        self.authURL_label.setOpenExternalLinks(True)


    """
    Method : on_getAccessToken
    Param : self
    Description :
        This method gets the Dropbox OAuth Authentication Token and then gets all the
        details from the associated Dropbox Account such as :-
            client_email = email address associated with the Dropbox Account
            client_uid = unique user identifier
            client_email_verified = boolean value :- True if authentic user of Dropbox, False otherwise.
    """
    def on_getAccessToken_clicked(self):
        self.auth_code = self.authText.text()
        self.auth_client = DropboxClient.get_access_token(self, self.auth_code)

        self.client_dict = self.auth_client.account_info()
        # print(self.auth_client.account_info())
        # print(self.client_dict)
        self.client_email = self.client_dict['email']
        self.client_uid = self.client_dict['uid']
        self.client_name_details = self.client_dict['name_details']
        self.client_email_verified = self.client_dict['email_verified']
        self.client_given_name = self.client_name_details['given_name']



        if (self.client_email_verified is True):

            try:

                qdialog = QtWidgets.QDialog()
                qdialog_ui = QuestionDialog.Ui_QuestionDialog()
                qdialog_ui.setupUi(qdialog)
                qdialog.exec_()

                if qdialog_ui.sendFilesOption.isChecked() == True:

                    FileClientDialog = QtWidgets.QDialog()
                    file_client_ui = FileClient.Ui_FileClientDialog()
                    # print(self.auth_client)
                    file_client_ui.setupUi(FileClientDialog, self.auth_client, self.passhash)
                    FileClientDialog.exec()

                elif qdialog_ui.receiveFilesOption.isChecked() == True:

                    user_private_key_file = cfg.PRIVATE_KEY_DIR + '\\' + self.client_given_name.lower() + '.private'
                    if not os.path.exists(user_private_key_file):
                        print('Error : Private Key not found.')
                    download_dialog = QtWidgets.QDialog()
                    download_dialog_ui = DecryptClient.Ui_DecryptionDialog()
                    download_dialog_ui.setupUi(download_dialog, private_key_file=user_private_key_file, code=self.client_email)
                    download_dialog.exec_()
            except Exception as e:
                print("Exception",e.__traceback__)
