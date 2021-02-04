#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
############################################
#from read_db import read_from_db
from line_gui import Ui_line_ui
from del_line_gui import Ui_del_ui
from table_gui import Ui_table_ui
#############################################

class Ui_db_ui(object):
    ############################################
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        #self.window.__init__(self.window,None, QtCore.Qt.WindowStaysOnTopHint)# code to keep the main window on top
        #self.window.super().__init__(self.window,None, QtCore.Qt.WindowStaysOnTopHint)
        self.ui=Ui_line_ui()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openWindow_2(self):
        self.window2=QtWidgets.QMainWindow()
        self.ui=Ui_del_ui()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def openWindow_3(self):
        self.window3=QtWidgets.QMainWindow()
        self.ui=Ui_table_ui()
        self.ui.setupUi(self.window3)
        self.window3.show()
    #############################################
    def setupUi(self, db_ui):
        db_ui.setObjectName("db_ui")
        db_ui.resize(420, 420)
        self.label = QtWidgets.QLabel(db_ui)
        self.label.setGeometry(QtCore.QRect(150, 30, 131, 21))
        self.label.setObjectName("label")
        self.add_object_btn = QtWidgets.QPushButton(db_ui)
        self.add_object_btn.setGeometry(QtCore.QRect(120, 137, 171, 31))
        self.add_object_btn.setObjectName("add_object_btn")
        #######################################################
        self.add_object_btn.clicked.connect(self.openWindow)
        #######################################################
        self.read_db_btn = QtWidgets.QPushButton(db_ui)
        self.read_db_btn.setGeometry(QtCore.QRect(100, 80, 211, 31))
        self.read_db_btn.setObjectName("read_db_btn")
        #######################################################
        #self.read_db_btn.clicked.connect(lambda: read_from_db())
        self.read_db_btn.clicked.connect(self.openWindow_3)
        #######################################################
        self.del_object_btn = QtWidgets.QPushButton(db_ui)
        self.del_object_btn.setGeometry(QtCore.QRect(120, 197, 171, 31))
        self.del_object_btn.setObjectName("del_object_btn")
        #######################################################
        self.del_object_btn.clicked.connect(self.openWindow_2)
        #######################################################
        self.print_object_btn = QtWidgets.QPushButton(db_ui)
        self.print_object_btn.setGeometry(QtCore.QRect(120, 250, 171, 31))
        self.print_object_btn.setObjectName("print_object_btn")
        #######################################################
        self.quit_btn = QtWidgets.QPushButton(db_ui)
        self.quit_btn.setGeometry(QtCore.QRect(120, 300, 171, 31))
        self.quit_btn.setObjectName("quit_btn")
        ########################################################
        self.quit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.retranslateUi(db_ui)
        QtCore.QMetaObject.connectSlotsByName(db_ui)

    def retranslateUi(self, db_ui):
        _translate = QtCore.QCoreApplication.translate
        db_ui.setWindowTitle(_translate("db_ui", "Dialog"))
        self.label.setText(_translate("db_ui", "Choose an action"))
        self.add_object_btn.setText(_translate("db_ui", "Add an object"))
        self.read_db_btn.setText(_translate("db_ui", "Read the object database"))
        self.del_object_btn.setText(_translate("db_ui", "Delete an object"))
        #########################################################
        self.print_object_btn.setText(_translate("db_ui", "Print"))
        #########################################################
        self.quit_btn.setText(_translate("db_ui", "Quit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db_ui = QtWidgets.QDialog()
    ui = Ui_db_ui()
    ui.setupUi(db_ui)
    db_ui.show()
    sys.exit(app.exec_())

