# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'line_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
####################################################
from PyQt5.QtCore import QCoreApplication
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
        self.label.setGeometry(QtCore.QRect(100, 30, 231, 21))
        self.label.setObjectName("label")
        self.add_line = QtWidgets.QPushButton(db_ui)
        self.add_line.setGeometry(QtCore.QRect(210, 190, 90, 28))
        self.add_line.setObjectName("add_line")
        self.object_name = QtWidgets.QLineEdit(db_ui)
        self.object_name.setGeometry(QtCore.QRect(90, 80, 211, 28))
        self.object_name.setObjectName("object_name")
        ###########################################################
        self.object_name.setFrame(True)
        self.object_name.setReadOnly(False)
        ###########################################################
        self.add_line.clicked.connect(lambda: create_line(get_max_id()+1,self.object_name.text()))
        ###########################################################
        self.add_image_btn = QtWidgets.QPushButton(db_ui)
        self.add_image_btn.setGeometry(QtCore.QRect(90, 130, 121, 25))
        self.add_image_btn.setAutoFillBackground(False)
        self.add_image_btn.setObjectName("add_image_btn")
        self.quit_btn = QtWidgets.QPushButton(db_ui)
        self.quit_btn.setGeometry(QtCore.QRect(90, 190, 90, 28))
        self.quit_btn.setObjectName("quit_btn")
        self.quit_btn.clicked.connect(db_ui.close)
        ############################################################
        self.add_image_btn.setObjectName("add_image")

        self.retranslateUi(db_ui)
        QtCore.QMetaObject.connectSlotsByName(db_ui)

    def retranslateUi(self, db_ui):
        _translate = QtCore.QCoreApplication.translate
        db_ui.setWindowTitle(_translate("db_ui", "Dialog"))
        self.label.setText(_translate("db_ui", "Add a ligne to the object table"))
        self.add_line.setText(_translate("db_ui", "Create"))
        self.object_name.setText(_translate("db_ui", "object name"))
        ##############################################################
        self.add_image_btn.setText(_translate("db_ui", "Add a picture"))
        self.quit_btn.setText(_translate("db_ui", "Quit"))

    ######################################################
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "Open a photo", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db_ui = QtWidgets.QDialog()
    ui = Ui_db_ui()
    ui.setupUi(db_ui)
    db_ui.show()
    sys.exit(app.exec_())

