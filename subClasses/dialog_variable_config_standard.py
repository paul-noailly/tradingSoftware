# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subClasses/dialog_variable_config_standard.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg, time, datetime, numpy as np
from subClasses.standardPlotItem import StandardPlotItem


class Ui_Dialog_ConfigVariableStandard(object):
    def setupUi(self, Dialog_ConfigVariableStandard, dic_current_param):
        Dialog_ConfigVariableStandard.setObjectName("Dialog_ConfigVariableStandard")
        Dialog_ConfigVariableStandard.resize(463, 288)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_ConfigVariableStandard)
        self.buttonBox.setGeometry(QtCore.QRect(160, 240, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_ConfigVariableStandard)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName("label")
        self.comboBox_timeframe = QtWidgets.QComboBox(Dialog_ConfigVariableStandard)
        self.comboBox_timeframe.setGeometry(QtCore.QRect(148, 10, 51, 20))
        self.comboBox_timeframe.setObjectName("comboBox_timeframe")
        self.comboBox_timeframe.addItem("")
        self.comboBox_timeframe.addItem("")
        self.comboBox_timeframe.addItem("")
        self.comboBox_timeframe.addItem("")
        self.comboBox_timeframe.addItem("")
        self.comboBox_timeframe.addItem("")
        self.spinBox_timeframe = QtWidgets.QSpinBox(Dialog_ConfigVariableStandard)
        self.spinBox_timeframe.setGeometry(QtCore.QRect(100, 10, 41, 20))
        self.spinBox_timeframe.setObjectName("spinBox_timeframe")
        self.label_2 = QtWidgets.QLabel(Dialog_ConfigVariableStandard)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_ConfigVariableStandard)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.comboBox_Style = QtWidgets.QComboBox(Dialog_ConfigVariableStandard)
        self.comboBox_Style.setGeometry(QtCore.QRect(100, 100, 69, 20))
        self.comboBox_Style.setObjectName("comboBox_Style")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.widget_PreviewGraph = QtWidgets.QWidget(Dialog_ConfigVariableStandard)
        self.widget_PreviewGraph.setGeometry(QtCore.QRect(200, 63, 221, 121))
        self.widget_PreviewGraph.setObjectName("widget_PreviewGraph")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_PreviewGraph)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog_ConfigVariableStandard)
        self.label_4.setGeometry(QtCore.QRect(20, 201, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog_ConfigVariableStandard)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 47, 13))
        self.label_5.setObjectName("label_5")
        self.comboBox_selectDock = QtWidgets.QComboBox(Dialog_ConfigVariableStandard)
        self.comboBox_selectDock.setGeometry(QtCore.QRect(100, 201, 69, 20))
        self.comboBox_selectDock.setObjectName("comboBox_selectDock")
        self.comboBox_selectDock.addItem("")
        self.comboBox_selectDock.addItem("")
        self.pushButton_createDock = QtWidgets.QPushButton(Dialog_ConfigVariableStandard)
        self.pushButton_createDock.setGeometry(QtCore.QRect(180, 200, 91, 22))
        self.pushButton_createDock.setObjectName("pushButton_createDock")
        self.pushButton_defaultParams = QtWidgets.QPushButton(Dialog_ConfigVariableStandard)
        self.pushButton_defaultParams.setGeometry(QtCore.QRect(370, 10, 51, 20))
        self.pushButton_defaultParams.setObjectName("pushButton_defaultParams")
        self.pushButton_showPreview = QtWidgets.QPushButton(Dialog_ConfigVariableStandard)
        self.pushButton_showPreview.setGeometry(QtCore.QRect(280, 40, 75, 20))
        self.pushButton_showPreview.setObjectName("pushButton_showPreview")
        self.widget_getColorButton = QtWidgets.QWidget(Dialog_ConfigVariableStandard)
        self.widget_getColorButton.setGeometry(QtCore.QRect(100, 66, 69, 20))
        self.widget_getColorButton.setObjectName("widget_getColorButton")
        self.spinBox_width = QtWidgets.QSpinBox(Dialog_ConfigVariableStandard)
        self.spinBox_width.setGeometry(QtCore.QRect(100, 130, 51, 20))
        self.spinBox_width.setObjectName("spinBox_width")
        
        # buttons fonctions
        self.pushButton_showPreview.clicked.connect(self.show_preview)
        self.pushButton_createDock.clicked.connect(self.create_new_dock)
        self.pushButton_defaultParams.clicked.connect(self.set_default_params)

        # Graph widget of preview
        self.w_plotWidget = pg.PlotWidget(parent=self.widget_PreviewGraph, axisItems = {'bottom': pg.DateAxisItem()})
        self.w_plotWidget.setBackground('w')
        self.w_plotWidget.showGrid(x=True, y=True)
        self.verticalLayout.addWidget(self.w_plotWidget)
        
        # variables
        self.dic_current_param = dic_current_param
        self.dic_default_param = {'type_config': "standard",'tf_nbs':self.dic_current_param['tf_nbs'], 'tf_metric':self.dic_current_param['tf_metric'], 'color':pg.mkColor('b'), 'style':'solid', 'width':1, 'dock':'main'}
        self.pushButton_Color = pg.ColorButton(self.widget_getColorButton)
        
        # initailize all variables
        self.set_dialog_values()

        self.retranslateUi(Dialog_ConfigVariableStandard)
        self.buttonBox.accepted.connect(Dialog_ConfigVariableStandard.accept)
        self.buttonBox.accepted.connect(self.submit)
        self.buttonBox.rejected.connect(Dialog_ConfigVariableStandard.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ConfigVariableStandard)
        
        self.plot_PreviewGraph()

    def retranslateUi(self, Dialog_ConfigVariableStandard):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ConfigVariableStandard.setWindowTitle(_translate("Dialog_ConfigVariableStandard", "Dialog"))
        self.label.setText(_translate("Dialog_ConfigVariableStandard", "Edit timeframe:"))
        self.comboBox_timeframe.setItemText(0, _translate("Dialog_ConfigVariableStandard", "sec"))
        self.comboBox_timeframe.setItemText(1, _translate("Dialog_ConfigVariableStandard", "min"))
        self.comboBox_timeframe.setItemText(2, _translate("Dialog_ConfigVariableStandard", "hour"))
        self.comboBox_timeframe.setItemText(3, _translate("Dialog_ConfigVariableStandard", "day"))
        self.comboBox_timeframe.setItemText(4, _translate("Dialog_ConfigVariableStandard", "month"))
        self.comboBox_timeframe.setItemText(5, _translate("Dialog_ConfigVariableStandard", "tick"))
        self.label_2.setText(_translate("Dialog_ConfigVariableStandard", "Edit color:"))
        self.label_3.setText(_translate("Dialog_ConfigVariableStandard", "Edit style:"))
        self.comboBox_Style.setItemText(0, _translate("Dialog_ConfigVariableStandard", "solid"))
        self.comboBox_Style.setItemText(1, _translate("Dialog_ConfigVariableStandard", "dash"))
        self.comboBox_Style.setItemText(2, _translate("Dialog_ConfigVariableStandard", "dot"))
        self.comboBox_Style.setItemText(3, _translate("Dialog_ConfigVariableStandard", "dash-dot"))
        self.label_4.setText(_translate("Dialog_ConfigVariableStandard", "Edit dock:"))
        self.label_5.setText(_translate("Dialog_ConfigVariableStandard", "Edit width:"))
        self.comboBox_selectDock.setItemText(0, _translate("Dialog_ConfigVariableStandard", "main"))
        self.comboBox_selectDock.setItemText(1, _translate("Dialog_ConfigVariableStandard", "osci"))
        self.pushButton_createDock.setText(_translate("Dialog_ConfigVariableStandard", "create new dock"))
        self.pushButton_defaultParams.setText(_translate("Dialog_ConfigVariableStandard", "Default"))
        self.pushButton_showPreview.setText(_translate("Dialog_ConfigVariableStandard", "Show preview"))
        
    def color_to_QtColor(self, elt):
        if type(elt) is str and len(elt) == 1:
            return pg.mkColor(elt)
        elif type(elt) is list and len(elt)==4:
            return pg.mkColor(tuple(elt))
        else:
            print('error unknown color type for ',elt)
            
    def Qtcolor_to_list_rgb(self, color):
        rgb = color.getRgb()
        return [i for i in rgb]
        
    def set_dialog_values(self):
        self.spinBox_timeframe.setValue(self.dic_current_param['tf_nbs'])
        self.comboBox_timeframe.setCurrentText(self.dic_current_param['tf_metric'])
        self.pushButton_Color.setColor(self.color_to_QtColor(self.dic_current_param['color']))
        self.comboBox_Style.setCurrentText(self.dic_current_param['style'])
        self.spinBox_width.setValue(self.dic_current_param['width'])
        self.comboBox_selectDock.setCurrentText(self.dic_current_param['dock'])
        
    def style_str_to_qt(self, style_str):
        '''transform the style as a string (input) to a Qt model of style object'''
        if style_str == 'solid':
            return QtCore.Qt.SolidLine
        elif style_str == 'dash':
            return QtCore.Qt.DashLine
        elif style_str == 'dot':
            return QtCore.Qt.DotLine
        elif style_str == 'dash-dot':
            return QtCore.Qt.DashDotLine
        else:
            print('unknown style: ',style_str)
            return 1        
        
    def set_default_params(self):
        self.dic_current_param = self.dic_default_param
        self.set_dialog_values()
        
    def update_dic_param(self):
        '''Extract the values from the input dialogs, and save it in the current dictionnary of param'''
        tf_nbs = self.spinBox_timeframe.value()
        tf_metric = self.comboBox_timeframe.currentText()
        color = self.Qtcolor_to_list_rgb(self.pushButton_Color.color())
        style = self.comboBox_Style.currentText()
        width = self.spinBox_width.value()
        dock = self.comboBox_selectDock.currentText()
        type_config = self.dic_current_param['type_config']
        self.dic_current_param = {'type_config':type_config, 'tf_nbs':tf_nbs, 'tf_metric':tf_metric, 'color':color, 'style':style, 'width':width, 'dock':dock}
        
    def plot_PreviewGraph(self):
        '''Use the current parameters selected to plot a preview of how the graph looks'''
        print('plotting preview with param ', self.dic_current_param)
        self.w_plotWidget.clear()
        # creating item
        item_to_plot = self.get_item_to_plot()
        self.w_plotWidget.addItem(item_to_plot)


    def get_item_to_plot(self):
        now = time.time()
        time_array = np.array([now+60*60*i for i in range(6)])
        value_array = np.array([10, 13, 17, 14, 15, 9])
        config = self.dic_current_param
        item_to_plot = StandardPlotItem(time_array, value_array, config)
        return item_to_plot
        
    def show_preview(self):
        self.update_dic_param()
        self.plot_PreviewGraph()
        
    def create_new_dock(self):
        '''Open a dialog, that ask the new dock name and where to place it depending and the existing dock
        Once created (i.e submit) add the dock name and default position to the list of dock indicated in the json work file'''
        print('a new dock have been created')
        
    def submit(self):
        self.update_dic_param()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_ConfigVariableStandard = QtWidgets.QDialog()
    ui = Ui_Dialog_ConfigVariableStandard()
    ui.setupUi(Dialog_ConfigVariableStandard)
    Dialog_ConfigVariableStandard.show()
    sys.exit(app.exec_())
