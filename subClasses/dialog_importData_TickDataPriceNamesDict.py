# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subClasses/dialog_importData_TickDataPriceNamesDict.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_TickDataPriceNamesDict(object):
    def setupUi(self, Dialog_TickDataPriceNamesDict, name_columns):
        Dialog_TickDataPriceNamesDict.setObjectName("Dialog_TickDataPriceNamesDict")
        Dialog_TickDataPriceNamesDict.resize(321, 162)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_TickDataPriceNamesDict)
        self.buttonBox.setGeometry(QtCore.QRect(90, 120, 141, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog_TickDataPriceNamesDict)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 301, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_midPrice = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_midPrice.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_midPrice.sizePolicy().hasHeightForWidth())
        self.textBrowser_midPrice.setSizePolicy(sizePolicy)
        self.textBrowser_midPrice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_midPrice.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_midPrice.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_midPrice.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textBrowser_midPrice.setTabChangesFocus(False)
        self.textBrowser_midPrice.setObjectName("textBrowser_midPrice")
        self.gridLayout.addWidget(self.textBrowser_midPrice, 0, 1, 1, 1)
        self.comboBox_askPrice = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_askPrice.sizePolicy().hasHeightForWidth())
        self.comboBox_askPrice.setSizePolicy(sizePolicy)
        self.comboBox_askPrice.setObjectName("comboBox_askPrice")
        self.gridLayout.addWidget(self.comboBox_askPrice, 1, 0, 1, 1)
        self.textBrowser_bidPrice = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_bidPrice.sizePolicy().hasHeightForWidth())
        self.textBrowser_bidPrice.setSizePolicy(sizePolicy)
        self.textBrowser_bidPrice.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textBrowser_bidPrice.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_bidPrice.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_bidPrice.setObjectName("textBrowser_bidPrice")
        self.gridLayout.addWidget(self.textBrowser_bidPrice, 2, 1, 1, 1)
        self.comboBox_bidPrice = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_bidPrice.sizePolicy().hasHeightForWidth())
        self.comboBox_bidPrice.setSizePolicy(sizePolicy)
        self.comboBox_bidPrice.setObjectName("comboBox_bidPrice")
        self.gridLayout.addWidget(self.comboBox_bidPrice, 2, 0, 1, 1)
        self.comboBox_midPrice = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_midPrice.sizePolicy().hasHeightForWidth())
        self.comboBox_midPrice.setSizePolicy(sizePolicy)
        self.comboBox_midPrice.setObjectName("comboBox_midPrice")
        self.gridLayout.addWidget(self.comboBox_midPrice, 0, 0, 1, 1)
        self.textBrowser_askPrice = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_askPrice.sizePolicy().hasHeightForWidth())
        self.textBrowser_askPrice.setSizePolicy(sizePolicy)
        self.textBrowser_askPrice.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_askPrice.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_askPrice.setObjectName("textBrowser_askPrice")
        self.gridLayout.addWidget(self.textBrowser_askPrice, 1, 1, 1, 1)
        
        # variables
        self.name_columns = name_columns
        self.dic_price_name = {}
        #combo boxes
        for col in name_columns:
            self.comboBox_midPrice.addItem("")
            self.comboBox_bidPrice.addItem("")
            self.comboBox_askPrice.addItem("")

        self.retranslateUi(Dialog_TickDataPriceNamesDict)
        self.buttonBox.accepted.connect(Dialog_TickDataPriceNamesDict.accept)
        self.buttonBox.accepted.connect(self.submit)
        self.buttonBox.rejected.connect(Dialog_TickDataPriceNamesDict.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_TickDataPriceNamesDict)

    def retranslateUi(self, Dialog_TickDataPriceNamesDict):
        _translate = QtCore.QCoreApplication.translate
        Dialog_TickDataPriceNamesDict.setWindowTitle(_translate("Dialog_TickDataPriceNamesDict", "Dialog"))
        for i in range(len(self.name_columns)):
            self.comboBox_midPrice.setItemText(i, _translate("ImportData", self.name_columns[i]))
            self.comboBox_bidPrice.setItemText(i, _translate("ImportData", self.name_columns[i]))
            self.comboBox_askPrice.setItemText(i, _translate("ImportData", self.name_columns[i]))
        self.textBrowser_midPrice.setHtml(_translate("Dialog_TickDataPriceNamesDict", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">midPrice</span></p></body></html>"))
        self.textBrowser_bidPrice.setHtml(_translate("Dialog_TickDataPriceNamesDict", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">bidPrice</span></p></body></html>"))
        self.textBrowser_askPrice.setHtml(_translate("Dialog_TickDataPriceNamesDict", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">askPrice</span></p></body></html>"))
        
    def submit(self):
        self.dic_price_name = {self.comboBox_midPrice.currentText():'midPrice', self.comboBox_bidPrice.currentText():'bidPrice', self.comboBox_askPrice.currentText():'askPrice'}


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_TickDataPriceNamesDict = QtWidgets.QDialog()
    ui = Ui_Dialog_TickDataPriceNamesDict()
    ui.setupUi(Dialog_TickDataPriceNamesDict)
    Dialog_TickDataPriceNamesDict.show()
    sys.exit(app.exec_())
