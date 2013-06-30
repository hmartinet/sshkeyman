# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtcreator/sshkeyman/addkeydialog.ui'
#
# Created: Sun Jun 30 22:39:29 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_add_key_dialog(object):
    def setupUi(self, add_key_dialog):
        add_key_dialog.setObjectName(_fromUtf8("add_key_dialog"))
        add_key_dialog.resize(364, 290)
        self.verticalLayout = QtGui.QVBoxLayout(add_key_dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.key_edit = QtGui.QTextEdit(add_key_dialog)
        self.key_edit.setObjectName(_fromUtf8("key_edit"))
        self.verticalLayout.addWidget(self.key_edit)
        self.button_box = QtGui.QDialogButtonBox(add_key_dialog)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(add_key_dialog)
        QtCore.QMetaObject.connectSlotsByName(add_key_dialog)

    def retranslateUi(self, add_key_dialog):
        add_key_dialog.setWindowTitle(_translate("add_key_dialog", "Add SSH key", None))

