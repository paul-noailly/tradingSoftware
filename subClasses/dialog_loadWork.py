# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subClasses/dialog_loadWork.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_loadWork(object):
    def setupUi(self, Dialog_loadWork, list_work):
        Dialog_loadWork.setObjectName("Dialog_loadWork")
        Dialog_loadWork.resize(450, 251)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_loadWork)
        self.buttonBox.setGeometry(QtCore.QRect(110, 210, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_loadWork)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        self.comboBox_selectWork = QtWidgets.QComboBox(Dialog_loadWork)
        self.comboBox_selectWork.setGeometry(QtCore.QRect(90, 10, 291, 20))
        self.comboBox_selectWork.setObjectName("comboBox_selectWork")
        self.textBrowser_workDescription = QtWidgets.QTextBrowser(Dialog_loadWork)
        self.textBrowser_workDescription.setGeometry(QtCore.QRect(10, 60, 371, 141))
        self.textBrowser_workDescription.setObjectName("textBrowser_workDescription")
        self.label_2 = QtWidgets.QLabel(Dialog_loadWork)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog_loadWork)
        self.buttonBox.accepted.connect(Dialog_loadWork.accept)
        self.buttonBox.accepted.connect(self.submit)
        self.buttonBox.rejected.connect(Dialog_loadWork.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_loadWork)
        
        # variables
        self.list_work = list_work
        self.selected_work = ''
        #combo boxes
        for work in list_work:
            self.comboBox_selectWork.addItem("")
        for i in range(len(self.list_work)):
            self.comboBox_selectWork.setItemText(i, self._translate("ImportData", self.list_work[i]))

        

    def retranslateUi(self, Dialog_loadWork):
        self._translate = QtCore.QCoreApplication.translate
        Dialog_loadWork.setWindowTitle(self._translate("Dialog_loadWork", "Dialog"))
        self.label.setText(self._translate("Dialog_loadWork", "Select a work:"))
        self.label_2.setText(self._translate("Dialog_loadWork", "Selected work description:"))
        
    def submit(self):
        self.selected_work = self.comboBox_selectWork.currentText().split('.jso')[0]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_loadWork = QtWidgets.QDialog()
    ui = Ui_Dialog_loadWork()
    ui.setupUi(Dialog_loadWork)
    Dialog_loadWork.show()
    sys.exit(app.exec_())
