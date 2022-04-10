# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'strategy_software_v2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialogButtonBox, QDialog, QVBoxLayout, QTabWidget, QColorDialog, QShortcut
from PyQt5.QtGui import QKeySequence
from shutil import copyfile
import os, shutil, pyqtgraph as pg, numpy as np, pandas as pd, time, json, datetime
from pyqtgraph import PlotWidget
from pyqtgraph.dockarea import DockArea, Dock
from functools import partial


# Own classes
from subClasses.dialog_importData import Ui_ImportData
from subClasses.dialog_newWork import Ui_NewWork
from subClasses.dictWork import DictWork
from subClasses.dialog_loadWork import Ui_Dialog_loadWork
from subClasses.dialog_addIndicator import Ui_Dialog_AddIndicator
from subClasses.indicatorGenerator import IndicatorGenerator
from subClasses.dialog_variable_config_standard import Ui_Dialog_ConfigVariableStandard
from subClasses.dialog_variable_config_ohlc import Ui_Dialog_ConfigVariableOHLC
from subClasses.dialog_adapativeConfig import Ui_Dialog_adaptativeConfig
from subClasses.plotItemGenerator import PlotItemGenerator


FOLDER_DATA = 'C:\\Users\\Paul\\Trading\\strategy_software\\imported_data\\'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1017)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # Dock Graph
        self.widget_DockGraphContainer = QtWidgets.QDockWidget(self.centralwidget)
        self.widget_DockGraphContainer.setGeometry(QtCore.QRect(160, 30, 1751, 881))
        self.widget_DockGraphContainer.setObjectName("widget_DockGraphContainer")
        # ToolBox
        # ToolBox - Layout
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 391, 27))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 3, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # ToolBox - Plot Data Button
        self.pushButton_plotData = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_plotData.setObjectName("pushButton_plotData")
        self.horizontalLayout.addWidget(self.pushButton_plotData)
        # ToolBox - Reset Variables Button
        self.pushButton_ResetVariables = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_ResetVariables.setObjectName("pushButton_ResetVariables")
        self.horizontalLayout.addWidget(self.pushButton_ResetVariables)
        # Toll Box - Add Data
        self.pushButton_addData = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_addData.setObjectName("pushButton_addData")
        self.horizontalLayout.addWidget(self.pushButton_addData)
        # ToolBox - Add Indicator Button        
        self.pushButton_AddIndicator = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_AddIndicator.setObjectName("pushButton_AddIndicator")
        self.horizontalLayout.addWidget(self.pushButton_AddIndicator)
        # ToolBox - Graph Config Button        
        self.pushButton_GraphConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GraphConfig.setGeometry(QtCore.QRect(1706, 4, 76, 23))
        self.pushButton_GraphConfig.setObjectName("pushButton_GraphConfig")
        # Tool Box chex box auto range
        self.checkBox_ToggleAutoRange = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ToggleAutoRange.setGeometry(QtCore.QRect(1789, 6, 111, 21))
        self.checkBox_ToggleAutoRange.setObjectName("checkBox_ToggleAutoRange")
        # Variables Selector
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 141, 881))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_checkBoxesVariables = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_checkBoxesVariables.setContentsMargins(0, 0, 0, 0)
        self.formLayout_checkBoxesVariables.setHorizontalSpacing(6)
        self.formLayout_checkBoxesVariables.setVerticalSpacing(0)
        self.formLayout_checkBoxesVariables.setObjectName("formLayout_checkBoxesVariables")
        self.icon_setting = QtGui.QIcon()
        self.icon_setting.addPixmap(QtGui.QPixmap("src/settings_black_18x18.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # Menu Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuChart = QtWidgets.QMenu(self.menubar)
        self.menuChart.setObjectName("menuChart")
        self.menuStrategy = QtWidgets.QMenu(self.menubar)
        self.menuStrategy.setObjectName("menuStrategy")
        self.menuTrading_Accounts = QtWidgets.QMenu(self.menubar)
        self.menuTrading_Accounts.setObjectName("menuTrading_Accounts")
        self.menuLabelling = QtWidgets.QMenu(self.menubar)
        self.menuLabelling.setObjectName("menuLabelling")
        self.menuData_Science_Tools = QtWidgets.QMenu(self.menubar)
        self.menuData_Science_Tools.setObjectName("menuData_Science_Tools")
        self.menuMachine_Learning = QtWidgets.QMenu(self.menubar)
        self.menuMachine_Learning.setObjectName("menuMachine_Learning")
        self.menuDeep_Learning = QtWidgets.QMenu(self.menubar)
        self.menuDeep_Learning.setObjectName("menuDeep_Learning")
        self.menuIndicator = QtWidgets.QMenu(self.menubar)
        self.menuIndicator.setObjectName("menuIndicator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_New_Data = QtWidgets.QAction(MainWindow)
        self.actionImport_New_Data.setObjectName("actionImport_New_Data")
        self.actionPlot_Data = QtWidgets.QAction(MainWindow)
        self.actionPlot_Data.setObjectName("actionPlot_Data")
        self.actionUnplot_Data = QtWidgets.QAction(MainWindow)
        self.actionUnplot_Data.setObjectName("actionUnplot_Data")
        self.actionClear_Indicators = QtWidgets.QAction(MainWindow)
        self.actionClear_Indicators.setObjectName("actionClear_Indicators")
        self.actionCreate_New_Strategy = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Strategy.setObjectName("actionCreate_New_Strategy")
        self.actionPlot_Strategy = QtWidgets.QAction(MainWindow)
        self.actionPlot_Strategy.setObjectName("actionPlot_Strategy")
        self.actionBacktest_Strategy = QtWidgets.QAction(MainWindow)
        self.actionBacktest_Strategy.setObjectName("actionBacktest_Strategy")
        self.actionAdd_New_Account = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Account.setObjectName("actionAdd_New_Account")
        self.actionShow_Accounts = QtWidgets.QAction(MainWindow)
        self.actionShow_Accounts.setObjectName("actionShow_Accounts")
        self.actionDeploy_Strategy = QtWidgets.QAction(MainWindow)
        self.actionDeploy_Strategy.setObjectName("actionDeploy_Strategy")
        self.actionSave_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Data.setObjectName("actionSave_Data")
        self.actionOpen_Work = QtWidgets.QAction(MainWindow)
        self.actionOpen_Work.setObjectName("actionOpen_Work")
        self.actionSave_Work = QtWidgets.QAction(MainWindow)
        self.actionSave_Work.setObjectName("actionSave_Work")
        self.actionCreate_New_Work = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Work.setObjectName("actionCreate_New_Work")
        self.actionSave_Work_as = QtWidgets.QAction(MainWindow)
        self.actionSave_Work_as.setObjectName("actionSave_Work_as")
        self.actionLoad_Work = QtWidgets.QAction(MainWindow)
        self.actionLoad_Work.setObjectName("actionLoad_Work")
        self.actionCreate_Indicator = QtWidgets.QAction(MainWindow)
        self.actionCreate_Indicator.setObjectName("actionCreate_Indicator")
        self.menuFile.addAction(self.actionImport_New_Data)
        self.menuChart.addAction(self.actionCreate_New_Work)
        self.menuChart.addAction(self.actionLoad_Work)
        self.menuChart.addAction(self.actionSave_Work)
        self.menuChart.addAction(self.actionSave_Work_as)
        self.menuStrategy.addAction(self.actionCreate_New_Strategy)
        self.menuStrategy.addAction(self.actionPlot_Strategy)
        self.menuStrategy.addAction(self.actionBacktest_Strategy)
        self.menuTrading_Accounts.addAction(self.actionAdd_New_Account)
        self.menuTrading_Accounts.addAction(self.actionShow_Accounts)
        self.menuTrading_Accounts.addAction(self.actionDeploy_Strategy)
        self.menuIndicator.addAction(self.actionCreate_Indicator)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuChart.menuAction())
        self.menubar.addAction(self.menuIndicator.menuAction())
        self.menubar.addAction(self.menuStrategy.menuAction())
        self.menubar.addAction(self.menuTrading_Accounts.menuAction())
        self.menubar.addAction(self.menuLabelling.menuAction())
        self.menubar.addAction(self.menuData_Science_Tools.menuAction())
        self.menubar.addAction(self.menuMachine_Learning.menuAction())
        self.menubar.addAction(self.menuDeep_Learning.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Graph widget        
        area = DockArea()
        self.widget_DockGraphContainer.setWidget(area)
        self.TopDock = Dock("Main Price Window", size=(500,200))
        self.BottomDock = Dock("Main Oscillator Window", size=(500,50))
        area.addDock(self.TopDock, 'right')     ## place d4 at right edge of dock area
        area.addDock(self.BottomDock, 'bottom', self.TopDock)
        
        #graph Initiate Graphs Windows
        self.w_mainGraph = pg.PlotWidget(axisItems = {'bottom': pg.DateAxisItem()}) #(title="Dock 4 plot")
        self.w_mainGraph.setBackground('w')
        self.w_mainGraph.showGrid(x=True, y=True)
        self.w_osciGraph = pg.PlotWidget(axisItems = {'bottom': pg.DateAxisItem()})  #(title="Dock 6 plot")
        self.w_osciGraph.setBackground('w')
        self.w_osciGraph.showGrid(x=True, y=True)
        self.w_mainGraph.setXLink(self.w_osciGraph)
        self.TopDock.addWidget(self.w_mainGraph)
        self.BottomDock.addWidget(self.w_osciGraph)
        


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Menu - File
        self.actionImport_New_Data.triggered.connect(self.function_Import_New_Data)
        # Menu - Work
        self.actionCreate_New_Work.triggered.connect(self.function_Create_New_Work)
        self.actionLoad_Work.triggered.connect(self.function_select_Work)
        self.actionSave_Work.triggered.connect(self.function_Save_Work)
        self.actionSave_Work_as.triggered.connect(self.function_Save_Work_as)
        # Menu - Indicator
        self.actionCreate_Indicator.triggered.connect(self.function_Create_Indicator)
        # Menu - Strategy
        self.actionCreate_New_Strategy.triggered.connect(self.function_Create_New_Strategy)
        self.actionPlot_Strategy.triggered.connect(self.function_Plot_Strategy)
        self.actionBacktest_Strategy.triggered.connect(self.function_Backtest_Strategy)
        # Menu - Accounts
        self.actionAdd_New_Account.triggered.connect(self.function_Add_New_Account)
        self.actionShow_Accounts.triggered.connect(self.function_Show_Accounts)
        self.actionDeploy_Strategy.triggered.connect(self.function_Deploy_Strategy)
        # toolBox buttons
        self.pushButton_plotData.clicked.connect(self.function_plotData)
        self.pushButton_ResetVariables.clicked.connect(self.function_ResetVariables)
        self.pushButton_addData.clicked.connect(self.function_AddData)
        self.pushButton_AddIndicator.clicked.connect(self.function_AddIndicator)
        # Graph config button
        self.pushButton_GraphConfig.clicked.connect(self.function_GraphConfig)
        self.checkBox_ToggleAutoRange.stateChanged.connect(self.function_ToggleAutoRange)
        # shortcut
        self.shortcut = QShortcut(QKeySequence("Ctrl+S"), self.centralwidget)
        self.shortcut.activated.connect(self.function_Save_Work)
        
        
        # Other variables
        self.pathFolderWork = 'work/'
        self.dic_form_layout_variable = {}
        # doictionary of pointeurs for docks
        self.dic_dock_pointers = {'main':self.w_mainGraph, 'osci':self.w_osciGraph}
        self.debug_index = 0
        

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "MainWindow"))
        # Tool Box Buttons
        self.pushButton_plotData.setText(self._translate("MainWindow", "Plot Data"))
        self.pushButton_ResetVariables.setText(self._translate("MainWindow", "Reset Variables"))
        self.pushButton_addData.setText(self._translate("MainWindow", "Add Data"))
        self.pushButton_AddIndicator.setText(self._translate("MainWindow", "Add Indicator"))
        self.pushButton_GraphConfig.setText(self._translate("MainWindow", "Graph Config"))
        self.checkBox_ToggleAutoRange.setText(self._translate("MainWindow", "Toggle Auto Range"))
        # Menu Bar
        self.menuFile.setTitle(self._translate("MainWindow", "File"))
        self.menuChart.setTitle(self._translate("MainWindow", "Work"))
        self.menuStrategy.setTitle(self._translate("MainWindow", "Strategy"))
        self.menuTrading_Accounts.setTitle(self._translate("MainWindow", "Trading Accounts"))
        self.menuLabelling.setTitle(self._translate("MainWindow", "Labelling"))
        self.menuData_Science_Tools.setTitle(self._translate("MainWindow", "Data Science Tools"))
        self.menuMachine_Learning.setTitle(self._translate("MainWindow", "Machine Learning"))
        self.menuDeep_Learning.setTitle(self._translate("MainWindow", "Deep Learning"))
        self.menuIndicator.setTitle(self._translate("MainWindow", "Indicator"))
        self.actionImport_New_Data.setText(self._translate("MainWindow", "Import New Data"))
        self.actionPlot_Data.setText(self._translate("MainWindow", "Plot Data"))
        self.actionUnplot_Data.setText(self._translate("MainWindow", "Unplot Data"))
        self.actionClear_Indicators.setText(self._translate("MainWindow", "Clear Indicators"))
        self.actionCreate_New_Strategy.setText(self._translate("MainWindow", "Create New Strategy"))
        self.actionPlot_Strategy.setText(self._translate("MainWindow", "Plot Strategy"))
        self.actionBacktest_Strategy.setText(self._translate("MainWindow", "Backtest Strategy"))
        self.actionAdd_New_Account.setText(self._translate("MainWindow", "Add New Account"))
        self.actionShow_Accounts.setText(self._translate("MainWindow", "Show Accounts"))
        self.actionDeploy_Strategy.setText(self._translate("MainWindow", "Deploy Strategy"))
        self.actionSave_Data.setText(self._translate("MainWindow", "Save Data"))
        self.actionOpen_Work.setText(self._translate("MainWindow", "Open Work"))
        self.actionSave_Work.setText(self._translate("MainWindow", "Save Work"))
        self.actionCreate_New_Work.setText(self._translate("MainWindow", "Create New Work"))
        self.actionSave_Work_as.setText(self._translate("MainWindow", "Save Work as"))
        self.actionLoad_Work.setText(self._translate("MainWindow", "Load Work"))
        self.actionCreate_Indicator.setText(self._translate("MainWindow", "Create Indicator"))
        
    # Menu File functions
    def function_Import_New_Data(self):
        '''When clicked, show a popup box, in wich there is one button to select a file, one dialog item to select type 
        of data, and one submit button.
        When submit is clicket, it copies the slected file to imported data folder, then it register it in a json, 
        with the type of data in it consists on (tick or ohlc)'''
        # Create Popup
        dialog = QtWidgets.QDialog()
        ui = Ui_ImportData()
        ui.setupUi(dialog)
        dialog.show()
        rsp = dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            print('data should have been imported succesfully')
        else:
            print('dialog for import data have been closed')
        print('action Import_New_Data has been done')

    def function_Create_New_Work(self):
        '''When clicked, show a popup box, in wich there is one button to select a file, one dialog item to select type 
        of data, and one submit button.
        When submit is clicket, it copies the slected file to imported data folder, then it register it in a json, 
        with the type of data in it consists on (tick or ohlc)'''
        # Create Popup
        dialog = QtWidgets.QDialog()
        ui = Ui_NewWork()
        ui.setupUi(dialog)
        dialog.show()
        rsp = dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            name_work = ui.name_work
            self.load_work(name_work)
            #print('data should have been imported succesfully')
        else:
            print('dialog for import data have been closed')
        print('action Create_New_Work has been done')

    def function_select_Work(self):
        list_work = [file for file in os.listdir(self.pathFolderWork) if file[-5:]=='.json']
        dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_loadWork()
        ui.setupUi(dialog, list_work)
        dialog.show()
        rsp = dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            self.current_name_work = ui.selected_work
        self.load_work(self.current_name_work)
        
    def load_work(self, name_work):
        '''Using the work name, it will import all the npy files constructed,
        plot the variables to plot (using the boolean plot in each variable key of the work.json file)
        it will plot it in the corresponding dock ()
        Then it will show the check boxes and config button on the left, for each varialbes.
        The ones that should be plotted will have a checked check box'''
        self.current_name_work = name_work
        print('we are about to load name_file.json = ',self.current_name_work+'.json')
        with open(self.pathFolderWork+self.current_name_work+'.json', 'r') as f:
            self.dict_current_work_sumup = json.load(f)
            f.close()
        for name_var in self.dict_current_work_sumup['variables'].keys():
            self.add_variable_to_form_layout(name_var)
        self.refresh_variables_layout()
        self.function_plotData()
        
            
    def add_variable_to_form_layout(self, name_var, doRefresh=False):
        '''Given a variable name, add 2 widget to the form layout, on check box with the name var, and one config button
        It saves it into the dic_form_layout_variable and then apply a refresh onto the form layout'''
        nbs_row = self.formLayout_checkBoxesVariables.rowCount()
        self.dic_form_layout_variable[name_var] = {'checkBoxWidget': QtWidgets.QCheckBox(self.formLayoutWidget), 'configButtonWidget': QtWidgets.QToolButton(self.formLayoutWidget), 
                                                    'configDialog':QtWidgets.QDialog() ,
                                                   'row':len(self.dic_form_layout_variable.keys()),
                                                   'showed':False}
        if doRefresh:
            self.refresh_variables_layout()
        
    def refresh_variables_layout(self):
        # reset
        '''Using the dictionnary dic_form_layout_variable we show the check boxes and the config button'''
        for name_var in self.dic_form_layout_variable.keys():
            # implement check box
            if not self.dic_form_layout_variable[name_var]['showed']:
                self.dic_form_layout_variable[name_var]['checkBoxWidget'].setObjectName(name_var+"CheckBox")
                self.formLayout_checkBoxesVariables.setWidget(self.dic_form_layout_variable[name_var]['row'], QtWidgets.QFormLayout.LabelRole, self.dic_form_layout_variable[name_var]['checkBoxWidget'])
                self.dic_form_layout_variable[name_var]['checkBoxWidget'].setText(self._translate("MainWindow", self.dict_current_work_sumup['variables'][name_var]['config']['display_name']))
                self.dic_form_layout_variable[name_var]['checkBoxWidget'].setCheckState(self.dict_current_work_sumup['variables'][name_var]['plot'])
                self.dic_form_layout_variable[name_var]['checkBoxWidget'].stateChanged.connect(partial(self.onSignal_configVariableCheckBoxChecked, name_var))
                # implement config button
                self.dic_form_layout_variable[name_var]['configButtonWidget'].setIcon(self.icon_setting)
                self.dic_form_layout_variable[name_var]['configButtonWidget'].setObjectName(name_var+"Config")
                self.formLayout_checkBoxesVariables.setWidget(self.dic_form_layout_variable[name_var]['row'], QtWidgets.QFormLayout.FieldRole, self.dic_form_layout_variable[name_var]['configButtonWidget'])
                self.dic_form_layout_variable[name_var]['configButtonWidget'].setText(self._translate("MainWindow", "..."))
                self.dic_form_layout_variable[name_var]['configButtonWidget'].clicked.connect(partial(self.open_dialogConfigVariable, name_var))
                # update showed
                self.dic_form_layout_variable[name_var]['showed'] = True

    def onSignal_configVariableCheckBoxChecked(self, name_var):
        if not self.dict_current_work_sumup['variables'][name_var]['plot']: # if plot=False
            self.dic_form_layout_variable[name_var]['checkBoxWidget'].setCheckState(1)
            self.dict_current_work_sumup['variables'][name_var]['plot'] = True
        else:
            self.dic_form_layout_variable[name_var]['checkBoxWidget'].setCheckState(0)
            self.dict_current_work_sumup['variables'][name_var]['plot'] = False
            
    def open_dialogConfigVariable(self, name_var):
        '''Open an adaptative dialog that we be built based on the config builder'''
        # get ui inputs
        config_builder = self.dict_current_work_sumup['variables'][name_var]['config_builder']
        current_config = self.dict_current_work_sumup['variables'][name_var]['config']
        default_config = self.dict_current_work_sumup['variables'][name_var]['default_config']
        dic_dock = self.dict_current_work_sumup['list_docks']
        plot_builder = self.dict_current_work_sumup['variables'][name_var]['plot_builder']
        # Create Popup
        dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_adaptativeConfig()
        ui.setupUi(dialog, config_builder, current_config, default_config, dic_dock, plot_builder)
        dialog.show()
        rsp = dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            self.dict_current_work_sumup['variables'][name_var]['config'] = ui.result_config

    def function_Save_Work(self):
        with open(self.pathFolderWork+self.current_name_work+'.json', 'w') as f:
            json.dump(self.dict_current_work_sumup, f)
            f.close()
        print('action Save_Work has been done')

    def function_Save_Work_as(self):
        # Open save dialog
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None,"QFileDialog.getSaveFileName()","","All Files (*.json)", options=options)
        # add json extension if needed
        if fileName[-5:]!='.json':
            fileName = fileName+'.json'
        if self.current_name_work != fileName.split('/')[-1].split('.')[0]: # Si on veut creer un nouveau file
            # copy json sumup
            self.current_name_work = fileName.split('/')[-1].split('.')[0]
            previous_path_folder_work_files = self.dict_current_work_sumup['path_folder_work_files'][:-1] # on retire le / de fin
            new_path_folder_work_files = self.pathFolderWork + self.current_name_work
            self.dict_current_work_sumup['path_folder_work_files'] = new_path_folder_work_files + '/'
            with open(fileName,'w') as f:            
                json.dump(self.dict_current_work_sumup, f)
                f.close()
            shutil.copytree(previous_path_folder_work_files,new_path_folder_work_files)
        else:
            self.function_Save_Work()
            # copy folder numpy
        print('action Save_Work_as has been done')
        
    def function_Create_Indicator(self):
        '''Create a new indicator via a dialog. Find a way to store all created indicator
        Find a way to register the indicator formula. Select nuber of output & input, name of input & conditions.
        Register a dict for the template of the config dialog (in wich there is parameters, pen config (color, fill?, width,..))
        A king of indidicator that will be abble to create is an ohlc object from a tick data object
        '''
        print('action Create_Indicator has been done')

    def function_Create_New_Strategy(self):
        print('action Create_New_Strategy has been done')

    def function_Plot_Strategy(self):
        print('action Plot_Strategy has been done')

    def function_Backtest_Strategy(self):
        print('action Backtest_Strategy has been done')

    def function_Add_New_Account(self):
        print('action Add_New_Account has been done')

    def function_Show_Accounts(self):
        print('action Show_Accounts has been done')

    def function_Deploy_Strategy(self):
        print('action Deploy_Strategy has been done') 

    def debug(self, additional_info=''):
        pass
        
    # Tool Box Functions
    def function_plotData(self):
        for plotWidget_name in self.dic_dock_pointers.keys():
            self.dic_dock_pointers[plotWidget_name].clear()
        '''Use the current work dic to plot the data using the current work'''
        path_work_files = self.dict_current_work_sumup['path_folder_work_files']
        # initialize crosshair
        self.dic_crosshair = {}
        for dock in self.dic_dock_pointers.keys():
            self.dic_crosshair[dock] = {'vLine':pg.InfiniteLine(angle=90, movable=False), 
                                   'hLine':pg.InfiniteLine(angle=0, movable=False), 
                                   'vb': self.dic_dock_pointers[dock].getViewBox(),
                                   'data':{},
                                   'time':[],
                                   'label':pg.LabelItem(justify='right')}
        for name_var in self.dict_current_work_sumup['variables'].keys():
            #self.dict_current_work_sumup['variables'][name_var]['plot'] = self.dic_form_layout_variable[name_var]['checkBoxWidget'].checkState()
            if self.dict_current_work_sumup['variables'][name_var]['plot']:
                # get item to plot
                config = self.dict_current_work_sumup['variables'][name_var]['config']
                plot_builder = self.dict_current_work_sumup['variables'][name_var]['plot_builder']
                dock = config['dock']
                dic_path_values = self.dict_current_work_sumup['variables'][name_var]['path_value_dic']
                dic_values = {key : np.load(path_work_files+dic_path_values[key], allow_pickle=True) for key in dic_path_values.keys()}
                arr_time = np.load(path_work_files + self.dict_current_work_sumup['variables'][name_var]['path_time_np'], allow_pickle=True)
                plotItemGenerator = PlotItemGenerator(config, plot_builder, dic_values, arr_time)
                item_to_plot = plotItemGenerator.get_plotItem()
                # add item to graph
                self.dic_dock_pointers[dock].addItem(item_to_plot)
                # add data to crosshair
                self.dic_crosshair[dock]['time'] = arr_time
                for key in dic_values.keys():
                    self.dic_crosshair[dock]['data'][key] = dic_values[key]
                #self.dic_crosshair[dock]['vb'] = item_to_plot.vb

        def mouseMoved(self,dock,evt):
            dic_dock_crosshair = self.dic_crosshair[dock]
            vb = dic_dock_crosshair['vb']
            pos = evt
            arr_time = dic_dock_crosshair['time']
            if self.dic_dock_pointers[dock].sceneBoundingRect().contains(pos):
                mousePoint = vb.mapSceneToView(pos)
                index = int(mousePoint.x())
                if index > 0 and index < len(arr_time):
                    txt = "time={}".format(datetime.datetime.fromtimestamp(arr_time[index]))
                    for key in dic_dock_crosshair['data'].keys():
                        txt += ' {}={}'.format(key,dic_dock_crosshair['data'][key][index])
                    self.dic_crosshair[dock]['label'].setText(txt)
                dic_dock_crosshair['vLine'].setPos(mousePoint.x())
                dic_dock_crosshair['hLine'].setPos(mousePoint.y())
        for dock in self.dic_dock_pointers.keys():
            self.dic_dock_pointers[dock].addItem(self.dic_crosshair[dock]['vLine'], ignoreBounds=True)
            self.dic_dock_pointers[dock].addItem(self.dic_crosshair[dock]['hLine'], ignoreBounds=True)
            self.dic_dock_pointers[dock].addItem(self.dic_crosshair[dock]['label'])
            #proxy = pg.SignalProxy(self.dic_dock_pointers[dock].scene().sigMouseMoved, rateLimit=60, slot=partial(mouseMoved, self, dock))
            self.dic_dock_pointers[dock].scene().sigMouseMoved.connect(partial(mouseMoved, self, dock))
        print('action plotData has been done')

    def function_ResetVariables(self):
        print('action ResetVariables has been done')

    def function_AddData(self):
        '''Add Data to the variables'''
        pass

    def function_AddIndicator(self):
        '''1 show a dialog to add indicator'''
        dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_AddIndicator()
        ui.setupUi(dialog, self.dict_current_work_sumup)
        dialog.show()
        rsp = dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            params = ui.params
            inputs_name = ui.inputs_name
            selected_indicator = ui.selected_indicator
            indicator_name_var = ui.indicator_name_var
        indicatorGenerator = IndicatorGenerator(selected_indicator)
        self.dict_current_work_sumup = indicatorGenerator.build_indicator(indicator_name_var, selected_indicator, inputs_name, params, self.dict_current_work_sumup)
        self.add_variable_to_form_layout(indicator_name_var, doRefresh=True)
        print('action AddIndicator has been done')

    def function_GraphConfig(self):
        '''Allows user to edit background and foreground of a graph in a dialog, need to specify wich dock to apply change to (or all docks)'''
        print('action GraphConfig has been done')

    def function_ToggleAutoRange(self):
        '''Change the auto range param for all graphs'''
        if self.checkBox_ToggleAutoRange.checkState() == 2:
            print('enabling auto range')
            for dock_key in self.dic_dock_pointers.keys():
                self.dic_dock_pointers[dock_key].enableAutoRange()
        else:
            print('disbling autorange')
            for dock_key in self.dic_dock_pointers.keys():
                self.dic_dock_pointers[dock_key].disableAutoRange()


        
    # Additional function



        

    
    # Menu - Chart - Plot_Data
    def Plot_Data(self):
        '''create a layout for main graph and a layout for data to plot
        1 Data Processing
         1.1: call an open file that will look into directory of imported data. fixe variable path_data = ...
         1.2: when selected, open the csv with pandas and check if we have time stamps, what are the variables ect.
         1.3: Store this data in a new folder (work) as a json+csv file. named by the date
         1.4: in the json plot the config for future work importing (like selected variables)
         1.5: in the csv, the new csv that will be modified when we add/delete indicator or data
        2 layout data
         2.1 Create the layout for data variables on the left
         2.2 for each variable (outside of timestamp) show a check box. default check only the 1st (mideprice)
         2.3 next to the check box, put a label for the variable name (columns name)
         2.4 next to the label, put a config button
         2.5 when clicked the config button open a popup with 3 selectable param and one submit button
         2.6 3 param: timeframe (source, 1sec, 1min, ...), the graph window on which to plot (with possibility to add new one), 
         and the type of value to plot (exact value, %change from 1st, %change from previous, zscored value,..)
         2.7 when submit is clicked, adjust json file, calculate new array and plot again
        3 graph layout
         3.1 Initialise 1 main layout, and plot raw price in it
         3.2 build fonction to add new layout (via tab widget, dock widget, ... )
         3.3 build fonctions to plot the ohlc
        '''
        # 1.1 when clicked, open file in the imported csv directory
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "C:/Users/Paul/Trading/strategy_software/imported_data/",
                                                  "All Files (*.csv);;Python Files (*.py)", options=options)
        if fileName:
            print('found file ', fileName)
        path_imported_data = fileName
        # 1.2 open data and do checking
        imported_data = pd.read_csv(path_imported_data)
        self.create_plot(imported_data)
        
    def create_plot(self, imported_data):
        ''' Use the imported data dtaframe to plot the dat'''
        for time_name_columns in ['timestamp','Timestamp']:
            if time_name_columns in imported_data.columns:
                break
        #print('name of the time columns is: ',time_name_columns)
        for price_name_columns in ['close','MidPrice','price','Price','midprice','mp','Midprice']:
            if price_name_columns in imported_data.columns:
                break
        #print('name of the price columns is: ',price_name_columns)
        # 1.3 extract arrays and store in a json =+df file for the work_save
        array_timestamp = imported_data[time_name_columns].to_numpy()
        array_price = imported_data[price_name_columns].to_numpy()
        
        # 3.1 Initialise 1 layout and plot price in it
        # Graph widget
        self.w_mainGraph = pg.PlotWidget(axisItems = {'bottom': pg.DateAxisItem()}) #(title="Dock 4 plot")
        self.w_mainGraph.setBackground('w')
        self.w_mainGraph.showGrid(x=True, y=True)
        self.w_mainGraph.setXRange(array_timestamp[0],array_timestamp[-1])
        self.w_mainGraph.plot(array_timestamp,array_price)
        self.w_osciGraph = pg.PlotWidget(axisItems = {'bottom': pg.DateAxisItem()})  #(title="Dock 6 plot")
        self.w_mainGraph.setBackground('w')
        self.w_osciGraph.showGrid(x=True, y=True)
        self.w_osciGraph.setXRange(array_timestamp[0],array_timestamp[-1])
        self.w_osciGraph.plot(array_timestamp,np.ones(len(array_timestamp)))
        self.w_mainGraph.setXLink(self.w_osciGraph)
        
        self.TopDock.addWidget(self.w_mainGraph)
        self.BottomDock.addWidget(self.w_osciGraph)
        #print('price have been plotted')
        

        
        #print('\n----')

    # Menu - Chart - Save_Work
    def Save_Work(self):
        '''Save the work, which contain the data, additional indicators, ect..'''
        '''options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
        #print(fileName)'''
        pass


if __name__ == "__main__":
    print('-----------------------------App is Launched------------------------------')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.activateWindow()
    #MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.WindowStaysOnTopHint) # allow the window to show on top of all other app on windows 10
    MainWindow.showMaximized() #show main window with maximal size
    sys.exit(app.exec_())
