# -*- coding: utf-8 -*-

from PyQt4.QtGui import QDialog, QDialogButtonBox, QFileDialog
from ui.editprofiledialogui import Ui_edit_profile_dialog
 
class EditProfileDialog(QDialog, Ui_edit_profile_dialog):
    
    _profile_name = None
    _profile = None
 
    def __init__(self, profile_name=None, profile=None):
        QDialog.__init__(self)
        self.setupUi(self)
        
        if profile_name:
            self.name_edit.setText(unicode(profile_name))
        if profile:
            if 'default' in profile:
                self.default_checkbox.setChecked(profile['default'])
            if 'host' in profile:
                self.host_edit.setText(unicode(profile['host']))
            if 'user' in profile:
                self.user_edit.setText(unicode(profile['user']))
            if 'key' in profile:
                self.key_edit.setText(unicode(profile['key']))
            if 'file' in profile:
                self.file_edit.setText(unicode(profile['file']))
            if 'timeout' in profile:
                self.timeout_spinbox.setValue(float(profile['timeout']))                
        
        self.name_edit.textChanged.connect(self.check_form)
        self.host_edit.textChanged.connect(self.check_form)
        self.user_edit.textChanged.connect(self.check_form)
        self.file_edit.textChanged.connect(self.check_form)
        self.timeout_spinbox.valueChanged.connect(self.check_form)
        self.button_box.rejected.connect(self.close)
        self.button_box.accepted.connect(self.save_profile)
        self.key_choose_button.clicked.connect(self.open_file_chooser)
        self.check_form()
        
    def profile_name(self):
        return self._profile_name
        
    def profile(self):
        return self._profile
    
    def open_file_chooser(self):
        self.key_edit.setText(QFileDialog.getOpenFileName())
            
    def save_profile(self):
        self._profile_name = unicode(self.name_edit.text())
        self._profile = {
            'host': unicode(self.host_edit.text()),
            'user': unicode(self.user_edit.text()),
            'key': unicode(self.key_edit.text()),
            'file': unicode(self.file_edit.text()),
            'default': self.default_checkbox.isChecked(),
            'timeout': self.timeout_spinbox.value()
        }
        self.close()
        
    def is_form_valid(self):
        if not self.name_edit.text():
            return False
        if not self.host_edit.text():
            return False
        if not self.user_edit.text():
            return False
        if not self.file_edit.text():
            return False
        return True
        
    def check_form(self):
        if self.is_form_valid():
            self.button_box.button(QDialogButtonBox.Save).setEnabled(True)
        else:
            self.button_box.button(QDialogButtonBox.Save).setEnabled(False)        


