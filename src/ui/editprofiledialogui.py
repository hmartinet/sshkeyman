# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtcreator/sshkeyman/editprofiledialog.ui'
#
# Created: Wed Jul  3 14:11:59 2013
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

class Ui_edit_profile_dialog(object):
    def setupUi(self, edit_profile_dialog):
        edit_profile_dialog.setObjectName(_fromUtf8("edit_profile_dialog"))
        edit_profile_dialog.resize(357, 212)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(edit_profile_dialog.sizePolicy().hasHeightForWidth())
        edit_profile_dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(edit_profile_dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.name_label = QtGui.QLabel(edit_profile_dialog)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.name_label)
        self.widget = QtGui.QWidget(edit_profile_dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.name_edit = QtGui.QLineEdit(self.widget)
        self.name_edit.setObjectName(_fromUtf8("name_edit"))
        self.horizontalLayout.addWidget(self.name_edit)
        self.default_checkbox = QtGui.QCheckBox(self.widget)
        self.default_checkbox.setObjectName(_fromUtf8("default_checkbox"))
        self.horizontalLayout.addWidget(self.default_checkbox)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.widget)
        self.host_label = QtGui.QLabel(edit_profile_dialog)
        self.host_label.setObjectName(_fromUtf8("host_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.host_label)
        self.host_edit = QtGui.QLineEdit(edit_profile_dialog)
        self.host_edit.setObjectName(_fromUtf8("host_edit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.host_edit)
        self.user_label = QtGui.QLabel(edit_profile_dialog)
        self.user_label.setObjectName(_fromUtf8("user_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.user_label)
        self.user_edit = QtGui.QLineEdit(edit_profile_dialog)
        self.user_edit.setObjectName(_fromUtf8("user_edit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.user_edit)
        self.label = QtGui.QLabel(edit_profile_dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.widget_2 = QtGui.QWidget(edit_profile_dialog)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.key_edit = QtGui.QLineEdit(self.widget_2)
        self.key_edit.setObjectName(_fromUtf8("key_edit"))
        self.horizontalLayout_2.addWidget(self.key_edit)
        self.key_choose_button = QtGui.QToolButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_choose_button.sizePolicy().hasHeightForWidth())
        self.key_choose_button.setSizePolicy(sizePolicy)
        self.key_choose_button.setObjectName(_fromUtf8("key_choose_button"))
        self.horizontalLayout_2.addWidget(self.key_choose_button)
        self.horizontalLayout_2.setStretch(0, 1)
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.widget_2)
        self.file_label = QtGui.QLabel(edit_profile_dialog)
        self.file_label.setObjectName(_fromUtf8("file_label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.file_label)
        self.file_edit = QtGui.QLineEdit(edit_profile_dialog)
        self.file_edit.setObjectName(_fromUtf8("file_edit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.file_edit)
        self.verticalLayout.addLayout(self.formLayout)
        self.button_box = QtGui.QDialogButtonBox(edit_profile_dialog)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(edit_profile_dialog)
        QtCore.QMetaObject.connectSlotsByName(edit_profile_dialog)
        edit_profile_dialog.setTabOrder(self.button_box, self.name_edit)
        edit_profile_dialog.setTabOrder(self.name_edit, self.default_checkbox)
        edit_profile_dialog.setTabOrder(self.default_checkbox, self.host_edit)
        edit_profile_dialog.setTabOrder(self.host_edit, self.user_edit)
        edit_profile_dialog.setTabOrder(self.user_edit, self.key_edit)
        edit_profile_dialog.setTabOrder(self.key_edit, self.key_choose_button)
        edit_profile_dialog.setTabOrder(self.key_choose_button, self.file_edit)

    def retranslateUi(self, edit_profile_dialog):
        edit_profile_dialog.setWindowTitle(_translate("edit_profile_dialog", "Edit Profile", None))
        self.name_label.setText(_translate("edit_profile_dialog", "Name", None))
        self.default_checkbox.setText(_translate("edit_profile_dialog", "default", None))
        self.host_label.setText(_translate("edit_profile_dialog", "Host", None))
        self.user_label.setText(_translate("edit_profile_dialog", "User", None))
        self.label.setText(_translate("edit_profile_dialog", "SSH key", None))
        self.key_edit.setToolTip(_translate("edit_profile_dialog", "If your ssh-agent already knows your key, you can leave this field empty.", None))
        self.key_edit.setPlaceholderText(_translate("edit_profile_dialog", "Use your ssh-agent if empty", None))
        self.key_choose_button.setText(_translate("edit_profile_dialog", "...", None))
        self.file_label.setText(_translate("edit_profile_dialog", "File", None))
        self.file_edit.setText(_translate("edit_profile_dialog", "/var/sshkeyman/servers", None))

