# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ashwin\PycharmProjects\DASec\src\DropboxClient\EmailDownloadLink.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EmailDownloadLink(object):
    def setupUi(self, EmailDownloadLink):
        EmailDownloadLink.setObjectName("EmailDownloadLink")
        EmailDownloadLink.resize(632, 75)
        self.shareLinkLabel = QtWidgets.QLabel(EmailDownloadLink)
        self.shareLinkLabel.setGeometry(QtCore.QRect(20, 20, 80, 25))
        self.shareLinkLabel.setObjectName("shareLinkLabel")

        self.retranslateUi(EmailDownloadLink)
        QtCore.QMetaObject.connectSlotsByName(EmailDownloadLink)

    def retranslateUi(self, EmailDownloadLink):
        _translate = QtCore.QCoreApplication.translate
        EmailDownloadLink.setWindowTitle(_translate("EmailDownloadLink", "Email Share URL"))
        self.shareLinkLabel.setText(_translate("EmailDownloadLink", "Share URL :"))

