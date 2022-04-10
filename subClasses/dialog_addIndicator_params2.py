# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_addIndicator_params.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_AddIndicator_Parameters(object):
    def setupUi(self, Dialog_AddIndicator_Parameters):
        Dialog_AddIndicator_Parameters.setObjectName("Dialog_AddIndicator_Parameters")
        Dialog_AddIndicator_Parameters.resize(230, 200)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_AddIndicator_Parameters)
        self.buttonBox.setGeometry(QtCore.QRect(35, 160, 160, 30))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox_inputs = QtWidgets.QGroupBox(Dialog_AddIndicator_Parameters)
        self.groupBox_inputs.setGeometry(QtCore.QRect(20, 10, 190, 50))
        self.groupBox_inputs.setObjectName("groupBox_inputs")
        self.label_inpu1 = QtWidgets.QLabel(self.groupBox_inputs)
        self.label_inpu1.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_inpu1.setObjectName("label_inpu1")
        self.comboBox_input1 = QtWidgets.QComboBox(self.groupBox_inputs)
        self.comboBox_input1.setGeometry(QtCore.QRect(100, 17, 71, 22))
        self.comboBox_input1.setObjectName("comboBox_input1")
        self.groupBox_parameters = QtWidgets.QGroupBox(Dialog_AddIndicator_Parameters)
        self.groupBox_parameters.setGeometry(QtCore.QRect(20, 70, 190, 80))
        self.groupBox_parameters.setObjectName("groupBox_parameters")
        self.label_2 = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label_3.setObjectName("label_3")
        self.spinBox_param1 = QtWidgets.QSpinBox(self.groupBox_parameters)
        self.spinBox_param1.setGeometry(QtCore.QRect(100, 17, 71, 22))
        self.spinBox_param1.setObjectName("spinBox_param1")
        self.spinBox_param2 = QtWidgets.QSpinBox(self.groupBox_parameters)
        self.spinBox_param2.setGeometry(QtCore.QRect(100, 47, 71, 22))
        self.spinBox_param2.setObjectName("spinBox_param2")

        self.retranslateUi(Dialog_AddIndicator_Parameters)
        self.buttonBox.accepted.connect(Dialog_AddIndicator_Parameters.accept)
        self.buttonBox.rejected.connect(Dialog_AddIndicator_Parameters.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AddIndicator_Parameters)

    def retranslateUi(self, Dialog_AddIndicator_Parameters):
        _translate = QtCore.QCoreApplication.translate
        Dialog_AddIndicator_Parameters.setWindowTitle(_translate("Dialog_AddIndicator_Parameters", "Dialog"))
        self.groupBox_inputs.setTitle(_translate("Dialog_AddIndicator_Parameters", "Inputs"))
        self.label_inpu1.setText(_translate("Dialog_AddIndicator_Parameters", "Input 1:"))
        self.groupBox_parameters.setTitle(_translate("Dialog_AddIndicator_Parameters", "Parameters"))
        self.label_2.setText(_translate("Dialog_AddIndicator_Parameters", "Param 1:"))
        self.label_3.setText(_translate("Dialog_AddIndicator_Parameters", "Param 2:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_AddIndicator_Parameters = QtWidgets.QDialog()
    ui = Ui_Dialog_AddIndicator_Parameters()
    ui.setupUi(Dialog_AddIndicator_Parameters)
    Dialog_AddIndicator_Parameters.show()
    sys.exit(app.exec_())
