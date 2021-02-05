#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
############################################
import sqlite3
from edit_line_gui import Ui_edit_ui
############################################

class Ui_table_ui(object):
    ############################################
    def openWindow_4(self):
        self.window4=QtWidgets.QMainWindow()
        self.ui=Ui_edit_ui()
        self.ui.setupUi(self.window4,self.line_to_edit.text())
        self.window4.show()
    #############################################
    def setupUi(self, table_ui):
        table_ui.setObjectName("table_ui")
        table_ui.resize(1303, 672)
        self.label = QtWidgets.QLabel(table_ui)
        self.label.setGeometry(QtCore.QRect(0, 30, 1301, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.edit_line = QtWidgets.QPushButton(table_ui)
        self.edit_line.setGeometry(QtCore.QRect(1160, 80, 90, 28))
        self.edit_line.setObjectName("edit_line")
        #############################################################
        self.edit_line.clicked.connect(self.openWindow_4)
        #############################################################
        self.line_to_edit = QtWidgets.QLineEdit(table_ui)
        self.line_to_edit.setGeometry(QtCore.QRect(1080, 80, 71, 28))
        self.line_to_edit.setObjectName("line_to_edit")
        self.tableView = QtWidgets.QTableView(table_ui)
        self.tableView.setGeometry(QtCore.QRect(30, 80, 1021, 561))
        self.tableView.setObjectName("tableView")
        #########################################################
        self.model = QtGui.QStandardItemModel(self.tableView)
        self.tableView.setModel(self.model)
        self.load_db()
        self.tableView.resizeColumnsToContents()
        #########################################################
        self.retranslateUi(table_ui)
        QtCore.QMetaObject.connectSlotsByName(table_ui)

    def retranslateUi(self, table_ui):
        _translate = QtCore.QCoreApplication.translate
        table_ui.setWindowTitle(_translate("table_ui", "Show your collections"))
        self.label.setText(_translate("table_ui", "Your collections"))
        self.edit_line.setText(_translate("table_ui", "Edit a line"))
        self.line_to_edit.setPlaceholderText(_translate("table_ui", "line"))
    ############################################################ 
    def load_db(self):
        try:
            conn=sqlite3.connect('objects.db')
            c=conn.cursor()
            c.execute("SELECT * FROM objects")
            data = c.fetchall()
            for row in data:
                items = [
                    QtGui.QStandardItem(str(field))##
                    for field in row
                ]
                self.model.appendRow(items)
        except sqlite3.Error as error:
            print("Failed to populate the table", error)
        finally:
            if (conn):
                conn.close()
                print("the sqlite connection is closed")
    ############################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    table_ui = QtWidgets.QDialog()
    ui = Ui_table_ui()
    ui.setupUi(table_ui)
    table_ui.show()
    sys.exit(app.exec_())

