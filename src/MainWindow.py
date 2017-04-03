# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.useridLabel = QtWidgets.QLabel(Dialog)
        self.useridLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.useridLabel.setWordWrap(True)
        self.useridLabel.setObjectName("useridLabel")
        self.gridLayout.addWidget(self.useridLabel, 0, 0, 1, 1)
        self.passwdLabel = QtWidgets.QLabel(Dialog)
        self.passwdLabel.setScaledContents(False)
        self.passwdLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passwdLabel.setWordWrap(True)
        self.passwdLabel.setObjectName("passwdLabel")
        self.gridLayout.addWidget(self.passwdLabel, 1, 0, 1, 1)
        self.passwdText = QtWidgets.QLineEdit(Dialog)
        self.passwdText.setObjectName("passwdText")
        self.gridLayout.addWidget(self.passwdText, 1, 1, 1, 2)
        self.useridText = QtWidgets.QLineEdit(Dialog)
        self.useridText.setObjectName("useridText")
        self.gridLayout.addWidget(self.useridText, 0, 1, 1, 2)
        self.newuserButton = QtWidgets.QPushButton(Dialog)
        self.newuserButton.setObjectName("newuserButton")
        self.gridLayout.addWidget(self.newuserButton, 3, 1, 1, 1)
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setIconSize(QtCore.QSize(10, 16))
        self.loginButton.setObjectName("loginButton")
        self.gridLayout.addWidget(self.loginButton, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.useridLabel.setText(_translate("Dialog", "Username"))
        self.passwdLabel.setText(_translate("Dialog", "Password"))
        self.newuserButton.setText(_translate("Dialog", "New User"))
        self.loginButton.setText(_translate("Dialog", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

