# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_addIndicator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_AddIndicator(object):
    def setupUi(self, Dialog_AddIndicator):
        Dialog_AddIndicator.setObjectName("Dialog_AddIndicator")
        Dialog_AddIndicator.resize(653, 267)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_AddIndicator)
        self.buttonBox.setGeometry(QtCore.QRect(450, 220, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_AddIndicator)
        self.label.setGeometry(QtCore.QRect(20, 60, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_AddIndicator)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_AddIndicator)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_mainGroup = QtWidgets.QComboBox(Dialog_AddIndicator)
        self.comboBox_mainGroup.setGeometry(QtCore.QRect(130, 60, 111, 22))
        self.comboBox_mainGroup.setObjectName("comboBox_mainGroup")
        self.comboBox_mainGroup.addItem("")
        self.comboBox_mainGroup.addItem("")
        self.comboBox_subGroup = QtWidgets.QComboBox(Dialog_AddIndicator)
        self.comboBox_subGroup.setGeometry(QtCore.QRect(130, 100, 111, 22))
        self.comboBox_subGroup.setObjectName("comboBox_subGroup")
        self.comboBox_indicatorName = QtWidgets.QComboBox(Dialog_AddIndicator)
        self.comboBox_indicatorName.setGeometry(QtCore.QRect(130, 140, 111, 22))
        self.comboBox_indicatorName.setObjectName("comboBox_indicatorName")
        self.textBrowser_indicatorDescription = QtWidgets.QTextBrowser(Dialog_AddIndicator)
        self.textBrowser_indicatorDescription.setGeometry(QtCore.QRect(260, 60, 371, 101))
        self.textBrowser_indicatorDescription.setObjectName("textBrowser_indicatorDescription")
        self.label_4 = QtWidgets.QLabel(Dialog_AddIndicator)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 191, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit_inpuNameIndicator = QtWidgets.QTextEdit(Dialog_AddIndicator)
        self.textEdit_inpuNameIndicator.setGeometry(QtCore.QRect(260, 20, 371, 20))
        self.textEdit_inpuNameIndicator.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_inpuNameIndicator.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_inpuNameIndicator.setObjectName("textEdit_inpuNameIndicator")
        self.pushButton_editParamsInputs = QtWidgets.QPushButton(Dialog_AddIndicator)
        self.pushButton_editParamsInputs.setGeometry(QtCore.QRect(70, 190, 131, 23))
        self.pushButton_editParamsInputs.setObjectName("pushButton_editParamsInputs")

        self.retranslateUi(Dialog_AddIndicator)
        self.buttonBox.accepted.connect(Dialog_AddIndicator.accept)
        self.buttonBox.rejected.connect(Dialog_AddIndicator.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AddIndicator)

    def retranslateUi(self, Dialog_AddIndicator):
        _translate = QtCore.QCoreApplication.translate
        Dialog_AddIndicator.setWindowTitle(_translate("Dialog_AddIndicator", "Dialog"))
        self.label.setText(_translate("Dialog_AddIndicator", "Choose main group:"))
        self.label_2.setText(_translate("Dialog_AddIndicator", "Choose sub group:"))
        self.label_3.setText(_translate("Dialog_AddIndicator", "Choose Indicator:"))
        self.comboBox_mainGroup.setItemText(0, _translate("Dialog_AddIndicator", "indicator"))
        self.comboBox_mainGroup.setItemText(1, _translate("Dialog_AddIndicator", "transformation"))
        self.label_4.setText(_translate("Dialog_AddIndicator", "Choose a Name for the new indicator:"))
        self.pushButton_editParamsInputs.setText(_translate("Dialog_AddIndicator", "Edit params and inputs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_AddIndicator = QtWidgets.QDialog()
    ui = Ui_Dialog_AddIndicator()
    ui.setupUi(Dialog_AddIndicator)
    Dialog_AddIndicator.show()
    sys.exit(app.exec_())
