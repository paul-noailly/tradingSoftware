# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subClasses/dialog_variable_config_ohlc.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg, time, datetime, numpy as np
from subClasses.candlestickItem import CandlestickItem


class Ui_Dialog_ConfigVariableOHLC(object):
    def setupUi(self, Dialog_ConfigVariableOHLC, dic_current_param):
        Dialog_ConfigVariableOHLC.setObjectName("Dialog_ConfigVariableOHLC")
        Dialog_ConfigVariableOHLC.resize(517, 402)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_ConfigVariableOHLC)
        self.buttonBox.setGeometry(QtCore.QRect(170, 360, 160, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName("label")
        self.comboBox_timeframe = QtWidgets.QComboBox(Dialog_ConfigVariableOHLC)
        self.comboBox_timeframe.setGeometry(QtCore.QRect(148, 10, 51, 20))
        self.comboBox_timeframe.setObjectName("comboBox_timeframe")
        self.comboBox_timeframe.addItem("")
        self.comboBox_timeframe.addItem("")
        self.comboBox_timeframe.addItem("")
        self.comboBox_timeframe.addItem("")
        self.comboBox_timeframe.addItem("")
        self.spinBox_timeframe = QtWidgets.QSpinBox(Dialog_ConfigVariableOHLC)
        self.spinBox_timeframe.setGeometry(QtCore.QRect(100, 10, 41, 20))
        self.spinBox_timeframe.setObjectName("spinBox_timeframe")
        self.label_2 = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 81, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_StyleWick = QtWidgets.QComboBox(Dialog_ConfigVariableOHLC)
        self.comboBox_StyleWick.setGeometry(QtCore.QRect(140, 109, 69, 20))
        self.comboBox_StyleWick.setObjectName("comboBox_StyleWick")
        self.comboBox_StyleWick.addItem("")
        self.comboBox_StyleWick.addItem("")
        self.comboBox_StyleWick.addItem("")
        self.comboBox_StyleWick.addItem("")
        self.widget_PreviewGraph = QtWidgets.QWidget(Dialog_ConfigVariableOHLC)
        self.widget_PreviewGraph.setGeometry(QtCore.QRect(240, 66, 241, 241))
        self.widget_PreviewGraph.setObjectName("widget_PreviewGraph")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_PreviewGraph)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label_4.setGeometry(QtCore.QRect(20, 320, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 81, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_selectDock = QtWidgets.QComboBox(Dialog_ConfigVariableOHLC)
        self.comboBox_selectDock.setGeometry(QtCore.QRect(100, 321, 69, 20))
        self.comboBox_selectDock.setObjectName("comboBox_selectDock")
        self.comboBox_selectDock.addItem("")
        self.comboBox_selectDock.addItem("")
        self.pushButton_createDock = QtWidgets.QPushButton(Dialog_ConfigVariableOHLC)
        self.pushButton_createDock.setGeometry(QtCore.QRect(180, 320, 91, 22))
        self.pushButton_createDock.setObjectName("pushButton_createDock")
        self.label_7 = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label_9.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.label_9.setObjectName("label_9")
        self.comboBox_StyleBody = QtWidgets.QComboBox(Dialog_ConfigVariableOHLC)
        self.comboBox_StyleBody.setGeometry(QtCore.QRect(140, 199, 69, 20))
        self.comboBox_StyleBody.setObjectName("comboBox_StyleBody")
        self.comboBox_StyleBody.addItem("")
        self.comboBox_StyleBody.addItem("")
        self.comboBox_StyleBody.addItem("")
        self.comboBox_StyleBody.addItem("")
        self.pushButton_defaultParams = QtWidgets.QPushButton(Dialog_ConfigVariableOHLC)
        self.pushButton_defaultParams.setGeometry(QtCore.QRect(430, 10, 51, 22))
        self.pushButton_defaultParams.setObjectName("pushButton_defaultParams")
        self.pushButton_ShowPreview = QtWidgets.QPushButton(Dialog_ConfigVariableOHLC)
        self.pushButton_ShowPreview.setGeometry(QtCore.QRect(320, 40, 75, 22))
        self.pushButton_ShowPreview.setObjectName("pushButton_ShowPreview")
        self.label_10 = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label_10.setGeometry(QtCore.QRect(20, 260, 81, 16))
        self.label_10.setObjectName("label_10")
        self.widget_colorBody = QtWidgets.QWidget(Dialog_ConfigVariableOHLC)
        self.widget_colorBody.setGeometry(QtCore.QRect(140, 260, 71, 20))
        self.widget_colorBody.setObjectName("widget_colorBody")
        self.label_6 = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 81, 16))
        self.label_6.setObjectName("label_6")
        self.widget_colorWick = QtWidgets.QWidget(Dialog_ConfigVariableOHLC)
        self.widget_colorWick.setGeometry(QtCore.QRect(140, 170, 71, 20))
        self.widget_colorWick.setObjectName("widget_colorWick")
        self.widget_colorRedCandle = QtWidgets.QWidget(Dialog_ConfigVariableOHLC)
        self.widget_colorRedCandle.setGeometry(QtCore.QRect(140, 80, 71, 20))
        self.widget_colorRedCandle.setObjectName("widget_colorRedCandle")
        self.widget_colorGreenCandle = QtWidgets.QWidget(Dialog_ConfigVariableOHLC)
        self.widget_colorGreenCandle.setGeometry(QtCore.QRect(140, 50, 71, 20))
        self.widget_colorGreenCandle.setObjectName("widget_colorGreenCandle")
        self.doubleSpinBox_percentWidthCandle = QtWidgets.QDoubleSpinBox(Dialog_ConfigVariableOHLC)
        self.doubleSpinBox_percentWidthCandle.setGeometry(QtCore.QRect(140, 290, 71, 20))
        self.doubleSpinBox_percentWidthCandle.setObjectName("doubleSpinBox_percentWidthCandle")
        self.doubleSpinBox_percentWidthCandle.setSingleStep(0.01)
        self.spinBox_widthWick = QtWidgets.QSpinBox(Dialog_ConfigVariableOHLC)
        self.spinBox_widthWick.setGeometry(QtCore.QRect(140, 140, 71, 20))
        self.spinBox_widthWick.setObjectName("spinBox_widthWick")
        self.spinBox_widthBody = QtWidgets.QSpinBox(Dialog_ConfigVariableOHLC)
        self.spinBox_widthBody.setGeometry(QtCore.QRect(140, 230, 71, 20))
        self.spinBox_widthBody.setObjectName("spinBox_widthBody")
        self.label_11 = QtWidgets.QLabel(Dialog_ConfigVariableOHLC)
        self.label_11.setGeometry(QtCore.QRect(20, 290, 111, 16))
        self.label_11.setObjectName("label_11")
        
        # buttons fonctions
        self.pushButton_ShowPreview.clicked.connect(self.show_preview)
        self.pushButton_createDock.clicked.connect(self.create_new_dock)
        self.pushButton_defaultParams.clicked.connect(self.set_default_params)

        # Graph widget preview
        self.w_plotWidget = pg.PlotWidget(parent=self.widget_PreviewGraph, axisItems = {'bottom': pg.DateAxisItem()})
        self.w_plotWidget.setBackground('w')
        self.w_plotWidget.showGrid(x=True, y=True)
        self.verticalLayout.addWidget(self.w_plotWidget)
        
        # variables
        self.dic_current_param = dic_current_param
        self.dic_default_param = {'type_config': "ohlc", 'tf_nbs':self.dic_current_param['tf_nbs'], 'tf_metric':self.dic_current_param['tf_metric'], 
                                  'color_gCandle':pg.mkColor('g'), 'color_rCandle':pg.mkColor('r'),
                                  'color_wick':pg.mkColor('k'), 'style_wick':'solid', 'width_wick':1, 
                                  'color_body':pg.mkColor('k'), 'style_body':'solid', 'width_body':1, 'dock':'main', 'percentWidthCandle':0.9}
        #color button
        self.pushButton_colorGreenCandle = pg.ColorButton(self.widget_colorGreenCandle)
        self.pushButton_colorRedCandle = pg.ColorButton(self.widget_colorRedCandle)
        self.pushButton_colorWick = pg.ColorButton(self.widget_colorWick)
        self.pushButton_colorBody = pg.ColorButton(self.widget_colorBody)
        
        # initailize all variables
        self.set_dialog_values()

        self.retranslateUi(Dialog_ConfigVariableOHLC)
        self.buttonBox.accepted.connect(Dialog_ConfigVariableOHLC.accept)
        self.buttonBox.accepted.connect(self.submit)
        self.buttonBox.rejected.connect(Dialog_ConfigVariableOHLC.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ConfigVariableOHLC)
        
        self.plot_PreviewGraph()

    def retranslateUi(self, Dialog_ConfigVariableOHLC):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ConfigVariableOHLC.setWindowTitle(_translate("Dialog_ConfigVariableOHLC", "Dialog"))
        self.label.setText(_translate("Dialog_ConfigVariableOHLC", "Edit timeframe:"))
        self.comboBox_timeframe.setItemText(0, _translate("Dialog_ConfigVariableOHLC", "sec"))
        self.comboBox_timeframe.setItemText(1, _translate("Dialog_ConfigVariableOHLC", "min"))
        self.comboBox_timeframe.setItemText(2, _translate("Dialog_ConfigVariableOHLC", "hour"))
        self.comboBox_timeframe.setItemText(3, _translate("Dialog_ConfigVariableOHLC", "day"))
        self.comboBox_timeframe.setItemText(4, _translate("Dialog_ConfigVariableOHLC", "month"))
        self.label_2.setText(_translate("Dialog_ConfigVariableOHLC", "Edit color green candle:"))
        self.label_3.setText(_translate("Dialog_ConfigVariableOHLC", "Edit style wick:"))
        self.comboBox_StyleWick.setItemText(0, _translate("Dialog_ConfigVariableOHLC", "solid"))
        self.comboBox_StyleWick.setItemText(1, _translate("Dialog_ConfigVariableOHLC", "dash"))
        self.comboBox_StyleWick.setItemText(2, _translate("Dialog_ConfigVariableOHLC", "dot"))
        self.comboBox_StyleWick.setItemText(3, _translate("Dialog_ConfigVariableOHLC", "dash-dot"))
        self.label_4.setText(_translate("Dialog_ConfigVariableOHLC", "Edit dock:"))
        self.label_5.setText(_translate("Dialog_ConfigVariableOHLC", "Edit width wick:"))
        self.comboBox_selectDock.setItemText(0, _translate("Dialog_ConfigVariableOHLC", "main"))
        self.comboBox_selectDock.setItemText(1, _translate("Dialog_ConfigVariableOHLC", "osci"))
        self.pushButton_createDock.setText(_translate("Dialog_ConfigVariableOHLC", "create new dock"))
        self.label_7.setText(_translate("Dialog_ConfigVariableOHLC", "Edit color red candle:"))
        self.label_8.setText(_translate("Dialog_ConfigVariableOHLC", "Edit style body:"))
        self.label_9.setText(_translate("Dialog_ConfigVariableOHLC", "Edit width body:"))
        self.comboBox_StyleBody.setItemText(0, _translate("Dialog_ConfigVariableOHLC", "solid"))
        self.comboBox_StyleBody.setItemText(1, _translate("Dialog_ConfigVariableOHLC", "dash"))
        self.comboBox_StyleBody.setItemText(2, _translate("Dialog_ConfigVariableOHLC", "dot"))
        self.comboBox_StyleBody.setItemText(3, _translate("Dialog_ConfigVariableOHLC", "dash-dot"))
        self.pushButton_defaultParams.setText(_translate("Dialog_ConfigVariableOHLC", "Default"))
        self.pushButton_ShowPreview.setText(_translate("Dialog_ConfigVariableOHLC", "Show Preview"))
        self.label_10.setText(_translate("Dialog_ConfigVariableOHLC", "Edit color body:"))
        self.label_6.setText(_translate("Dialog_ConfigVariableOHLC", "Edit color wick:"))
        self.label_11.setText(_translate("Dialog_ConfigVariableOHLC", "Edit width ratio candle:"))
        
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
        self.pushButton_colorGreenCandle.setColor(self.color_to_QtColor(self.dic_current_param['color_gCandle']))
        self.pushButton_colorRedCandle.setColor(self.color_to_QtColor(self.dic_current_param['color_rCandle']))
        self.pushButton_colorWick.setColor(self.color_to_QtColor(self.dic_current_param['color_wick']))
        self.comboBox_StyleWick.setCurrentText(self.dic_current_param['style_wick'])
        self.spinBox_widthWick.setValue(self.dic_current_param['width_wick'])
        self.pushButton_colorBody.setColor(self.color_to_QtColor(self.dic_current_param['color_body']))
        self.comboBox_StyleBody.setCurrentText(self.dic_current_param['style_body'])
        self.spinBox_widthBody.setValue(self.dic_current_param['width_body'])
        self.comboBox_selectDock.setCurrentText(self.dic_current_param['dock'])
        self.doubleSpinBox_percentWidthCandle.setValue(self.dic_current_param['percentWidthCandle'])
        
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
        color_gCandle = self.Qtcolor_to_list_rgb(self.pushButton_colorGreenCandle.color())
        color_rCandle = self.Qtcolor_to_list_rgb(self.pushButton_colorRedCandle.color())
        color_wick = self.Qtcolor_to_list_rgb(self.pushButton_colorWick.color())
        style_wick = self.comboBox_StyleWick.currentText()
        width_wick = self.spinBox_widthWick.value()
        color_body = self.Qtcolor_to_list_rgb(self.pushButton_colorBody.color())
        style_body = self.comboBox_StyleBody.currentText()
        width_body = self.spinBox_widthBody.value()
        dock = self.comboBox_selectDock.currentText()
        percentWidthCandle = self.doubleSpinBox_percentWidthCandle.value()
        type_config = self.dic_current_param['type_config']
        self.dic_current_param = {'type_config':type_config, 'tf_nbs':tf_nbs, 'tf_metric':tf_metric, 'color_gCandle':color_gCandle, 'color_rCandle':color_rCandle,
                                  'color_wick':color_wick, 'style_wick':style_wick, 'width_wick':width_wick, 
                                  'color_body':color_body, 'style_body':style_body, 'width_body':width_body, 'dock':dock,
                                  'percentWidthCandle':percentWidthCandle}
        
    def plot_PreviewGraph(self):
        '''Use the current parameters selected to plot a preview of how the graph looks'''
        self.w_plotWidget.clear()
        # creating item
        item_to_plot = self.get_item_to_plot()
        self.w_plotWidget.addItem(item_to_plot)

        
    def get_item_to_plot(self):
        now = time.time()-56*60
        time_array = np.array([now+60*60*i for i in range(6)])
        open_array = np.array([10, 13, 17, 14, 15, 9])
        close_array = np.array([13, 17, 14, 15, 9, 15])
        low_array = np.array([5, 9, 11, 5, 8, 8])
        high_array = np.array([15, 20, 23, 19, 22, 16])
        config = self.dic_current_param
        item_to_plot = CandlestickItem(time_array, open_array, high_array, low_array, close_array, config)
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
    Dialog_ConfigVariableOHLC = QtWidgets.QDialog()
    ui = Ui_Dialog_ConfigVariableOHLC()
    ui.setupUi(Dialog_ConfigVariableOHLC)
    Dialog_ConfigVariableOHLC.show()
    sys.exit(app.exec_())
