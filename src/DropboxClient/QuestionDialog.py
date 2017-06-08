# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ashwin\PycharmProjects\DASec\src\DropboxClient\QuestionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QuestionDialog(object):
    def setupUi(self, QuestionDialog):
        QuestionDialog.setObjectName("QuestionDialog")
        QuestionDialog.resize(198, 92)
        self.sendFilesOption = QtWidgets.QRadioButton(QuestionDialog)
        self.sendFilesOption.setGeometry(QtCore.QRect(20, 20, 120, 20))
        self.sendFilesOption.setObjectName("sendFilesOption")
        self.receiveFilesOption = QtWidgets.QRadioButton(QuestionDialog)
        self.receiveFilesOption.setGeometry(QtCore.QRect(20, 50, 120, 20))
        self.receiveFilesOption.setObjectName("receiveFilesOption")

        self.retranslateUi(QuestionDialog)
        QtCore.QMetaObject.connectSlotsByName(QuestionDialog)

    def retranslateUi(self, QuestionDialog):
        _translate = QtCore.QCoreApplication.translate
        QuestionDialog.setWindowTitle(_translate("QuestionDialog", "Select Option"))
        self.sendFilesOption.setText(_translate("QuestionDialog", "Send Files"))
        self.receiveFilesOption.setText(_translate("QuestionDialog", "Receive Files"))

