# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_addIndicator_params.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_Dialog_AddIndicator_Parameters(object):
    def setupUi(self, Dialog_AddIndicator_Parameters, name_indicator, dic_current_work):

        with open('indicator/indicator.json') as f:
            self.dic_indicator_sumup = json.load(f)
            f.close()
        self.indicator_template_inputs = self.dic_indicator_sumup[name_indicator]['inputs'] # return something like {'x':any type}
        self.indicator_template_params = self.dic_indicator_sumup[name_indicator]['params'] # return something like {'p':'period'}
        self.indicator_default_params = self.dic_indicator_sumup[name_indicator]['default_params'] # return something like {'p':21}
        self.list_current_variables = [key for key in dic_current_work['variables'].keys()]

        # import data
        nbs_input = len(self.indicator_template_inputs)
        nbs_param = len(self.indicator_template_params)
        # geometry calculus
        self.h_one_param_on_main_window = 30
        h_mainwindow = 110 + nbs_input*self.h_one_param_on_main_window + nbs_param*self.h_one_param_on_main_window
        w_mainwindow = 230
        h_groupbox_inputs = 20 + nbs_input*self.h_one_param_on_main_window
        w_groupbox_inputs = 190
        y_groupbox_inputs = 10
        x_groupbox_inputs = w_mainwindow/2 - w_groupbox_inputs/2
        h_groupbox_parameters = 20 + nbs_param*self.h_one_param_on_main_window
        w_groupbox_parameters = 190
        y_groupbox_parameters = 40 + nbs_input*self.h_one_param_on_main_window
        x_groupbox_parameters = w_mainwindow/2 - w_groupbox_parameters/2
        h_buttonbox = 30
        w_buttonbox = 160
        y_buttonbox = 70 + nbs_input*self.h_one_param_on_main_window + nbs_param*self.h_one_param_on_main_window
        x_buttonbox = w_mainwindow/2 - w_buttonbox/2


        # setting permanent objects
        Dialog_AddIndicator_Parameters.setObjectName("Dialog_AddIndicator_Parameters")
        Dialog_AddIndicator_Parameters.resize(w_mainwindow, h_mainwindow)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_AddIndicator_Parameters)
        self.buttonBox.setGeometry(QtCore.QRect(x_buttonbox, y_buttonbox, w_buttonbox, h_buttonbox))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox_inputs = QtWidgets.QGroupBox(Dialog_AddIndicator_Parameters)
        self.groupBox_inputs.setGeometry(QtCore.QRect(x_groupbox_inputs, y_groupbox_inputs, w_groupbox_inputs, h_groupbox_inputs))
        self.groupBox_parameters = QtWidgets.QGroupBox(Dialog_AddIndicator_Parameters)
        self.groupBox_parameters.setGeometry(QtCore.QRect(x_groupbox_parameters, y_groupbox_parameters, w_groupbox_parameters, h_groupbox_parameters))
        self.groupBox_parameters.setObjectName("groupBox_parameters")
        self.groupBox_inputs.setObjectName("groupBox_inputs")

        self.retranslateUi(Dialog_AddIndicator_Parameters)
        self.buttonBox.accepted.connect(Dialog_AddIndicator_Parameters.accept)
        self.buttonBox.accepted.connect(self.submit)
        self.buttonBox.rejected.connect(Dialog_AddIndicator_Parameters.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AddIndicator_Parameters)

        # Add widgets to inputs group box
        self.dic_label_input = {}
        self.dic_comboBox_input = {}
        i = 0
        for key in self.indicator_template_inputs.keys():
            h_label, w_label, x_label, y_label = 16, 71, 20, 20+i*self.h_one_param_on_main_window
            name_input = self.indicator_template_inputs[key]
            #label
            self.dic_label_input[key] = QtWidgets.QLabel(self.groupBox_inputs)
            self.dic_label_input[key].setGeometry(QtCore.QRect(x_label, y_label, w_label, h_label))
            self.dic_label_input[key].setObjectName("label_input_"+name_input)
            self.dic_label_input[key].setText(self._translate("Dialog_AddIndicator_Parameters", name_input+':'))

            h_combobox, w_combobox, x_combobox, y_combobox = 22, 71, 100, 17+i*self.h_one_param_on_main_window
            #combo box
            self.dic_comboBox_input[key] = QtWidgets.QComboBox(self.groupBox_inputs)
            self.dic_comboBox_input[key].setGeometry(QtCore.QRect(x_combobox, y_combobox, w_combobox, h_combobox))
            self.dic_comboBox_input[key].setObjectName("comboBox_input_"+name_input)
            for k in range(len(self.list_current_variables)):
                var = self.list_current_variables[k]
                self.dic_comboBox_input[key].addItem("")
                self.dic_comboBox_input[key].setItemText(k, self._translate("Dialog_AddIndicator", var))
            i += 1

        # Add widgets to params group box
        self.dic_label_parameter = {}
        self.dic_spinBox_parameter = {}
        i = 0
        for key in self.indicator_template_params.keys():
            h_label, w_label, x_label, y_label = 16, 71, 20, 20+i*self.h_one_param_on_main_window
            name_parameter = self.indicator_template_params[key]
            #label
            self.dic_label_parameter[key] = QtWidgets.QLabel(self.groupBox_parameters)
            self.dic_label_parameter[key].setGeometry(QtCore.QRect(x_label, y_label, w_label, h_label))
            self.dic_label_parameter[key].setObjectName("label_param"+name_parameter)
            self.dic_label_parameter[key].setText(self._translate("Dialog_AddIndicator_Parameters", name_parameter+':'))

            h_spinBox, w_spinBox, x_spinBox, y_spinBox = 22, 71, 100, 17+i*self.h_one_param_on_main_window
            #combo box
            self.dic_spinBox_parameter[key] = QtWidgets.QSpinBox(self.groupBox_parameters)
            self.dic_spinBox_parameter[key].setGeometry(QtCore.QRect(x_spinBox, y_spinBox, w_spinBox, h_spinBox))
            self.dic_spinBox_parameter[key].setObjectName("spinbox_pram_"+name_parameter)
            self.dic_spinBox_parameter[key].setValue(self.indicator_default_params[key])
            # compteur
            i+=1

        

    def retranslateUi(self, Dialog_AddIndicator_Parameters):
        self._translate = QtCore.QCoreApplication.translate
        Dialog_AddIndicator_Parameters.setWindowTitle(self._translate("Dialog_AddIndicator_Parameters", "Dialog"))
        self.groupBox_inputs.setTitle(self._translate("Dialog_AddIndicator_Parameters", "Inputs"))
        self.groupBox_parameters.setTitle(self._translate("Dialog_AddIndicator_Parameters", "Parameters"))

    def submit(self):
        self.params = {}
        for key in self.indicator_template_params.keys():
            self.params[key] = self.dic_spinBox_parameter[key].value()
        self.inputs_name = {}
        for key in self.indicator_template_inputs.keys():
            self.inputs_name[key] = self.dic_comboBox_input[key].currentText()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_AddIndicator_Parameters = QtWidgets.QDialog()
    ui = Ui_Dialog_AddIndicator_Parameters()
    ui.setupUi(Dialog_AddIndicator_Parameters)
    Dialog_AddIndicator_Parameters.show()
    sys.exit(app.exec_())
