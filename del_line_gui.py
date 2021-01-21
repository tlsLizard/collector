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
        self.label.setGeometry(QtCore.QRect(100, 30, 201, 21))
        self.label.setObjectName("label")
        self.delete_line = QtWidgets.QPushButton(db_ui)
        self.delete_line.setGeometry(QtCore.QRect(190, 110, 90, 28))
        self.delete_line.setObjectName("delete_line")
        self.object_id = QtWidgets.QLineEdit(db_ui)
        self.object_id.setGeometry(QtCore.QRect(90, 80, 61, 28))
        self.object_id.setObjectName("object_id")
        #########################################################
        self.quit_btn = QtWidgets.QPushButton(del_line_ui)
        self.quit_btn.setGeometry(QtCore.QRect(90, 130, 90, 28))
        self.quit_btn.setObjectName("quit_btn")
        self.quit_btn.clicked.connect(db_ui.close)
        ###########################################################
        self.quit_btn.clicked.connect(lambda: delete_line(int(self.object_id.text())))
        ##renvoyer un message d'erreur si l'id n'a pas d'entree dans la table
        ###########################################################
        self.msg_box = QtWidgets.QLabel(db_ui)
        self.msg_box.setGeometry(QtCore.QRect(90, 120, 58, 16))
        self.msg_box.setText("coucou")
        self.msg_box.setObjectName("msg_box")

        self.retranslateUi(db_ui)
        QtCore.QMetaObject.connectSlotsByName(db_ui)

    def retranslateUi(self, db_ui):
        _translate = QtCore.QCoreApplication.translate
        db_ui.setWindowTitle(_translate("db_ui", "Dialog"))
        self.label.setText(_translate("db_ui", "Delete a line from the object table"))
        self.delete_line.setText(_translate("db_ui", "Delete"))
        self.object_id.setText(_translate("db_ui", "object_id"))
        self.quit_btn.setText(_translate("db_ui", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db_ui = QtWidgets.QDialog()
    ui = Ui_db_ui()
    ui.setupUi(db_ui)
    db_ui.show()
    sys.exit(app.exec_())

