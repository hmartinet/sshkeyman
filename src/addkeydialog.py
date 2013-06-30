# -*- coding: utf-8 -*-

from PyQt4.QtGui import QDialog
from ui.addkeydialogui import Ui_add_key_dialog

class AddKeyDialog(QDialog, Ui_add_key_dialog):
 
    _key = None
 
    def __init__(self, profile_name=None, profile=None):
        QDialog.__init__(self)
        self.setupUi(self)
        self.button_box.rejected.connect(self.cancel)
        self.button_box.accepted.connect(self.save)
        
    def key(self):
        return self._key
        
    def save(self):
        line = unicode(self.key_edit.toPlainText())
        keyline = line.split(' ')
        if len(keyline) == 3:
            proto = keyline[0].rstrip()
            key = keyline[1].rstrip()
            keyname = keyline[2].rstrip()
            self._key = {'keyname': keyname, 'proto' : proto, 'key' : key, 'full' : line.rstrip()}
            self.close()
        
    def cancel(self):
        self.close()
        
