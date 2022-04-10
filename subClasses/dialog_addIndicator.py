# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_addIndicator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from subClasses.dialog_addIndicator_params import Ui_Dialog_AddIndicator_Parameters
import json


class Ui_Dialog_AddIndicator(object):
    def setupUi(self, Dialog_AddIndicator, dic_current_work):
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

        self.dic_current_work = dic_current_work

        self.retranslateUi(Dialog_AddIndicator)
        self.buttonBox.accepted.connect(Dialog_AddIndicator.accept)
        self.buttonBox.accepted.connect(self.submit)
        self.buttonBox.rejected.connect(Dialog_AddIndicator.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AddIndicator)


        with open('indicator/indicator.json', 'r') as f:
            self.dic_indicator_sumup = json.load(f)
            f.close()
        self.dic_mainGroup_to_subGroup = {}
        self.dic_subGroup_to_indicator = {}
        for indicator in self.dic_indicator_sumup.keys():
            mainG = self.dic_indicator_sumup[indicator]['main group']
            subG = self.dic_indicator_sumup[indicator]['sub group']
            # adding to main to sub dic
            if mainG in self.dic_mainGroup_to_subGroup.keys():
                if subG not in self.dic_mainGroup_to_subGroup[mainG]:
                    self.dic_mainGroup_to_subGroup[mainG].append(subG)        
            else:
                self.dic_mainGroup_to_subGroup[mainG] = [subG]
            # adding to sub to indicator dic
            if subG in self.dic_subGroup_to_indicator.keys():
                if indicator not in self.dic_subGroup_to_indicator[subG]:
                     self.dic_subGroup_to_indicator[subG].append(indicator)        
            else:
                self.dic_subGroup_to_indicator[subG] = [indicator]

        print('----debug\ndic main group: {}\ndic sub group: {}\nList values main group: {}'.format(self.dic_mainGroup_to_subGroup, 
            self.dic_subGroup_to_indicator, [key for key in self.dic_mainGroup_to_subGroup.keys()]))

        self.selected_indicator = ''

        self.initialise_comboBox_mainGroup()

        self.comboBox_mainGroup.currentTextChanged.connect(self.initialise_comboBox_subGroup)
        self.comboBox_subGroup.currentTextChanged.connect(self.initialise_comboBox_IndicatorName)

        self.pushButton_editParamsInputs.clicked.connect(self.indicatorName_is_selected)
        

    def retranslateUi(self, Dialog_AddIndicator):
        self._translate = QtCore.QCoreApplication.translate
        Dialog_AddIndicator.setWindowTitle(self._translate("Dialog_AddIndicator", "Dialog"))
        self.label.setText(self._translate("Dialog_AddIndicator", "Choose main group:"))
        self.label_2.setText(self._translate("Dialog_AddIndicator", "Choose sub group:"))
        self.label_3.setText(self._translate("Dialog_AddIndicator", "Choose Indicator:"))
        self.comboBox_mainGroup.setItemText(0, self._translate("Dialog_AddIndicator", "indicator"))
        self.comboBox_mainGroup.setItemText(1, self._translate("Dialog_AddIndicator", "transformation"))
        self.label_4.setText(self._translate("Dialog_AddIndicator", "Choose a Name for the new indicator:"))
        self.pushButton_editParamsInputs.setText(self._translate("Dialog_AddIndicator", "Edit params and inputs"))

    def submit(self):
        pass

    def initialise_comboBox_mainGroup(self):
        self.comboBox_mainGroup.clear()
        list_values = [key for key in self.dic_mainGroup_to_subGroup.keys()]
        for i in range(len(list_values)):
            value = list_values[i]
            self.comboBox_mainGroup.addItem("")
            self.comboBox_mainGroup.setItemText(i, self._translate("Dialog_AddIndicator", value))

    def initialise_comboBox_subGroup(self):
        self.comboBox_subGroup.clear()
        current_mainGroup = self.comboBox_mainGroup.currentText()
        list_values = self.dic_mainGroup_to_subGroup[current_mainGroup]
        for i in range(len(list_values)):
            value = list_values[i]
            self.comboBox_subGroup.addItem("")
            self.comboBox_subGroup.setItemText(i, self._translate("Dialog_AddIndicator", value))

    def initialise_comboBox_IndicatorName(self):
        self.comboBox_indicatorName.clear()
        current_subGroup = self.comboBox_subGroup.currentText()
        if current_subGroup != '':
            list_values = self.dic_subGroup_to_indicator[current_subGroup]
            for i in range(len(list_values)):
                value = list_values[i]
                self.comboBox_indicatorName.addItem("")
                self.comboBox_indicatorName.setItemText(i, self._translate("Dialog_AddIndicator", value))

    def indicatorName_is_selected(self):
        '''triggered when indicator name is selected in the combo box
        make things appears in the text browser
        instanciaze a dic (found in indicator_sumup) that will be the argument of an adaptative dialog
        that will be opened via a push button and used to set the parameters for the indicator'''
        self.selected_indicator = self.comboBox_indicatorName.currentText()
        self.indicator_name_var = self.textEdit_inpuNameIndicator.toPlainText()
        dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_AddIndicator_Parameters()
        ui.setupUi(dialog, self.selected_indicator, self.dic_current_work)
        dialog.show()
        rsp = dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            self.params = ui.params
            self.inputs_name = ui.inputs_name



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_AddIndicator = QtWidgets.QDialog()
    ui = Ui_Dialog_AddIndicator()
    ui.setupUi(Dialog_AddIndicator)
    Dialog_AddIndicator.show()
    sys.exit(app.exec_())
