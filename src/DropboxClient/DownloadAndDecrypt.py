# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ashwin\PycharmProjects\DASec\src\DropboxClient\DownloadAndDecrypt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadDialog(object):
    def setupUi(self, DownloadDialog):
        DownloadDialog.setObjectName("DownloadDialog")
        DownloadDialog.resize(620, 220)
        self.downloadAndDecryptGroupBox = QtWidgets.QGroupBox(DownloadDialog)
        self.downloadAndDecryptGroupBox.setGeometry(QtCore.QRect(10, 10, 600, 200))
        self.downloadAndDecryptGroupBox.setObjectName("downloadAndDecryptGroupBox")
        self.downloadLinkLabel = QtWidgets.QLabel(self.downloadAndDecryptGroupBox)
        self.downloadLinkLabel.setGeometry(QtCore.QRect(20, 20, 160, 20))
        self.downloadLinkLabel.setObjectName("downloadLinkLabel")
        self.downloadLinkLineEdit = QtWidgets.QLineEdit(self.downloadAndDecryptGroupBox)
        self.downloadLinkLineEdit.setGeometry(QtCore.QRect(20, 60, 560, 20))
        self.downloadLinkLineEdit.setObjectName("downloadLinkLineEdit")
        self.downloadButton = QtWidgets.QPushButton(self.downloadAndDecryptGroupBox)
        self.downloadButton.setGeometry(QtCore.QRect(20, 100, 160, 25))
        self.downloadButton.setObjectName("downloadButton")

        self.retranslateUi(DownloadDialog)
        QtCore.QMetaObject.connectSlotsByName(DownloadDialog)

    def retranslateUi(self, DownloadDialog):
        _translate = QtCore.QCoreApplication.translate
        DownloadDialog.setWindowTitle(_translate("DownloadDialog", "Dialog"))
        self.downloadAndDecryptGroupBox.setTitle(_translate("DownloadDialog", "Download and Decrypt Files"))
        self.downloadLinkLabel.setText(_translate("DownloadDialog", "Paste Your Download Link Here:"))
        self.downloadButton.setText(_translate("DownloadDialog", "Download + Decrypt"))

