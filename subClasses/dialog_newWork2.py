# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_newWork.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewWork(object):
    def setupUi(self, NewWork):
        NewWork.setObjectName("NewWork")
        NewWork.resize(533, 345)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewWork)
        self.buttonBox.setGeometry(QtCore.QRect(110, 305, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(NewWork)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setObjectName("label")
        self.textEdit_InputNewWorkName = QtWidgets.QTextEdit(NewWork)
        self.textEdit_InputNewWorkName.setGeometry(QtCore.QRect(130, 5, 251, 23))
        self.textEdit_InputNewWorkName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_InputNewWorkName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_InputNewWorkName.setObjectName("textEdit_InputNewWorkName")
        self.label_3 = QtWidgets.QLabel(NewWork)
        self.label_3.setGeometry(QtCore.QRect(10, 245, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(NewWork)
        self.label_4.setGeometry(QtCore.QRect(10, 275, 81, 16))
        self.label_4.setObjectName("label_4")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(NewWork)
        self.dateTimeEdit.setGeometry(QtCore.QRect(130, 240, 111, 23))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(NewWork)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(130, 270, 111, 23))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.tableWidget_rowPreview = QtWidgets.QTableWidget(NewWork)
        self.tableWidget_rowPreview.setGeometry(QtCore.QRect(130, 190, 391, 41))
        self.tableWidget_rowPreview.setObjectName("tableWidget_rowPreview")
        self.tableWidget_rowPreview.setColumnCount(0)
        self.tableWidget_rowPreview.setRowCount(0)
        self.comboBox_assetType = QtWidgets.QComboBox(NewWork)
        self.comboBox_assetType.setGeometry(QtCore.QRect(130, 40, 161, 22))
        self.comboBox_assetType.setObjectName("comboBox_assetType")
        self.comboBox_Broker = QtWidgets.QComboBox(NewWork)
        self.comboBox_Broker.setGeometry(QtCore.QRect(130, 70, 161, 22))
        self.comboBox_Broker.setObjectName("comboBox_Broker")
        self.comboBox_File = QtWidgets.QComboBox(NewWork)
        self.comboBox_File.setGeometry(QtCore.QRect(130, 100, 161, 22))
        self.comboBox_File.setObjectName("comboBox_File")
        self.label_2 = QtWidgets.QLabel(NewWork)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(NewWork)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(NewWork)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 121, 16))
        self.label_6.setObjectName("label_6")
        self.textBrowser_description = QtWidgets.QTextBrowser(NewWork)
        self.textBrowser_description.setGeometry(QtCore.QRect(130, 130, 391, 51))
        self.textBrowser_description.setObjectName("textBrowser_description")
        self.label_7 = QtWidgets.QLabel(NewWork)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(NewWork)
        self.label_8.setGeometry(QtCore.QRect(10, 190, 121, 16))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(NewWork)
        self.buttonBox.accepted.connect(NewWork.accept)
        self.buttonBox.rejected.connect(NewWork.reject)
        QtCore.QMetaObject.connectSlotsByName(NewWork)

    def retranslateUi(self, NewWork):
        _translate = QtCore.QCoreApplication.translate
        NewWork.setWindowTitle(_translate("NewWork", "Dialog"))
        self.label.setText(_translate("NewWork", "Enter New Work Name:"))
        self.label_3.setText(_translate("NewWork", "Select Init Date:"))
        self.label_4.setText(_translate("NewWork", "Select End Date:"))
        self.label_2.setText(_translate("NewWork", "Select Asset Type:"))
        self.label_5.setText(_translate("NewWork", "Select Broker:"))
        self.label_6.setText(_translate("NewWork", "Select File:"))
        self.label_7.setText(_translate("NewWork", "Data Description:"))
        self.label_8.setText(_translate("NewWork", "Data 1st row preview:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewWork = QtWidgets.QDialog()
    ui = Ui_NewWork()
    ui.setupUi(NewWork)
    NewWork.show()
    sys.exit(app.exec_())
