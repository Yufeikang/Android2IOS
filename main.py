#!/usr/bin/env python3
# encoding: utf-8


"""
@version: 1.0
@author: kang
@license: Apache Licence 
@contact: kyf0722@gmail.com
@site: http://www.kangyufei.net
@software: PyCharm
@file: main.py
@time: 4/5/2016 19:21
@description: main
"""
import os
import difflib
from PyQt5.QtGui import QIcon
import image_rc
from main_windows import Ui_MainWindow
from PyQt5.QtWidgets import *
from parses_string import *


class MainWindows(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.cur_ios_item = None
        self.ios_string_file_context = ''
        self.ios_string_dict = {}
        self.android_string_src = {}
        self.android_string_dist = {}
        self.save_filename = None
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.actionExit.triggered.connect(self.close)
        self.actionAndroid_dist.triggered.connect(self.open_android_dist)
        self.actionAndroid_src.triggered.connect(self.open_android_src)
        self.actionOpen_IOS_Setting.triggered.connect(self.open_ios_file)
        self.actionSave.triggered.connect(self.save)
        self.actionSave.setShortcut('Ctrl+S')
        self.setWindowIcon(QIcon(':img/main.ico'))

    def open_ios_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select IOS String File", os.getcwd(),
                                                  "IOS Strings Files (*.strings);;ALL Files (*)")
        self.statusbar.showMessage('Open Successful :%s' % filename)
        if filename:
            try:
                self.ios_string_dict, self.ios_string_file_context = parses_strings(filename)
            except Exception as err:
                self.statusbar.showMessage('open_ios_file ERROR:%s' % err)
                return
            if self.android_string_dist.__len__() < 1:
                if not self.open_android_dist():
                    self.statusbar.showMessage('open_android_dist ERROR:')
                    return
            if self.android_string_src.__len__() < 1:
                if not self.open_android_src():
                    self.statusbar.showMessage('open_android_src ERROR:')
                    return
            self.display_data()

    def open_android_src(self):
        filename_list, ok = QFileDialog.getOpenFileNames(self, "Select android src String File", os.getcwd(),
                                                         "XML Files (*.xml);;ALL Files (*)")

        self.statusbar.showMessage('Open Successful :%s' % filename_list)
        if ok:
            try:
                self.android_string_src = parses_xml(filename_list)
                return True
            except Exception as err:
                self.statusbar.showMessage('open_android_src ERROR:%s' % err)
                return False
        else:
            return False

    def open_android_dist(self):
        filename_list, ok = QFileDialog.getOpenFileNames(self, "Select Android Dist String File", os.getcwd(),
                                                         "XML Files (*.xml);;ALL Files (*)")
        self.statusbar.showMessage('Open Successful :%s' % filename_list)
        if ok:
            try:
                self.android_string_dist = parses_xml(filename_list)
                return True
            except Exception as err:
                self.statusbar.showMessage('open_android_dist ERROR:%s' % err)
                return False
        else:
            return False

    def display_data(self):
        self.listWidget_IOS.clear()
        for k in self.ios_string_dict.keys():
            item = QListWidgetItem(QIcon(':img/xcode.png'), self.ios_string_dict[k], self.listWidget_IOS, 0)
            item.setToolTip('The key ID :%s' % k)
            item.setStatusTip(k)
            self.listWidget_IOS.addItem(item)
        self.listWidget_IOS.itemDoubleClicked.connect(self.ios_item_clicked)
        self.listWidget_IOS.currentItemChanged.connect(self.ios_item_end_edit)
        self.listWidget_IOS.itemChanged.connect(self.ios_item_change)
        self.listWidget_IOS.itemClicked.connect(self.search_from_android)
        self.listWidget_IOS.sortItems()

    def ios_item_clicked(self, item=QListWidgetItem()):
        self.listWidget_IOS.openPersistentEditor(item)

    def ios_item_end_edit(self, item_cur, item_pre):
        self.listWidget_IOS.closePersistentEditor(item_pre)

    def ios_item_change(self, item=QListWidgetItem):
        value = item.text()
        key = item.statusTip()
        self.ios_string_dict[key] = value
        self.sync_ios_dict_to_context()

    def sync_ios_dict_to_context(self):
        self.ios_string_file_context = sync_ios_dict_to_context(self.ios_string_dict, self.ios_string_file_context)

    def search_from_android(self, item=QListWidgetItem):
        value = item.text()
        key = item.statusTip()
        self.cur_ios_item = item
        result_list = []
        s = difflib.SequenceMatcher()
        for android_str_key in self.android_string_src.keys():
            s.set_seqs(value, self.android_string_src[android_str_key])
            if s.ratio() > 0.5:
                try:
                    dist_str = self.android_string_dist[android_str_key]
                except:
                    dist_str = 'null'
                result_list.append((android_str_key, dist_str, self.android_string_src[android_str_key]))
        self.listWidget_Android.clear()
        for k, dist, src in result_list:
            android_item = QListWidgetItem(QIcon(':img/android.png'), dist, self.listWidget_Android, 0)
            android_item.setToolTip('src :%s' % src)
            android_item.setStatusTip(k)
            self.listWidget_Android.addItem(android_item)
        self.listWidget_Android.itemDoubleClicked.connect(self.android_item_doubleClicked)

    def android_item_doubleClicked(self, item):
        self.cur_ios_item.setText(item.text())

    def save(self):
        if len(self.ios_string_file_context) < 1:  # ios string 内容存在 需要保存
            return
        if self.save_filename is None:
            self.save_filename, _ = QFileDialog.getSaveFileName(self, "Save IOS String File", os.getcwd(),
                                                                "IOS Strings Files (*.strings);;ALL Files (*)")
        f = open(self.save_filename, 'w', encoding='utf-8')
        f.write(self.ios_string_file_context)
        f.close()
        self.statusbar.showMessage('Save Ok!')

    def closeEvent(self, *args, **kwargs):
        super().closeEvent(*args, **kwargs)
        self.close()

    def close(self):
        ok = QMessageBox.question(self, 'Info', 'Save?', QMessageBox.Save | QMessageBox.No)
        if ok == QMessageBox.Save:
            self.save()
        sys.exit(0)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app_show = MainWindows()
    app_show.show()
    sys.exit(app.exec_())
