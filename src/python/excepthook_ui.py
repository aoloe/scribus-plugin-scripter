# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'excepthook.ui'
#
# Created: Fri Aug 15 04:25:07 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExceptHookDialog(object):
    def setupUi(self, ExceptHookDialog):
        ExceptHookDialog.setObjectName("ExceptHookDialog")
        ExceptHookDialog.resize(542, 290)
        self.verticalLayout = QtWidgets.QVBoxLayout(ExceptHookDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(ExceptHookDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.closeButton = QtWidgets.QPushButton(ExceptHookDialog)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 0, 1, 1, 1)
        self.exceptionLabel = QtWidgets.QLabel(ExceptHookDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exceptionLabel.setFont(font)
        self.exceptionLabel.setObjectName("exceptionLabel")
        self.gridLayout.addWidget(self.exceptionLabel, 1, 0, 1, 1)
        self.detailsButton = QtWidgets.QPushButton(ExceptHookDialog)
        self.detailsButton.setObjectName("detailsButton")
        self.gridLayout.addWidget(self.detailsButton, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tracebackBrowser = QtWidgets.QTextBrowser(ExceptHookDialog)
        self.tracebackBrowser.setMinimumSize(QtCore.QSize(0, 200))
        self.tracebackBrowser.setObjectName("tracebackBrowser")
        self.verticalLayout.addWidget(self.tracebackBrowser)

        self.retranslateUi(ExceptHookDialog)
        QtCore.QMetaObject.connectSlotsByName(ExceptHookDialog)

    def retranslateUi(self, ExceptHookDialog):
        _translate = QtCore.QCoreApplication.translate
        ExceptHookDialog.setWindowTitle(_translate("ExceptHookDialog", "Script error"))
        self.label.setText(_translate("ExceptHookDialog", "An exception occurred while running the script."))
        self.closeButton.setText(_translate("ExceptHookDialog", "&Close"))
        self.exceptionLabel.setText(_translate("ExceptHookDialog", "Exception"))
        self.detailsButton.setText(_translate("ExceptHookDialog", "&Details >>"))

