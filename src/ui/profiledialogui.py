# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtcreator/sshkeyman/profiledialog.ui'
#
# Created: Fri Jul  5 12:06:08 2013
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

class Ui_profile_dialog(object):
    def setupUi(self, profile_dialog):
        profile_dialog.setObjectName(_fromUtf8("profile_dialog"))
        profile_dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(profile_dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_2 = QtGui.QWidget(profile_dialog)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.profile_list = QtGui.QListWidget(self.widget_2)
        self.profile_list.setObjectName(_fromUtf8("profile_list"))
        self.horizontalLayout_2.addWidget(self.profile_list)
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.add_button = QtGui.QToolButton(self.widget_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("media/icon/16x16/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon)
        self.add_button.setAutoRaise(True)
        self.add_button.setObjectName(_fromUtf8("add_button"))
        self.verticalLayout_2.addWidget(self.add_button)
        self.remove_button = QtGui.QToolButton(self.widget_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("media/icon/16x16/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_button.setIcon(icon1)
        self.remove_button.setAutoRaise(True)
        self.remove_button.setObjectName(_fromUtf8("remove_button"))
        self.verticalLayout_2.addWidget(self.remove_button)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtGui.QWidget(profile_dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.edit_button = QtGui.QPushButton(self.widget)
        self.edit_button.setObjectName(_fromUtf8("edit_button"))
        self.horizontalLayout.addWidget(self.edit_button)
        self.open_button = QtGui.QPushButton(self.widget)
        self.open_button.setObjectName(_fromUtf8("open_button"))
        self.horizontalLayout.addWidget(self.open_button)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(profile_dialog)
        QtCore.QMetaObject.connectSlotsByName(profile_dialog)
        profile_dialog.setTabOrder(self.profile_list, self.open_button)
        profile_dialog.setTabOrder(self.open_button, self.edit_button)
        profile_dialog.setTabOrder(self.edit_button, self.add_button)
        profile_dialog.setTabOrder(self.add_button, self.remove_button)

    def retranslateUi(self, profile_dialog):
        profile_dialog.setWindowTitle(_translate("profile_dialog", "Profiles", None))
        self.add_button.setText(_translate("profile_dialog", "...", None))
        self.remove_button.setText(_translate("profile_dialog", "...", None))
        self.edit_button.setText(_translate("profile_dialog", "Edit", None))
        self.open_button.setText(_translate("profile_dialog", "Open", None))

