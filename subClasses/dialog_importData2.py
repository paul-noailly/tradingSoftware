# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_importData.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog
from subClasses.dialog_importData_TickDataPriceNamesDict import Ui_Dialog_TickDataPriceNamesDict
from subClasses.dialog_importData_OHLCPriceNamesDict import Ui_Dialog_OHLCPriceNamesDict
import os, shutil, pandas as pd, numpy as np, datetime, json


class Ui_ImportData(object):
    def setupUi(self, ImportData):
        ImportData.setObjectName("ImportData")
        ImportData.resize(770, 374)
        # button box
        self.buttonBox = QtWidgets.QDialogButtonBox(ImportData)
        self.buttonBox.setGeometry(QtCore.QRect(240, 330, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        # Select file
        self.label = QtWidgets.QLabel(ImportData)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label.setObjectName("label")
        self.textBrowser_OpenFile = QtWidgets.QTextBrowser(ImportData)
        self.textBrowser_OpenFile.setGeometry(QtCore.QRect(160, 5, 141, 23))
        self.textBrowser_OpenFile.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_OpenFile.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_OpenFile.setObjectName("textBrowser_OpenFile")
        self.toolButton_OpenFile = QtWidgets.QToolButton(ImportData)
        self.toolButton_OpenFile.setGeometry(QtCore.QRect(300, 4, 31, 25))
        self.toolButton_OpenFile.setObjectName("toolButton_OpenFile")
        # Show Preview
        self.tableWidget__dfPreview = QtWidgets.QTableWidget(ImportData)
        self.tableWidget__dfPreview.setGeometry(QtCore.QRect(390, 30, 361, 41))
        self.tableWidget__dfPreview.setObjectName("tableWidget__dfPreview")
        self.tableWidget__dfPreview.setColumnCount(0)
        self.tableWidget__dfPreview.setRowCount(0)
        self.pushButton_show1strow = QtWidgets.QPushButton(ImportData)
        self.pushButton_show1strow.setGeometry(QtCore.QRect(530, 10, 81, 23))
        self.pushButton_show1strow.setObjectName("pushButton_show1strow")
        # Data Type
        self.label_2 = QtWidgets.QLabel(ImportData)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_DataType = QtWidgets.QComboBox(ImportData)
        self.comboBox_DataType.setGeometry(QtCore.QRect(160, 35, 141, 23))
        self.comboBox_DataType.setObjectName("comboBox_DataType")
        self.comboBox_DataType.addItem("")
        self.comboBox_DataType.addItem("")
        # date column name
        self.label_3 = QtWidgets.QLabel(ImportData)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_nameDateColumn = QtWidgets.QComboBox(ImportData)
        self.comboBox_nameDateColumn.setGeometry(QtCore.QRect(160, 65, 141, 22))
        self.comboBox_nameDateColumn.setObjectName("comboBox_nameDateColumn")
        # timestamp name
        self.label_4 = QtWidgets.QLabel(ImportData)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 141, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_nameTimestamp = QtWidgets.QComboBox(ImportData)
        self.comboBox_nameTimestamp.setGeometry(QtCore.QRect(160, 95, 141, 22))
        self.comboBox_nameTimestamp.setObjectName("comboBox_nameTimestamp")
        self.comboBox_nameTimestamp.addItem("")
        self.textEdit_nameTimeStamp = QtWidgets.QTextEdit(ImportData)
        self.textEdit_nameTimeStamp.setGeometry(QtCore.QRect(310, 95, 131, 23))
        self.textEdit_nameTimeStamp.setObjectName("textEdit_nameTimeStamp")
        # dateformat
        self.label_6 = QtWidgets.QLabel(ImportData)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit_dateFormat = QtWidgets.QTextEdit(ImportData)
        self.textEdit_dateFormat.setGeometry(QtCore.QRect(160, 125, 141, 23))
        self.textEdit_dateFormat.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_dateFormat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_dateFormat.setObjectName("textEdit_dateFormat")
        self.label_datefromatinfo = QtWidgets.QLabel(ImportData)
        self.label_datefromatinfo.setGeometry(QtCore.QRect(310, 130, 211, 16))
        self.label_datefromatinfo.setObjectName("label_datefromatinfo")
        # Enter description data
        self.label_10 = QtWidgets.QLabel(ImportData)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 131, 16))
        self.label_10.setObjectName("label_10")
        self.textEdit = QtWidgets.QTextEdit(ImportData)
        self.textEdit.setGeometry(QtCore.QRect(160, 160, 281, 51))
        self.textEdit.setObjectName("textEdit")
        #select classification
        self.groupBox_selectclassification = QtWidgets.QGroupBox(ImportData)
        self.groupBox_selectclassification.setGeometry(QtCore.QRect(10, 220, 281, 80))
        self.groupBox_selectclassification.setObjectName("groupBox_selectclassification")
        self.comboBox_typeAsset = QtWidgets.QComboBox(self.groupBox_selectclassification)
        self.comboBox_typeAsset.setGeometry(QtCore.QRect(160, 20, 111, 23))
        self.comboBox_typeAsset.setObjectName("comboBox_typeAsset")
        self.label_8 = QtWidgets.QLabel(self.groupBox_selectclassification)
        self.label_8.setGeometry(QtCore.QRect(10, 55, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.groupBox_selectclassification)
        self.label_5.setGeometry(QtCore.QRect(10, 25, 111, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_broker = QtWidgets.QComboBox(self.groupBox_selectclassification)
        self.comboBox_broker.setGeometry(QtCore.QRect(160, 50, 111, 23))
        self.comboBox_broker.setObjectName("comboBox_broker")
        # create classification
        self.groupBox_addNewClassification = QtWidgets.QGroupBox(ImportData)
        self.groupBox_addNewClassification.setGeometry(QtCore.QRect(300, 220, 331, 80))
        self.groupBox_addNewClassification.setObjectName("groupBox_addNewClassification")
        self.label_9 = QtWidgets.QLabel(self.groupBox_addNewClassification)
        self.label_9.setGeometry(QtCore.QRect(10, 55, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.groupBox_addNewClassification)
        self.label_7.setGeometry(QtCore.QRect(10, 25, 111, 16))
        self.label_7.setObjectName("label_7")
        self.textEdit_assetType = QtWidgets.QTextEdit(self.groupBox_addNewClassification)
        self.textEdit_assetType.setGeometry(QtCore.QRect(150, 20, 111, 23))
        self.textEdit_assetType.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_assetType.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_assetType.setObjectName("textEdit_assetType")
        self.textEdit_NewBroker = QtWidgets.QTextEdit(self.groupBox_addNewClassification)
        self.textEdit_NewBroker.setGeometry(QtCore.QRect(150, 50, 111, 23))
        self.textEdit_NewBroker.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_NewBroker.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_NewBroker.setObjectName("textEdit_NewBroker")
        self.pushButton_submitAssetType = QtWidgets.QPushButton(self.groupBox_addNewClassification)
        self.pushButton_submitAssetType.setGeometry(QtCore.QRect(270, 20, 51, 23))
        self.pushButton_submitAssetType.setObjectName("pushButton_submitAssetType")
        self.pushButton_submitnewBroker = QtWidgets.QPushButton(self.groupBox_addNewClassification)
        self.pushButton_submitnewBroker.setGeometry(QtCore.QRect(270, 50, 51, 23))
        self.pushButton_submitnewBroker.setObjectName("pushButton_submitnewBroker")


        self.retranslateUi(ImportData)
        self.buttonBox.accepted.connect(ImportData.accept)
        self.buttonBox.accepted.connect(self.submit_importedData)
        self.buttonBox.rejected.connect(ImportData.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportData)

        # class variables
        self.data_have_been_imported = False
        self.path_imported_data_sumup_json = 'imported_data/imported_data_sumup.json'
        self.path_classification_data_json = 'imported_data/classification_data.json'
        self.path_target_folder = 'imported_data/'

        # Buttons connexion
        self.toolButton_OpenFile.clicked.connect(self.submit_importedData)
        self.pushButton_show1strow.clicked.connect(self.function_showPreview)
        self.pushButton_submitnewBroker.clicked.connect(self.function_submitNewBroker)
        self.pushButton_submitAssetType.clicked.connect(self.function_submitNewAssetType)

        # signal trigger
        self.comboBox_nameTimestamp.currentTextChanged.connect(self.onSelectCreateNewTimestamp)

        # combo boxes initialisations

    def retranslateUi(self, ImportData):
        _translate = QtCore.QCoreApplication.translate
        ImportData.setWindowTitle(_translate("ImportData", "Dialog"))
        self.comboBox_DataType.setItemText(0, _translate("ImportData", "tick data"))
        self.comboBox_DataType.setItemText(1, _translate("ImportData", "fixed data"))
        self.label.setText(_translate("ImportData", "Select the data to import: "))
        self.toolButton_OpenFile.setText(_translate("ImportData", "..."))
        self.label_2.setText(_translate("ImportData", "Select type of data:"))
        self.label_3.setText(_translate("ImportData", "Select name of date column:"))
        self.label_4.setText(_translate("ImportData", "Select name of time column:"))
        self.label_6.setText(_translate("ImportData", "Select date format:"))
        self.comboBox_nameTimestamp.setItemText(0, _translate("ImportData", "create new (input right)"))
        self.label_datefromatinfo.setText(_translate("ImportData", "(1st date is 2020-08-01 01:00:02)"))
        self.groupBox_selectclassification.setTitle(_translate("ImportData", "Select Classification"))
        self.label_8.setText(_translate("ImportData", "Select Broker:"))
        self.label_5.setText(_translate("ImportData", "Select Type of Asset:"))
        self.groupBox_addNewClassification.setTitle(_translate("ImportData", "Add new Classifications"))
        self.label_9.setText(_translate("ImportData", "Name new Broker:"))
        self.label_7.setText(_translate("ImportData", "Name new Asset Type:"))
        self.pushButton_submitAssetType.setText(_translate("ImportData", "Submit"))
        self.pushButton_submitnewBroker.setText(_translate("ImportData", "Submit"))

    def submit_importedData(self):
        '''Extract all datas, copy the dataframe in appropriate folder, and update the imported_data_sumup dic'''
        # extract data
        self.create_dic_imported_data()
        # copy df
        path_src = self.path_src
        path_target = self.path_target
        shutil.copy(path_src, path_target)
        # updtade imported data dic sumup
        with open(self.path_imported_data_sumup_json,'r') as f:
            dic_imported_data_sumup = json.load(f)
            f.close()
        dic_imported_data_sumup[self.namefile_imported_data] = self.dic_imported_data
        with open(self.path_imported_data_sumup_json,'w') as f:
            json.dump(dic_imported_data_sumup, f)
            f.close()

    def open_file_dialog(self):
        '''open an open_file dialog and update the name file'''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filePath, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", 
                                                  "C:/Users/Paul/Trading/Data", 
                                                  "All Files (*.csv);;Python Files (*.py)", options=options)
        if filePath:
            print('found file ', filePath)
        self.path_src = filePath
        self.namefile_imported_data = self.pathFileToOpen.split('/')[-1]
        self.textBrowser_OpenFile.setPlainText(self.namefile_imported_data)
        self.path_target = self.path_target_folder + self.namefile_imported_data

    def function_showPreview(self):
        '''Read the csv and extract 1st row, then create the rows and columns for QtableWidget. Finally Show columns and 1st row as string label in each slot'''
        # read csv and extract data
        if not self.data_have_been_imported:
            self.df = pd.read_csv(path_src)
            self.data_have_been_imported = True
        list_columns_str = [col for col in self.df]
        list_values_str = [str(self.df.iloc[0,i]) for i in range(len(self.df.columns))]
        # create the rows and columns
        self.tableWidget__dfPreview.clear()
        self.tableWidget__dfPreview.setColumnCount(len(self.df.columns))
        self.tableWidget__dfPreview.setRowCount(2)
        for i in range(0,len(self.df.columns)):
            self.tableWidget__dfPreview.setItem(0,i, QtWidgets.QTableWidgetItem(list_columns_str[i]))
            self.tableWidget__dfPreview.setItem(1,i, QtWidgets.QTableWidgetItem(list_values_str[i]))
        # Print values as labels in slots

    def onSelectCreateNewTimestamp(self):
        '''Triggered by signal of self combobox name timestamp changed, if name is 'create new...' then enable the edit text on the right, else: disable it'''
        # check value
        current_time_name = self.comboBox_nameTimestamp.currentText()
        # disable or enable
        if current_time_name == 'create new (input right)':
            self.textEdit_nameTimeStamp.setEnabled(True)
        else:
            self.textEdit_nameTimeStamp.setEnabled(False)


    def function_submitNewAssetType(self):
        '''Extract name of new asset type value, then open the classification_data.json and add it to the asset type key. Finally Add a row to the asset type combo box'''
        # extract name
        new_assetType_name = self.textEdit_NewBroker.toPlainText()
        # put it in json classification
        with open(self.path_classification_data_json,'r') as f:
            dic_classification_imported_data = json.load(f)
            f.close()
        dic_classification_imported_data['list_type_assets'].append(new_assetType_name)
        with open(self.path_classification_data_json,'w') as f:
            json.dump(dic_classification_imported_data, f)
            f.close()  
        # add row to asset type combobox
        self.comboBox_typeAsset.addItem("")
        self.comboBox_typeAsset.setItemText(len(dic_classification_imported_data['list_type_assets'])-1, _translate("ImportData", new_assetType_name))


    def function_submitNewBroker(self):
        '''Extract name of new broker value, then open the classification_data.json and add it to the broker key. Finally Add a row to the broker combo box'''
        # extract name
        new_broker_name = self.textEdit_NewBroker.toPlainText()
        # put it in json classification
        with open(self.path_classification_data_json,'r') as f:
            dic_classification_imported_data = json.load(f)
            f.close()
        dic_classification_imported_data['list_broker'].append(new_broker_name)
        with open(self.path_classification_data_json,'w') as f:
            json.dump(dic_classification_imported_data, f)
            f.close()  
        # add row to broker combobox
        self.comboBox_broker.addItem("")
        self.comboBox_broker.setItemText(len(dic_classification_imported_data['list_broker'])-1, _translate("ImportData", new_broker_name))

    def create_dic_imported_data(self):
        '''create the dic of imported data that will be put under imported_data_sumup[namefile]'''
        # extract data
        if not self.data_have_been_imported:
            self.df = pd.read_csv(path_src)
            self.data_have_been_imported = True
        self.name_columns = [col for col in self.df.columns]
        type_data = self.comboBox_DataType.currentText().split(' ')[0]
        name_date_column = self.comboBox_nameDateColumn.currentText()
        name_time_column = self.comboBox_nameTimestamp.currentText()
        if name_time_column == 'create new (input right)':
            name_time_column = self.textEdit_nameTimeStamp.toPlainText()
        list_columns = self.name_columns
        format_date = self.textEdit_dateFormat.toPlainText()
        initDate = datetime.datetime.strptime(self.df.time.iloc[0],format_date).strftime(format="%Y-%m-%d %H:%M")
        endDate = datetime.datetime.strptime(self.df.time.iloc[-1],format_date).strftime(format="%Y-%m-%d %H:%M")
        type_asset = self.comboBox_typeAsset.currentText()
        broker = self.comboBox_broker.currentText()
        # create dic
        self.dic_imported_data = {'type_data':type_data, 'initDate':initDate, 'endDate':endDate, 'name_date_column':name_date_column, 'name_time_column':name_time_column,
                                    'list_columns':list_columns, 'format_date':format_date, 'type_asset':type_asset, 'broker':broker}

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImportData = QtWidgets.QDialog()
    ui = Ui_ImportData()
    ui.setupUi(ImportData)
    ImportData.show()
    sys.exit(app.exec_())
