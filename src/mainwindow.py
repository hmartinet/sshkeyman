# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QMainWindow, QTreeWidgetItem, QListWidgetItem, QMessageBox
from ui.mainwindowui import Ui_main
from splashscreen import SplashScreen
from addkeydialog import AddKeyDialog
import paramiko
import json
from jsonschema import validate
import time
import jsonschema
import socket
 
class MainWindow(QMainWindow, Ui_main):
    
    _servers = {}
    _keys = {}
    _commit_keys = {}
    _items = {}
    _splash = None
    
    _profile = None
    
    _selected_key_name = None
    _reload_profiles = False
 
    def __init__(self, profile):
        self._splash = SplashScreen()
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self._profile = profile
        self.rollback_button.clicked.connect(self.load)
        self.commit_button.clicked.connect(self.commit)
        self.key_list.currentItemChanged.connect(self.key_item_selected)
        self.key_list.itemChanged.connect(self.key_item_changed)
        self.server_tree.itemChanged.connect(self.server_item_selected)
        
        self.add_key_button.clicked.connect(self.import_key)
        self.remove_key_button.clicked.connect(self.remove_key)
        
        self.action_import_key.triggered.connect(self.import_key)
        self.action_profiles.triggered.connect(self.open_profiles)
        self.action_exit.triggered.connect(self.close)
        self.action_about.triggered.connect(self.about)
        
        self.load()
        self.move(self._splash.pos() + self._splash.rect().center() - self.rect().center());
        
    def load(self, action=u'load'):   
        self.key_list.blockSignals(True)
         
        if action == u'commit':
            self._commit_keys = self._keys
        else:
            self._commit_keys = {}
        self._keys = {}
        self._items = {}
         
        self.hide() 
        self._splash.setProgress(0.0, u'Loading server list...')
        self._splash.show()
        
        for _ in range(20):
            time.sleep(0.001)
            QApplication.processEvents()
        
        try:
            self.load_server_list()
            self.load_key_list(action)
            
            self._splash.hide()
            self.show()
            self.key_list.blockSignals(False)
            
            item = self.key_list.item(0)
            item.setSelected(True)
            self.key_item_selected(item)
        except (jsonschema.SchemaError, jsonschema.ValidationError) as ex:
            self.key_list.blockSignals(False)
            self.server_tree.blockSignals(False)
            self._splash.close()
            raise ex
        
    def load_server_list(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(self._profile[u'host'], username=self._profile[u'user'], 
                        key_filename=self._profile[u'key'] if self._profile[u'key'] else None)
        except socket.error as ex:
            self._splash.close()
            raise ex
        
        _, stdout, stderr = ssh.exec_command('cat %s' % self._profile['file'])
        error = stderr.read()
        if error:
            raise NameError(error)
        schema_file = open('media/servers-schema-1.0.json', 'r')
        schema = json.load(schema_file)
        schema_file.close()
        self._servers = json.load(stdout)
        validate(self._servers, schema)
        ssh.close()
        
        self.server_tree.blockSignals(True)
        self._items = {}
        while self.server_tree.topLevelItemCount() > 0:
            self.server_tree.takeTopLevelItem(0)
        for group, servers in self._servers[u'servers'].items():
            group_item = self.add_server_tree_item(group)
            for server_name, server in servers.items():
                server_item = self.add_server_tree_item(server_name, group_item)
                for user in server[u'users']:
                    item = self.add_server_tree_item(user, server_item, True)
                    self._items[server_name] = {user: item}          
        self.server_tree.expandAll()
        self.server_tree.blockSignals(False)
        
    def add_server_tree_item(self, label, parent=None, is_leaf=False):
        item = QTreeWidgetItem(parent)
        item.setText(0, unicode(label))
        if is_leaf:
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        self.server_tree.addTopLevelItem(item)
        return item      
            
    def load_key_list(self, action):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          
        total = 1
        for servers in self._servers[u'servers'].values():
            for server in servers.values():
                total += len(server[u'users'])  
        
        i=0
        for servers in self._servers[u'servers'].values():
            for server_name, server in servers.items():
                for user in server[u'users']:
                    i += 1
                    self._splash.setProgress(float(i)/float(total), u'%s %s %s settings...' % (u'Writing' if action == u'commit' else u'Loading', server_name, user))
                    self.load_key_list_from(ssh, server_name, server[u'host'], user, action)
            
        self.reload_key_list()
        
    def reload_key_list(self):
        while self.key_list.count() > 0:
            self.key_list.takeItem(0)
        for key in sorted(self._keys.keys()):
            item = QListWidgetItem(unicode(key))
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)
            item.setData(Qt.UserRole, unicode(key))
            self.key_list.addItem(item)
        
    def load_key_list_from(self, ssh, server_name, host, user, action):
        try:
            ssh.connect(host, username=user, key_filename=self._profile[u'key'] if self._profile[u'key'] else None)
        except:
            ssh.close()
            self.server_tree.blockSignals(True)
            self._items[server_name][user].setDisabled(True)
            self.server_tree.blockSignals(False)
            return
              
        if action == u'commit':
            sftp = ssh.open_sftp()
            keyfile = sftp.open('./.ssh/authorized_keys.new', 'w')

            content = u''
            for keyname, key in self._commit_keys.items():
                if (server_name, user) in key[u'servers']:
                    content += (key[u'full'] + u'\n' )
            keyfile.write(content)
            keyfile.close()
            sftp.close()
            ssh.exec_command('mv ./.ssh/authorized_keys.new ./.ssh/authorized_keys')
        
        _, stdout, _ = ssh.exec_command('cat ./.ssh/authorized_keys')
        for line in stdout.readlines():
            keyline = unicode(line).split(' ')
            if len(keyline) == 3:
                proto = keyline[0].rstrip()
                key = keyline[1].rstrip()
                keyname = keyline[2].rstrip()
                i = 1
                while self._keys.has_key(keyname):
                    if self._keys[keyname][u'proto'] != proto or self._keys[keyname][u'key'] != key:
                        i += 1
                        keyname = keyline[2] + u' (%s)' % i
                    else:
                        if not (server_name, user) in self._keys[keyname][u'servers']:
                            self._keys[keyname][u'servers'].append((server_name, user))
                        break
                        
                if not self._keys.has_key(keyname):
                    self._keys[keyname] = {u'proto' : proto, u'key' : key, u'full' : line.rstrip(), u'servers' : [(server_name, user)]}
        
        ssh.close()
                
    def key_item_selected(self, item):
        if not item:
            return
        
        self.server_tree.blockSignals(True)
        self._selected_key_name = unicode(item.text())
        key = self._keys[self._selected_key_name]
        self.key_edit.setText(key[u'full'])
        for server, users in self._items.items():
            for user, item in users.items():
                if (server, user) in key[u'servers']:
                    item.setCheckState(0, Qt.Checked)
                else:
                    item.setCheckState(0, Qt.Unchecked)
        self.server_tree.blockSignals(False)
        
    def key_item_changed(self, item):
        if unicode(item.text()) != unicode(item.data(Qt.UserRole).toString()):
            self._keys[unicode(item.text())] = self._keys.pop(unicode(item.data(Qt.UserRole).toString()))
            self._keys[unicode(item.text())][u'full'] = '%s %s %s' % (self._keys[unicode(item.text())][u'proto'],
                                                                      self._keys[unicode(item.text())][u'key'],
                                                                      unicode(item.text()))
            item.setData(Qt.UserRole, unicode(item.text()))
                
    def server_item_selected(self, item):
        user = unicode(item.text(0))
        server_name = unicode(item.parent().text(0))
        if item.checkState(0) == Qt.Checked:
            if (server_name, user) not in self._keys[self._selected_key_name][u'servers']:
                self._keys[self._selected_key_name][u'servers'].append((server_name, user))
        else:
            if (server_name, user) in self._keys[self._selected_key_name][u'servers']:
                self._keys[self._selected_key_name][u'servers'].remove((server_name, user))
     
    def commit(self):
        self.load(u'commit')
        
    def import_key(self):
        add_key_dialog = AddKeyDialog()
        add_key_dialog.exec_()
        new_key = add_key_dialog.key()
        if new_key:
            self._keys[new_key['keyname']] = {
                u'proto' : new_key['proto'], 
                u'key' : new_key['key'], 
                u'full' : new_key['full'], 
                u'servers' : []
            }
            item = QListWidgetItem(unicode(new_key[u'keyname']))
            self.key_list.addItem(item)
            self.key_list.sortItems()
            item.setSelected(True)
            self.key_item_selected(item)

    def remove_key(self):
        del self._keys[self._selected_key_name]
        self.reload_key_list()
    
        item = self.key_list.item(0)
        item.setSelected(True)
        self.key_item_selected(item)
        
    def reload_profiles(self):
        if self._reload_profiles:
            self._reload_profiles = False
            return True
        return False
        
    def open_profiles(self):
        self._reload_profiles = True
        self.close()

    def about(self):
        QMessageBox.about(self.parent(), u"About SSH key manager", 
                          u"<big><b>SSH key manager</b></big><br/><i>v1.0_alpha1</i><br/><br/>" + 
                          u"<b>Author:</b>" + u"<br/>Hervé Martinet<br/><br/>" +
                          u'<b>Splashscreen Photo:</b><br/>Joel Bennett<br/><a href="http://www.flickr.com/photos/jaykul/">http://www.flickr.com/photos/jaykul/</a>' +
                          u'<br/><i>licensed under a Creative Commons (CC BY-NC-SA 2.0)</i><br/><br/>' +
                          u'<b>Icon Set:</b><br/>Default Icon by interactivemania<br/><a href="http://www.defaulticon.com/">http://www.defaulticon.com/</a>' +
                          u'<br/><i>licensed under a Creative Commons (CC BY-ND 3.0)</i>') 
