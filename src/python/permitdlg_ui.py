# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'permitdlg.ui'
#
# Created: Fri Aug 15 04:25:40 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PermitDialog(object):
    def setupUi(self, PermitDialog):
        PermitDialog.setObjectName("PermitDialog")
        PermitDialog.resize(603, 393)
        PermitDialog.setSizeGripEnabled(True)
        PermitDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(PermitDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.filenameLabel = QtWidgets.QLabel(PermitDialog)
        self.filenameLabel.setObjectName("filenameLabel")
        self.verticalLayout.addWidget(self.filenameLabel)
        self.label = QtWidgets.QLabel(PermitDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.detailsButton = QtWidgets.QPushButton(PermitDialog)
        self.detailsButton.setCheckable(True)
        self.detailsButton.setObjectName("detailsButton")
        self.horizontalLayout.addWidget(self.detailsButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.problemsBrowser = QtWidgets.QTextBrowser(PermitDialog)
        self.problemsBrowser.setObjectName("problemsBrowser")
        self.gridLayout.addWidget(self.problemsBrowser, 1, 0, 1, 1)
        self.rememberCheck = QtWidgets.QCheckBox(PermitDialog)
        self.rememberCheck.setObjectName("rememberCheck")
        self.gridLayout.addWidget(self.rememberCheck, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.allowButton = QtWidgets.QPushButton(PermitDialog)
        self.allowButton.setObjectName("allowButton")
        self.horizontalLayout_2.addWidget(self.allowButton)
        self.denyButton = QtWidgets.QPushButton(PermitDialog)
        self.denyButton.setDefault(True)
        self.denyButton.setObjectName("denyButton")
        self.horizontalLayout_2.addWidget(self.denyButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.retranslateUi(PermitDialog)
        QtCore.QMetaObject.connectSlotsByName(PermitDialog)

    def retranslateUi(self, PermitDialog):
        _translate = QtCore.QCoreApplication.translate
        PermitDialog.setWindowTitle(_translate("PermitDialog", "Confirm to run unsafe script"))
        self.filenameLabel.setText(_translate("PermitDialog", "scriptname.py"))
        self.label.setText(_translate("PermitDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Attention:</span> This script file contains code which <span style=\" font-style:italic;\">might harm </span>your system.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You should only permit execution of this script if you are sure that it comes from a trustworthy source. </p></body></html>"))
        self.detailsButton.setText(_translate("PermitDialog", "De&tails >>"))
        self.problemsBrowser.setHtml(_translate("PermitDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\';\"></p></body></html>"))
        self.rememberCheck.setText(_translate("PermitDialog", "&Remember preference for this file"))
        self.allowButton.setText(_translate("PermitDialog", "&Allow"))
        self.denyButton.setText(_translate("PermitDialog", "&Deny"))

