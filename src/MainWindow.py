# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib,os
import hashlib


class Ui_DropboxEncryptionApp(object):
    def setupUi(self, DropboxEncryptionApp):
        DropboxEncryptionApp.setObjectName("DropboxEncryptionApp")
        DropboxEncryptionApp.resize(400, 300)
        DropboxEncryptionApp.setSizeGripEnabled(False)
        DropboxEncryptionApp.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(DropboxEncryptionApp)
        self.gridLayout.setObjectName("gridLayout")
        self.useridLabel = QtWidgets.QLabel(DropboxEncryptionApp)
        self.useridLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.useridLabel.setWordWrap(True)
        self.useridLabel.setObjectName("useridLabel")
        self.gridLayout.addWidget(self.useridLabel, 0, 0, 1, 1)
        self.passwdLabel = QtWidgets.QLabel(DropboxEncryptionApp)
        self.passwdLabel.setScaledContents(False)
        self.passwdLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.passwdLabel.setWordWrap(True)
        self.passwdLabel.setObjectName("passwdLabel")
        self.gridLayout.addWidget(self.passwdLabel, 1, 0, 1, 1)

        self.passwdText = QtWidgets.QLineEdit(DropboxEncryptionApp)
        self.passwdText.setObjectName("passwdText")
        self.passwdText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.passwdText, 1, 1, 1, 2)
        self.useridText = QtWidgets.QLineEdit(DropboxEncryptionApp)
        self.useridText.setObjectName("useridText")
        self.gridLayout.addWidget(self.useridText, 0, 1, 1, 2)

        self.newuserButton = QtWidgets.QPushButton(DropboxEncryptionApp)
        self.newuserButton.setObjectName("newuserButton")
        self.newuserButton.clicked.connect(self.on_newuserButton_clicked)

        self.gridLayout.addWidget(self.newuserButton, 3, 1, 1, 1)
        self.loginButton = QtWidgets.QPushButton(DropboxEncryptionApp)
        self.loginButton.setIconSize(QtCore.QSize(10, 16))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setDefault(True)
        self.gridLayout.addWidget(self.loginButton, 2, 1, 1, 1)

        self.retranslateUi(DropboxEncryptionApp)
        QtCore.QMetaObject.connectSlotsByName(DropboxEncryptionApp)

    def retranslateUi(self, DropboxEncryptionApp):
        _translate = QtCore.QCoreApplication.translate
        DropboxEncryptionApp.setWindowTitle(_translate("DropboxEncryptionApp", "Dropbox-with-Encrypted-Doc-Support"))
        DropboxEncryptionApp.setWindowIcon(QtGui.QIcon(QtGui.QPixmap("../resources/dropbox.png")))
        self.useridLabel.setText(_translate("DropboxEncryptionApp", "Username"))
        self.passwdLabel.setText(_translate("DropboxEncryptionApp", "Password"))
        self.newuserButton.setText(_translate("DropboxEncryptionApp", "New User"))
        self.loginButton.setText(_translate("DropboxEncryptionApp", "Login"))

    def on_newuserButton_clicked(self):
        self.newUserDialogCaller = newUserDialog()
        self.newUserDialogCaller.exec_()


class newUserDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(newUserDialog, self).__init__(parent)

        self.newUserLabel1 = QtWidgets.QLabel('Set New Username')
        self.newUserLabel2 = QtWidgets.QLabel('Set New Password')
        self.newUserLabel3 = QtWidgets.QLabel('Repeat Password')

        self.newUserText1 = QtWidgets.QLineEdit()
        self.newUserText2 = QtWidgets.QLineEdit()
        self.newUserText3 = QtWidgets.QLineEdit()
        self.newUserText2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newUserText3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.newUserButton1 = QtWidgets.QPushButton("Reset")
        self.newUserButton2 = QtWidgets.QPushButton("Submit")
        self.newUserButton2.clicked.connect(self.on_newUserSubmit_clicked)
        self.newUserButton1.clicked.connect(self.on_newUserReset_clicked)
        self.newUserButton2.setDefault(True)

        self.newUserFormLayout = QtWidgets.QFormLayout()
        self.newUserFormLayout.addRow(self.newUserLabel1, self.newUserText1)
        self.newUserFormLayout.addRow(self.newUserLabel2, self.newUserText2)
        self.newUserFormLayout.addRow(self.newUserLabel3, self.newUserText3)
        self.newUserFormLayout.addRow(self.newUserButton1, self.newUserButton2)

        self.setLayout(self.newUserFormLayout)
        self.resize(250, 200)
        self.setWindowTitle('New User Sign-up')
        self.show()

    def on_newUserSubmit_clicked(self):

        if (self.newUserText1.text() == '' or self.newUserText2.text() == '' or self.newUserText3.text() == ''):
            emptyErrMsg = QtWidgets.QMessageBox()
            emptyErrMsg.setText('Please fill up the details')
            emptyErrMsg.setWindowTitle('Error Message')
            emptyErrMsg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            emptyErrMsg.buttonClicked.connect(self.on_emptyErrMsgOK_clicked)
            emptyErrMsg.exec_()
        else:
            hash1 = hashlib.sha512()
            hash2 = hashlib.sha512()

            newuserid = self.newUserText1.text()
            hash1.update(self.newUserText2.text().encode())
            hash2.update(self.newUserText3.text().encode())
            newpasswd = hash1.hexdigest()
            confnewpasswd = hash2.hexdigest()
            # print(newpasswd+'\n'+confnewpasswd)

        if (newpasswd == confnewpasswd):
            succMsg = QtWidgets.QMessageBox()
            succMsg.setText('New User: ' + newuserid + '\nCreated Successfully')
            succMsg.setWindowTitle('New User Created')
            succMsg.exec_()

            try:
                file_path = '../resources/users'

                if os.path.isfile(file_path):
                    # users.cfg exists
                    # print(path_to_file_users)
                    # print("exists")
                    with open(file_path, 'a') as f:
                        f.write(newuserid+':'+newpasswd+'\n')
                        f.close()
                else:
                    # users.cfg does not exist
                    # print(path_to_file_users)
                    # print("not exists")
                    with open(file_path,'w+') as f:
                        f.write(newuserid+':'+newpasswd+'\n')
                        f.close()

            except FileNotFoundError:
                print(FileNotFoundError.strerror)
            #finally:
            #    newUserDialog.close(self)
            #    DropboxEncryptionApp.show(self)




        else:
            errmsg = QtWidgets.QMessageBox()
            errmsg.setWindowTitle('Error Message')
            errmsg.setText('Wrong Password')
            errmsg.setInformativeText('Repeated passwords must be same')

    def on_emptyErrMsgOK_clicked(i):
        print(i.text())

    def on_newUserReset_clicked(self):
        # print(1)
        resetmsg = QtWidgets.QMessageBox()
        resetmsg.setWindowTitle('Reset All Fields')
        resetmsg.setText('Do you wish to Reset all fields ?')
        resetmsg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        resetmsg.exec_()
        self.newUserText1.setText(" ")
        self.newUserText2.setText(" ")
        self.newUserText3.setText(" ")
        # self.newUserText2.textChanged(self, ' ')
        # self.newUserText3.textChanged(self, ' ')
        # print(2)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DropboxEncryptionApp = QtWidgets.QDialog()
    ui = Ui_DropboxEncryptionApp()
    ui.setupUi(DropboxEncryptionApp)
    DropboxEncryptionApp.show()
    sys.exit(app.exec_())
