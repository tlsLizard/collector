# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'line_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#####################################################
from line import count_items, create_line,get_max_id
####################################################

###############################
class Ui_line_ui(object): ##changement de nom
################################
    def setupUi(self, db_ui):
        db_ui.setObjectName("db_ui")
        db_ui.resize(400, 300)
        self.label = QtWidgets.QLabel(db_ui)
        self.label.setGeometry(QtCore.QRect(100, 30, 201, 21))
        self.label.setObjectName("label")
        self.add_line = QtWidgets.QPushButton(db_ui)
        self.add_line.setGeometry(QtCore.QRect(160, 130, 90, 28))
        self.add_line.setObjectName("add_line")
        self.object_name = QtWidgets.QLineEdit(db_ui)
        self.object_name.setGeometry(QtCore.QRect(90, 80, 211, 28))
        self.object_name.setObjectName("object_name")
        ###########################################################
        self.add_line.clicked.connect(lambda: create_line(get_max_id()+1,self.object_name.text()))
        ###########################################################


        self.retranslateUi(db_ui)
        QtCore.QMetaObject.connectSlotsByName(db_ui)

    def retranslateUi(self, db_ui):
        _translate = QtCore.QCoreApplication.translate
        db_ui.setWindowTitle(_translate("db_ui", "Dialog"))
        self.label.setText(_translate("db_ui", "Add a ligne to the object table"))
        self.add_line.setText(_translate("db_ui", "Create"))
        self.object_name.setText(_translate("db_ui", "object name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db_ui = QtWidgets.QDialog()
    ui = Ui_db_ui()
    ui.setupUi(db_ui)
    db_ui.show()
    sys.exit(app.exec_())

