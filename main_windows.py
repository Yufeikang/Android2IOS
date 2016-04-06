# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_windows.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 921, 511))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_IOS = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_IOS.setObjectName("listWidget_IOS")
        self.horizontalLayout.addWidget(self.listWidget_IOS)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 0, 5, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.listWidget_Android = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_Android.setObjectName("listWidget_Android")
        self.horizontalLayout.addWidget(self.listWidget_Android)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 921, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_XML = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_XML.setObjectName("menuOpen_XML")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAndroid_src = QtWidgets.QAction(MainWindow)
        self.actionAndroid_src.setObjectName("actionAndroid_src")
        self.actionAndroid_dist = QtWidgets.QAction(MainWindow)
        self.actionAndroid_dist.setObjectName("actionAndroid_dist")
        self.actionOpen_IOS_Setting = QtWidgets.QAction(MainWindow)
        self.actionOpen_IOS_Setting.setObjectName("actionOpen_IOS_Setting")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuOpen_XML.addAction(self.actionAndroid_src)
        self.menuOpen_XML.addAction(self.actionAndroid_dist)
        self.menuFile.addAction(self.menuOpen_XML.menuAction())
        self.menuFile.addAction(self.actionOpen_IOS_Setting)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "IOS String List："))
        self.label_2.setText(_translate("MainWindow", "Android String List"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_XML.setTitle(_translate("MainWindow", "Open XML"))
        self.actionAndroid_src.setText(_translate("MainWindow", "Android src"))
        self.actionAndroid_dist.setText(_translate("MainWindow", "Android dist"))
        self.actionOpen_IOS_Setting.setText(_translate("MainWindow", "Open IOS String"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

