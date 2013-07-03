# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog, QListWidgetItem
from ui.profiledialogui import Ui_profile_dialog
from editprofiledialog import EditProfileDialog
import json
 
class ProfileDialog(QDialog, Ui_profile_dialog):
    
    _settings = None
    _profiles = {}
    
    _selected_profile = None
 
    def __init__(self, settings, load_default):
        QDialog.__init__(self)
        self.setupUi(self)
        
        self._settings = settings
        self._profiles = json.loads(str(settings.value('profiles', '{}').toString()))
        self.load_profiles(load_default)
            
        self.add_button.clicked.connect(self.add_profile)
        self.remove_button.clicked.connect(self.remove_profile)
        
        self.edit_button.clicked.connect(self.edit_profile)
        self.open_button.clicked.connect(self.open_profile)
        self.profile_list.doubleClicked.connect(self.open_profile)
        
    def reset(self):
        self._selected_profile = None
        
    def selected_profile(self):
        return self._selected_profile
        
    def load_profiles(self, load_default):
        while self.profile_list.count() > 0:
            self.profile_list.takeItem(0)
        for profile_name, profile in self._profiles.items():
            item = QListWidgetItem(unicode(profile_name) + (u' (default)' if profile['default'] else u''))
            item.setData(Qt.UserRole, unicode(profile_name))
            self.profile_list.addItem(item)
            if load_default and profile['default']:
                self._selected_profile = profile
            
    def add_profile(self):
        edit_profile_dialog = EditProfileDialog()
        edit_profile_dialog.setWindowTitle(u'Add Profile')
        edit_profile_dialog.exec_()
        new_profile = edit_profile_dialog.profile()
        if new_profile:
            if new_profile['default']:
                for profile in self._profiles.values():
                    profile['default'] = False
            self._profiles[edit_profile_dialog.profile_name()] = new_profile
            self._settings.setValue('profiles', json.dumps(self._profiles))
            self.load_profiles(False)
        
    def remove_profile(self):
        if self.profile_list.selectedItems():
            del self._profiles[unicode(self.profile_list.selectedItems()[0].data(Qt.UserRole).toString())]
            self._settings.setValue('profiles', json.dumps(self._profiles))
            self.load_profiles()
            
    def edit_profile(self):
        if self.profile_list.selectedItems():
            profile_name = unicode(self.profile_list.selectedItems()[0].data(Qt.UserRole).toString())
            edit_profile_dialog = EditProfileDialog(profile_name, self._profiles[profile_name])
            edit_profile_dialog.setWindowTitle(u'Edit Profile')
            edit_profile_dialog.exec_()
            new_profile = edit_profile_dialog.profile()
            if new_profile:
                del self._profiles[profile_name]
                if new_profile['default']:
                    for profile in self._profiles.values():
                        profile['default'] = False
                self._profiles[edit_profile_dialog.profile_name()] = new_profile
                self._settings.setValue('profiles', json.dumps(self._profiles))
                self.load_profiles()
                
    def open_profile(self):
        if self.profile_list.selectedItems():
            self._selected_profile = self._profiles[unicode(self.profile_list.selectedItems()[0].data(Qt.UserRole).toString())]
            self.close()

