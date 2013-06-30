# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QApplication, QMessageBox
from mainwindow import MainWindow
from profiledialog import ProfileDialog
import socket
import jsonschema

def main(argv):
    app = QApplication(argv, True)
    
    settings = QSettings('sshkeyman', 'sshkeyman')
    
    no_connection = True
    wnd = None
    profile_dialog = ProfileDialog(settings)
    while (no_connection):
        try:   
            profile_dialog.exec_()
            profile = profile_dialog.selected_profile()
            if not profile:
                sys.exit()
            
            wnd = MainWindow(profile)
            wnd.show()
            no_connection = False
        except socket.error as ex:
            if wnd:
                wnd.close()
            profile_dialog.reset()
            box = QMessageBox(QMessageBox.Critical, unicode(ex.__class__.__name__), unicode('Failed to connect to server !'))
            box.setDetailedText(unicode(ex).replace('\\n', '\n').replace('\\t', '    '));
            box.exec_()
        except (jsonschema.SchemaError, jsonschema.ValidationError) as ex:
            if wnd:
                wnd.close()
            profile_dialog.reset()
            box = QMessageBox(QMessageBox.Critical, unicode(ex.__class__.__name__), unicode('The servers configuration file format in invalid !'))
            box.setDetailedText(unicode(ex).replace('\\n', '\n').replace('\\t', '    '));
            box.exec_()
    
    app.exec_()
    if wnd.reload_profiles():
        main(argv)
 
if __name__ == "__main__":
    main(sys.argv)