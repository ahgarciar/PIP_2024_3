# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p2_ejemplo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_sumar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sumar.setGeometry(QtCore.QRect(160, 180, 191, 61))
        self.btn_sumar.setObjectName("btn_sumar")
        self.txt_num1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_num1.setGeometry(QtCore.QRect(160, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txt_num1.setFont(font)
        self.txt_num1.setText("")
        self.txt_num1.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_num1.setObjectName("txt_num1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(87, 20, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 71, 31))
        self.label_2.setObjectName("label_2")
        self.txt_num2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_num2.setGeometry(QtCore.QRect(160, 60, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txt_num2.setFont(font)
        self.txt_num2.setText("")
        self.txt_num2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_num2.setObjectName("txt_num2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 71, 31))
        self.label_3.setObjectName("label_3")

        ##########################################################################
        ###AGREGADO MANUALMENTE
        self.txt_num3 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_num3.setGeometry(QtCore.QRect(160, 110, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txt_num3.setFont(font)
        self.txt_num3.setText("")
        self.txt_num3.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_num3.setObjectName("txt_num3")
        ##########################################################################

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_sumar.setText(_translate("MainWindow", "SUMA"))
        self.label.setText(_translate("MainWindow", "Número 1:"))
        self.label_2.setText(_translate("MainWindow", "Número 2:"))
        self.label_3.setText(_translate("MainWindow", "Número 3:"))
