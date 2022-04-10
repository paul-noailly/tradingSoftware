# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'strategy_software_v2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from shutil import copyfile
import os, shutil

FOLDER_DATA = 'C:\\Users\\Paul\\Trading\\strategy_software\\imported_data\\'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1076, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuChart = QtWidgets.QMenu(self.menubar)
        self.menuChart.setObjectName("menuChart")
        self.menuAdd_Indicator = QtWidgets.QMenu(self.menubar)
        self.menuAdd_Indicator.setObjectName("menuAdd_Indicator")
        self.menuCreate_Indicator = QtWidgets.QMenu(self.menubar)
        self.menuCreate_Indicator.setObjectName("menuCreate_Indicator")
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
        self.menuFile.addAction(self.actionImport_New_Data)
        self.menuFile.addAction(self.actionOpen_Work)
        self.menuChart.addAction(self.actionPlot_Data)
        self.menuChart.addAction(self.actionUnplot_Data)
        self.menuChart.addAction(self.actionClear_Indicators)
        self.menuChart.addAction(self.actionSave_Work)
        self.menuStrategy.addAction(self.actionCreate_New_Strategy)
        self.menuStrategy.addAction(self.actionPlot_Strategy)
        self.menuStrategy.addAction(self.actionBacktest_Strategy)
        self.menuTrading_Accounts.addAction(self.actionAdd_New_Account)
        self.menuTrading_Accounts.addAction(self.actionShow_Accounts)
        self.menuTrading_Accounts.addAction(self.actionDeploy_Strategy)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuChart.menuAction())
        self.menubar.addAction(self.menuAdd_Indicator.menuAction())
        self.menubar.addAction(self.menuCreate_Indicator.menuAction())
        self.menubar.addAction(self.menuStrategy.menuAction())
        self.menubar.addAction(self.menuTrading_Accounts.menuAction())
        self.menubar.addAction(self.menuLabelling.menuAction())
        self.menubar.addAction(self.menuData_Science_Tools.menuAction())
        self.menubar.addAction(self.menuMachine_Learning.menuAction())
        self.menubar.addAction(self.menuDeep_Learning.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Menu - File
        self.actionImport_New_Data.triggered.connect(self.Import_New_Data)
        self.actionOpen_Work.triggered.connect(self.Open_Work)
        # Menu - Chart
        self.actionPlot_Data.triggered.connect(self.Plot_Data)
        self.actionSave_Work.triggered.connect(self.Save_Work)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuChart.setTitle(_translate("MainWindow", "Chart"))
        self.menuAdd_Indicator.setTitle(_translate("MainWindow", "Add Indicator"))
        self.menuCreate_Indicator.setTitle(_translate("MainWindow", "Create Indicator"))
        self.menuStrategy.setTitle(_translate("MainWindow", "Strategy"))
        self.menuTrading_Accounts.setTitle(_translate("MainWindow", "Trading Accounts"))
        self.menuLabelling.setTitle(_translate("MainWindow", "Labelling"))
        self.menuData_Science_Tools.setTitle(_translate("MainWindow", "Data Science Tools"))
        self.menuMachine_Learning.setTitle(_translate("MainWindow", "Machine Learning"))
        self.menuDeep_Learning.setTitle(_translate("MainWindow", "Deep Learning"))
        self.actionImport_New_Data.setText(_translate("MainWindow", "Import New Data"))
        self.actionPlot_Data.setText(_translate("MainWindow", "Plot Data"))
        self.actionUnplot_Data.setText(_translate("MainWindow", "Unplot Data"))
        self.actionClear_Indicators.setText(_translate("MainWindow", "Clear Indicators"))
        self.actionCreate_New_Strategy.setText(_translate("MainWindow", "Create New Strategy"))
        self.actionPlot_Strategy.setText(_translate("MainWindow", "Plot Strategy"))
        self.actionBacktest_Strategy.setText(_translate("MainWindow", "Backtest Strategy"))
        self.actionAdd_New_Account.setText(_translate("MainWindow", "Add New Account"))
        self.actionShow_Accounts.setText(_translate("MainWindow", "Show Accounts"))
        self.actionDeploy_Strategy.setText(_translate("MainWindow", "Deploy Strategy"))
        self.actionSave_Data.setText(_translate("MainWindow", "Save Data"))
        self.actionOpen_Work.setText(_translate("MainWindow", "Open Work"))
        self.actionSave_Work.setText(_translate("MainWindow", "Save Work"))
        
    # Menu - File - Import_New_Data
    def Import_New_Data(self):
        '''Open window to select csv file, then copy this file to the imported_data folder'''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "C:/Users/Paul/Trading/","All Files (*.csv);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        source = fileName
        target = FOLDER_DATA+source.split('/')[-1]
        shutil.copy(source, target)
        print('succesfully imported ',source.split('/')[-1])
        
    # Menu - File - Open_Work
    def Open_Work(self):
        '''Open previous work: data + indicators + strategies + ...'''
        pass
    
    # Menu - Chart - Plot_Data
    def Plot_Data(self):
        '''Use js package of tradingview to plot graphs'''
        
        pass
    
    # Menu - Chart - Save_Work
    def Save_Work(self):
        '''Save the work, which contain the data, additional indicators, ect..'''
        '''options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)'''
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())