# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subClasses/dialog_importData_OHLCPriceNamesDict.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_OHLCPriceNamesDict(object):
    def setupUi(self, Dialog_OHLCPriceNamesDict, name_columns):
        Dialog_OHLCPriceNamesDict.setObjectName("Dialog_OHLCPriceNamesDict")
        Dialog_OHLCPriceNamesDict.resize(348, 211)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_OHLCPriceNamesDict)
        self.buttonBox.setGeometry(QtCore.QRect(100, 170, 151, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog_OHLCPriceNamesDict)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 311, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 2, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_4.sizePolicy().hasHeightForWidth())
        self.textBrowser_4.setSizePolicy(sizePolicy)
        self.textBrowser_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 3, 1, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 1, 1, 1, 1)
        self.comboBox_open = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_open.setObjectName("comboBox_open")
        self.gridLayout.addWidget(self.comboBox_open, 0, 0, 1, 1)
        self.comboBox_high = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_high.setObjectName("comboBox_high")
        self.gridLayout.addWidget(self.comboBox_high, 1, 0, 1, 1)
        self.comboBox_low = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_low.setObjectName("comboBox_low")
        self.gridLayout.addWidget(self.comboBox_low, 2, 0, 1, 1)
        self.comboBox_close = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_close.setObjectName("comboBox_close")
        self.gridLayout.addWidget(self.comboBox_close, 3, 0, 1, 1)
        
        # variables
        self.name_columns = name_columns
        self.dic_price_name = {}
        #combo boxes
        for col in name_columns:
            self.comboBox_open.addItem("")
            self.comboBox_high.addItem("")
            self.comboBox_low.addItem("")
            self.comboBox_close.addItem("")

        self.retranslateUi(Dialog_OHLCPriceNamesDict)
        self.buttonBox.accepted.connect(Dialog_OHLCPriceNamesDict.accept)
        self.buttonBox.accepted.connect(self.submit)
        self.buttonBox.rejected.connect(Dialog_OHLCPriceNamesDict.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_OHLCPriceNamesDict)
        
        

    def retranslateUi(self, Dialog_OHLCPriceNamesDict):
        _translate = QtCore.QCoreApplication.translate
        Dialog_OHLCPriceNamesDict.setWindowTitle(_translate("Dialog_OHLCPriceNamesDict", "Dialog"))
        for i in range(len(self.name_columns)):
            self.comboBox_open.setItemText(i, _translate("ImportData", self.name_columns[i]))
            self.comboBox_high.setItemText(i, _translate("ImportData", self.name_columns[i]))
            self.comboBox_low.setItemText(i, _translate("ImportData", self.name_columns[i]))
            self.comboBox_close.setItemText(i, _translate("ImportData", self.name_columns[i]))
        self.textBrowser_3.setHtml(_translate("Dialog_OHLCPriceNamesDict", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">low</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog_OHLCPriceNamesDict", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">open</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Dialog_OHLCPriceNamesDict", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">close</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog_OHLCPriceNamesDict", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">high</span></p></body></html>"))

    def submit(self):
        self.dic_price_name = {self.comboBox_open.currentText():'open', self.comboBox_high.currentText():'high', self.comboBox_low.currentText():'low', self.comboBox_close.currentText():'close'}

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_OHLCPriceNamesDict = QtWidgets.QDialog()
    ui = Ui_Dialog_OHLCPriceNamesDict()
    ui.setupUi(Dialog_OHLCPriceNamesDict)
    Dialog_OHLCPriceNamesDict.show()
    sys.exit(app.exec_())
