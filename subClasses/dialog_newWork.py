# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subClasses/dialog_newWork.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QFileDialog
import json, numpy as np, pandas as pd, shutil, datetime
from subClasses.dictWork import DictWork


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
        self.dateEdit_InitDate = QtWidgets.QDateTimeEdit(NewWork)
        self.dateEdit_InitDate.setGeometry(QtCore.QRect(130, 240, 111, 23))
        self.dateEdit_InitDate.setObjectName("dateEdit_InitDate")
        self.dateEdit_EndDate = QtWidgets.QDateTimeEdit(NewWork)
        self.dateEdit_EndDate.setGeometry(QtCore.QRect(130, 270, 111, 23))
        self.dateEdit_EndDate.setObjectName("dateEdit_EndDate")
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
        self.buttonBox.accepted.connect(self.submit)
        self.buttonBox.rejected.connect(NewWork.reject)
        QtCore.QMetaObject.connectSlotsByName(NewWork)
        
        # other variables
        self.pathFileToOpen = ''
        self.pathImportedDataFolder = 'imported_data/'
        self.pathJsonSumupImportedData = 'imported_data/imported_data_sumup.json'
        self.pathJsonClassificationData = 'imported_data/classification_data.json'
        self.pathWorkFolder = 'work/'

        # group variables (classification data)
        with open(self.pathJsonClassificationData,'r') as f:
            self.dic_ClassificationData = json.load(f)
            f.close()
        with open(self.pathJsonSumupImportedData,'r') as f:
            self.dic_SumupImportedData = json.load(f)
            f.close()

        # initialize 1st combo box
        list_assetType = [key for key in self.dic_ClassificationData.keys()]
        for i in range(len(self.dic_ClassificationData)):
            self.comboBox_assetType.addItem("")
            self.comboBox_assetType.setItemText(i, self._translate("NewWork", list_assetType[i]))

        # signals
        self.comboBox_assetType.currentTextChanged.connect(self.onAssetTypeChanged)
        self.comboBox_Broker.currentTextChanged.connect(self.onBrokerChanged)
        self.comboBox_File.currentTextChanged.connect(self.onFileSelected)

    def retranslateUi(self, NewWork):
        self._translate = QtCore.QCoreApplication.translate
        NewWork.setWindowTitle(self._translate("NewWork", "Dialog"))
        self.label.setText(self._translate("NewWork", "Enter New Work Name:"))
        self.label_3.setText(self._translate("NewWork", "Select Init Date:"))
        self.label_4.setText(self._translate("NewWork", "Select End Date:"))
        self.label_2.setText(self._translate("NewWork", "Select Asset Type:"))
        self.label_5.setText(self._translate("NewWork", "Select Broker:"))
        self.label_6.setText(self._translate("NewWork", "Select File:"))
        self.label_7.setText(self._translate("NewWork", "Data Description:"))
        self.label_8.setText(self._translate("NewWork", "Data 1st row preview:"))

    def onAssetTypeChanged(self):
        self.comboBox_Broker.clear()
        self.comboBox_File.clear()
        current_assetType = self.comboBox_assetType.currentText()
        list_available_broker = self.dic_ClassificationData[current_assetType]
        i = 0
        for broker_name in list_available_broker:
            self.comboBox_Broker.addItem("")
            self.comboBox_Broker.setItemText(i, self._translate("NewWork", broker_name))
            if i == 0:
                self.comboBox_Broker.setCurrentText(broker_name)
            i += 1

    def onBrokerChanged(self):
        self.comboBox_File.clear()
        current_assetType = self.comboBox_assetType.currentText()
        current_broker = self.comboBox_Broker.currentText()
        i = 0
        for data_name in self.dic_SumupImportedData.keys():
            if self.dic_SumupImportedData[data_name]['broker'] == current_broker and self.dic_SumupImportedData[data_name]['type_asset'] == current_assetType:
                self.comboBox_File.addItem("")
                self.comboBox_File.setItemText(i, self._translate("NewWork", data_name))
                if i == 0:
                    self.comboBox_File.setCurrentText(data_name)
                i += 1         


    def onFileSelected(self):
        # extract name and data relative to nae
        filename_dataToUse = self.comboBox_File.currentText()
        if filename_dataToUse != '':
            with open(self.pathJsonSumupImportedData,'r') as f:
                self.jsonSumupImportedData = json.load(f)[filename_dataToUse]
                f.close()
            initDate, endDate = self.jsonSumupImportedData["initDate"], self.jsonSumupImportedData["endDate"]
            initDateQ = QDateTime(datetime.datetime.strptime(initDate, "%Y-%m-%d %H:%M"))
            endDateQ = QDateTime(datetime.datetime.strptime(endDate, "%Y-%m-%d %H:%M"))
            # Set Dates max and min input boxes
            self.dateEdit_InitDate.setMinimumDateTime(initDateQ)
            self.dateEdit_InitDate.setMaximumDateTime(endDateQ)
            self.dateEdit_InitDate.setDateTime(initDateQ)
            self.dateEdit_EndDate.setMinimumDateTime(initDateQ)
            self.dateEdit_EndDate.setMaximumDateTime(endDateQ)
            self.dateEdit_EndDate.setDateTime(endDateQ)
            # Show preview 1st row
            self.path_src = self.pathImportedDataFolder + filename_dataToUse
            self.filename_dataToUse = filename_dataToUse
            self.pathFileToOpen = self.path_src
            self.df = pd.read_csv(self.path_src) 
            list_columns_str = [col for col in self.df]
            list_values_str = [str(self.df.iloc[0,i]) for i in range(len(self.df.columns))]
            # create the rows and columns
            self.tableWidget_rowPreview.clear()
            self.tableWidget_rowPreview.setColumnCount(len(self.df.columns))
            self.tableWidget_rowPreview.setRowCount(1)
            self.tableWidget_rowPreview.setHorizontalHeaderLabels(list_columns_str)
            for i in range(0,len(self.df.columns)):
                self.tableWidget_rowPreview.setItem(0,i, QtWidgets.QTableWidgetItem(list_values_str[i]))
            # Show description
            description = self.jsonSumupImportedData['description']
            self.textBrowser_description.setPlainText(description)
        
    def submit(self):
        '''Create the work template using the data we selected
        open df, create all the numpy of variables and put it in  folder with work name
        create the json file that identify the work (with all variables, and indicators, and
        if checkbox is checked by default for each)'''
        new_work_name = self.textEdit_InputNewWorkName.toPlainText().replace(' ','_')
        self.name_work = new_work_name
        path_dataToUse = self.pathFileToOpen
        filename_dataToUse = self.filename_dataToUse
        init_date = self.dateEdit_InitDate.dateTime().toPyDateTime().strftime(format='%Y-%m-%d %H:%M')
        end_date = self.dateEdit_EndDate.dateTime().toPyDateTime().strftime(format='%Y-%m-%d %H:%M')
        name_date_column = self.jsonSumupImportedData["name_date_column"]
        name_timestamp_column = self.jsonSumupImportedData["name_time_column"]
        format_date = self.jsonSumupImportedData["format_date"]
        type_data = self.jsonSumupImportedData["type_data"]
        df = pd.read_csv(path_dataToUse)
        # new work, its diction
        newWork = DictWork(new_work_name)
        newWork.create_work(df, name_date_column, name_timestamp_column, format_date, type_data, init_date, end_date, path_dataToUse)
        print('A new work have been initialised')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewWork = QtWidgets.QDialog()
    ui = Ui_NewWork()
    ui.setupUi(NewWork)
    NewWork.show()
    sys.exit(app.exec_())
