# Author : Ashwin Joshi
# CS 6348 Project
# User Authentication with HMAC
#
#
import socket
import sys
from PyQt5 import QtGui,QtCore,uic
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit,)
from PyQt5.QtGui import QIcon

class AuthenticationClient(QtGui.QDialog):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        uic.loadUi('MainWindow.ui',self)

        self.setGeometry(500,500,500,300)
        self.setWindowTitle('Enc.DropBox-Extension')
        self.setWindowIcon(QIcon('dropbox.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = AuthenticationClient()
    sys.exit(app.exec_())

""" client_socket = socket.socket()
client_host = socket.gethostname()
client_port = 8899

try:
    client_socket.connect((client_host, client_port))
    print(client_socket.recv(1024))

finally:
    client_socket.close() """