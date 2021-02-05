# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'del_line_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#####################################################
from line import delete_line
####################################################

############################
class Ui_del_ui(object):#changement de nom
############################
    def setupUi(self, db_ui):
        db_ui.setObjectName("db_ui")
        db_ui.resize(388, 187)
        self.label = QtWidgets.QLabel(db_ui)
        self.label.setGeometry(QtCore.QRect(70, 30, 261, 21))
        self.label.setObjectName("label")
        self.delete_line = QtWidgets.QPushButton(db_ui)
        self.delete_line.setGeometry(QtCore.QRect(200, 130, 90, 28))
        self.delete_line.setObjectName("delete_line")
        self.object_id = QtWidgets.QLineEdit(db_ui)
        self.object_id.setGeometry(QtCore.QRect(140, 70, 101, 28))
        self.object_id.setObjectName("object_id")
        ###########################################################
        self.delete_line.clicked.connect(lambda: delete_line(int(self.object_id.text())))
        ##renvoyer un message d'erreur si l'id n'a pas d'entree dans la table
        ###########################################################
        self.quit_btn = QtWidgets.QPushButton(db_ui)
        self.quit_btn.setGeometry(QtCore.QRect(80, 130, 90, 28))
        self.quit_btn.setObjectName("quit_btn")
        self.quit_btn.clicked.connect(db_ui.close)

        self.retranslateUi(db_ui)
        QtCore.QMetaObject.connectSlotsByName(db_ui)

    def retranslateUi(self, db_ui):
        _translate = QtCore.QCoreApplication.translate
        db_ui.setWindowTitle(_translate("db_ui", "Delete an object"))
        self.label.setText(_translate("db_ui", "Delete a line from the object table"))
        self.delete_line.setText(_translate("db_ui", "Delete"))
        self.object_id.setPlaceholderText(_translate("db_ui", "object_id"))
        self.quit_btn.setText(_translate("db_ui", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db_ui = QtWidgets.QDialog()
    ui = Ui_del_ui()
    ui.setupUi(db_ui)
    db_ui.show()
    sys.exit(app.exec_())
