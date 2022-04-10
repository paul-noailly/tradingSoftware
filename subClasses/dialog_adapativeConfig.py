# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_adapativeConfig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from subClasses.plotItemGenerator import PlotItemGenerator
import pyqtgraph as pg, numpy as np


class Ui_Dialog_adaptativeConfig(object):
    def setupUi(self, Dialog_adaptativeConfig, config_builder, current_config, default_config, dic_dock, plot_builder):
        self.max_line_per_groupBox = 16 # not used but can be used later in the loops if needed
        self.dic_dock = dic_dock
        self.list_dock = [self.dic_dock[key][name] for key in self.dic_dock.keys()]
        self.default_config = default_config
        self.current_config = current_config
        self.config_builder = config_builder
        self.list_available_style = ['solid','dash','dot','dash-dot']
        self.plot_builder = plot_builder

        Dialog_adaptativeConfig.setObjectName("Dialog_adaptativeConfig")
        Dialog_adaptativeConfig.resize(750, 612)
        # button box
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_adaptativeConfig)
        self.buttonBox.setGeometry(QtCore.QRect(400, 570, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        # display name
        self.groupBox = QtWidgets.QGroupBox(Dialog_adaptativeConfig)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 351, 56))
        self.groupBox.setObjectName("groupBox")
        self.label_displayname = QtWidgets.QLabel(self.groupBox)
        self.label_displayname.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_displayname.setObjectName("label_displayname")
        self.textEdit_displaName = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_displaName.setGeometry(QtCore.QRect(110, 20, 221, 21))
        self.textEdit_displaName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_displaName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_displaName.setObjectName("textEdit_displaName")
        # preview graph
        self.widget_graphPreview = QtWidgets.QWidget(Dialog_adaptativeConfig)
        self.widget_graphPreview.setGeometry(QtCore.QRect(270, 110, 451, 421))
        self.widget_graphPreview.setObjectName("widget_graphPreview")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_graphPreview)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_graphPreview = QtWidgets.QPushButton(Dialog_adaptativeConfig)
        self.pushButton_graphPreview.setGeometry(QtCore.QRect(450, 80, 75, 23))
        self.pushButton_graphPreview.setObjectName("pushButton_graphPreview")
        # default param
        self.pushButton_defaultParameters = QtWidgets.QPushButton(Dialog_adaptativeConfig)
        self.pushButton_defaultParameters.setGeometry(QtCore.QRect(574, 30, 121, 23))
        self.pushButton_defaultParameters.setObjectName("pushButton_defaultParameters")
        # stacked widget 
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog_adaptativeConfig)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 70, 231, 541))
        self.stackedWidget.setObjectName("stackedWidget")
        # page 1 and group box 1
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.groupBox_config1 = QtWidgets.QGroupBox(self.page)
        self.groupBox_config1.setGeometry(QtCore.QRect(0, 20, 221, 511))
        self.groupBox_config1.setObjectName("groupBox_config1")
        self.stackedWidget.addWidget(self.page)
        # page 2 and group box 2
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.groupBox_config2 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_config2.setGeometry(QtCore.QRect(0, 20, 221, 511))
        self.groupBox_config2.setObjectName("groupBox_config2")
        self.stackedWidget.addWidget(self.page_2)
        # translate
        self.retranslateUi(Dialog_adaptativeConfig)
        QtCore.QMetaObject.connectSlotsByName(Dialog_adaptativeConfig)
        # lines:
        self.dic_label_config_param = {}
        self.dic_widget_config_param = {}
        self.dic_color_dialog = {}
        self.list_config_key = [key for key in self.config_builder.keys()]
        for i in range(len(self.config_builder)): # we go trhough each config parameter with config_builder
            name_config_param = self.list_config_key[i]
            type_config_param = self.config_builder[name_config_param]
            if name_config_param != 'diplay_name': # display name is already put in 1st group box
                if i < 16: # bellow 16 we put widget in group box 1
                    # placing label
                    self.dic_label_config_param[name_config_param] = QtWidgets.QLabel(self.groupBox_config1)
                    self.dic_label_config_param[name_config_param].setGeometry(QtCore.QRect(20, 30+i*30, 90, 18))
                    self.dic_label_config_param[name_config_param].setObjectName('label_'+name_config_param)
                    self.dic_label_config_param[name_config_param].setText(self.self._translate("Dialog_adaptativeConfig", name_config_param.replace('_',' ')+':'))
                    # placing widget
                    if type_config_param == 'color':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QWidget(self.groupBox_config1)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+i*30, 80, 25))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                        self.dic_color_dialog[name_config_param] = pg.ColorButton(self.dic_widget_config_param[name_config_param])
                        self.dic_color_dialog[name_config_param].setText(self._translate("Dialog_adaptativeConfig", "Edit Color"))
                    elif type_config_param == 'style':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QComboBox(self.groupBox_config1)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+i*30, 80, 23))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                        index_style = 0 
                        for name_style in list_available_style:
                            self.dic_widget_config_param[name_config_param].addItem("")
                            self.dic_widget_config_param[name_config_param].setItemText(index_style, self._translate("Dialog_adaptativeConfig", name_style))
                            index_style += 1
                    elif type_config_param == 'spinInt':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QSpinBox(self.groupBox_config1)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+i*30, 80, 23))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                    elif type_config_param == 'checkBox':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QCheckBox(self.groupBox_config1)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+i*30, 80, 23))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                        self.dic_widget_config_param[name_config_param].setText(self._translate("Dialog_adaptativeConfig", 'Toggle Param'))
                    elif type_config_param == 'dock':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QComboBox(self.groupBox_config1)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+i*30, 80, 23))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                        index_dock = 0 
                        for name_dock in self.list_dock:
                            self.dic_widget_config_param[name_config_param].addItem("")
                            self.dic_widget_config_param[name_config_param].setItemText(index_dock, self._translate("Dialog_adaptativeConfig", name_dock))
                            index_dock += 1
                    elif type_config_param[:5] == 'spin_':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QDoubleSpinBox(self.groupBox_config1)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+i*30, 80, 23))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                        step = float(type_config_param[5:])
                        self.dic_widget_config_param[name_config_param].setSingleStep(step)
                    else:
                        print('ERROR : unknown type config ({}) during the building of the config param dialog'.format(type_config_param))
                elif i < 32: # between 16 and 32 we put widgets in group box 2
                    # placing label
                    self.dic_label_config_param[name_config_param] = QtWidgets.QLabel(self.groupBox_config2)
                    self.dic_label_config_param[name_config_param].setGeometry(QtCore.QRect(20, 30+(i-16)*30, 90, 18))
                    self.dic_label_config_param[name_config_param].setObjectName('label_'+name_config_param)
                    self.dic_label_config_param[name_config_param].setText(self._translate("Dialog_adaptativeConfig", name_config_param.replace('_',' ')+':'))
                    # placing widget
                    if type_config_param == 'color':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QWidget(self.groupBox_config2)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+(i-16)*30, 80, 25))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                        self.dic_color_dialog[name_config_param] = pg.ColorButton(self.dic_widget_config_param[name_config_param])
                        self.dic_color_dialog[name_config_param].setText(self._translate("Dialog_adaptativeConfig", "Edit Color"))
                    elif type_config_param == 'style':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QComboBox(self.groupBox_config2)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+(i-16)*30, 80, 23))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                        index_style = 0 
                        for name_style in list_available_style:
                            self.dic_widget_config_param[name_config_param].addItem("")
                            self.dic_widget_config_param[name_config_param].setItemText(index_style, self._translate("Dialog_adaptativeConfig", name_style))
                            index_style += 1
                    elif type_config_param == 'spinInt':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QSpinBox(self.groupBox_config2)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+(i-16)*30, 80, 23))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                    elif type_config_param == 'checkBox':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QCheckBox(self.groupBox_config2)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+(i-16)*30, 80, 23))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                        self.dic_widget_config_param[name_config_param].setText(self._translate("Dialog_adaptativeConfig", 'Toggle Param'))
                    elif type_config_param == 'dock':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QComboBox(self.groupBox_config2)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+(i-16)*30, 80, 23))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                        index_dock = 0 
                        for name_dock in self.list_dock:
                            self.dic_widget_config_param[name_config_param].addItem("")
                            self.dic_widget_config_param[name_config_param].setItemText(index_dock, self._translate("Dialog_adaptativeConfig", name_dock))
                            index_dock += 1
                    elif type_config_param[:5] == 'spin_':
                        self.dic_widget_config_param[name_config_param] = QtWidgets.QDoubleSpinBox(self.groupBox_config2)
                        self.dic_widget_config_param[name_config_param].setGeometry(QtCore.QRect(120, 27+(i-16)*30, 80, 23))
                        self.dic_widget_config_param[name_config_param].setObjectName('widget_'+name_config_param)
                        step = float(type_config_param[5:])
                        self.dic_widget_config_param[name_config_param].setSingleStep(step)
                    else:
                        print('ERROR : unknown type config ({}) during the building of the config param dialog'.format(type_config_param))
                else:
                    print('ERROR There is more than 32 config parameter. The code is not designed for that')


        self.stackedWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(self.submit)
        self.buttonBox.accepted.connect(Dialog_adaptativeConfig.accept)
        self.buttonBox.rejected.connect(Dialog_adaptativeConfig.reject)

        # buttons fonctions
        self.pushButton_graphPreview.clicked.connect(self.show_preview)
        self.pushButton_defaultParameters.clicked.connect(self.set_default_config)

        # Graph widget preview
        self.w_plotWidget = pg.PlotWidget(parent=self.widget_graphPreview, axisItems = {'bottom': pg.DateAxisItem()})
        self.w_plotWidget.setBackground('w')
        self.w_plotWidget.showGrid(x=True, y=True)
        self.verticalLayout.addWidget(self.w_plotWidget)

        self.set_current_config()

    def retranslateUi(self, Dialog_adaptativeConfig):
        self._translate = QtCore.QCoreApplication.translate
        Dialog_adaptativeConfig.setWindowTitle(self._translate("Dialog_adaptativeConfig", "Dialog"))
        self.groupBox.setTitle(self._translate("Dialog_adaptativeConfig", "Display Name"))
        self.label_displayname.setText(self._translate("Dialog_adaptativeConfig", "Display Name:"))
        self.pushButton_graphPreview.setText(self._translate("Dialog_adaptativeConfig", "Preview"))
        self.pushButton_defaultParameters.setText(self._translate("Dialog_adaptativeConfig", "Default Parameters"))
        self.groupBox_config1.setTitle(self._translate("Dialog_adaptativeConfig", "Graph Look Config 1/2"))
        self.groupBox_config2.setTitle(self._translate("Dialog_adaptativeConfig", "Graph Look Config 2/2"))

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

    def set_current_config(self):
        '''Take variables from current config and initialized the default value of all widget with it'''
        config = self.current_config
        self.set_config_params(config)

    def set_default_config(self):
        config = self.default_config
        self.set_config_params(config)

    def set_config_params(self, config):
        list_config_key = [key for key in config.keys()]
        for i in range(len(config)):
            name_config_param = list_config_key[i]
            value_config = config[name_config_param]
            if type_config_param == 'color':
                self.dic_color_dialog[name_config_param].setColor(self.color_to_QtColor(value_config))
            elif type_config_param == 'style':
                self.dic_widget_config_param[name_config_param].setCurrentText(value_config)
            elif type_config_param == 'spinInt':
                self.dic_widget_config_param[name_config_param].setValue(value_config)
            elif type_config_param == 'checkBox':
                self.dic_widget_config_param[name_config_param].setCheckState(value_config)
            elif type_config_param == 'dock':
                self.dic_widget_config_param[name_config_param].setCurrentText(value_config)
            elif type_config_param[:5] == 'spin_':
                self.dic_widget_config_param[name_config_param].setValue(value_config)

    def get_current_config(self):
        result_config = {}
        result_config['display_name'] = self.textEdit_displaName.toPlainText()
        for i in range(len(self.config_builder)):
            name_config_param = self.list_config_key[i]
            type_config_param = self.config_builder[name_config_param]
            if type_config_param == 'color':
                result_config[name_config_param] = self.Qtcolor_to_list_rgb(self.dic_color_dialog[name_config_param].color())
            elif type_config_param == 'style':
                result_config[name_config_param] = self.dic_widget_config_param[name_config_param].currentText()
            elif type_config_param == 'spinInt':
                result_config[name_config_param] = self.dic_widget_config_param[name_config_param].value()
            elif type_config_param == 'checkBox':
                result_config[name_config_param] = self.dic_widget_config_param[name_config_param].checkState()
            elif type_config_param == 'dock':
                result_config[name_config_param] = self.dic_widget_config_param[name_config_param].currentText()
            elif type_config_param[:5] == 'spin_':
                result_config[name_config_param] = self.dic_widget_config_param[name_config_param].value()
        return result_config

    def show_preview(self):
        self.w_plotWidget.clear()
        current_config = self.get_current_config()
        plotItemGenerator = plotItemGenerator(plot_builder=self.plot_builder)
        item_to_plot = plotItemGenerator.get_example_plotItem(current_config)
        self.w_plotWidget.addItem(item_to_plot)


    def submit(self):
        '''Extract all parameters from widgets and update self.current_config'''
        self.result_config = {}
        self.result_config['display_name'] = self.textEdit_displaName.toPlainText()
        for i in range(len(self.config_builder)):
            name_config_param = self.list_config_key[i]
            type_config_param = self.config_builder[name_config_param]
            if type_config_param == 'color':
                self.result_config[name_config_param] = self.Qtcolor_to_list_rgb(self.dic_color_dialog[name_config_param].color())
            elif type_config_param == 'style':
                self.result_config[name_config_param] = self.dic_widget_config_param[name_config_param].currentText()
            elif type_config_param == 'spinInt':
                self.result_config[name_config_param] = self.dic_widget_config_param[name_config_param].value()
            elif type_config_param == 'checkBox':
                self.result_config[name_config_param] = self.dic_widget_config_param[name_config_param].checkState()
            elif type_config_param == 'dock':
                self.result_config[name_config_param] = self.dic_widget_config_param[name_config_param].currentText()
            elif type_config_param[:5] == 'spin_':
                self.result_config[name_config_param] = self.dic_widget_config_param[name_config_param].value()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_adaptativeConfig = QtWidgets.QDialog()
    ui = Ui_Dialog_adaptativeConfig()
    ui.setupUi(Dialog_adaptativeConfig)
    Dialog_adaptativeConfig.show()
    sys.exit(app.exec_())
