# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python\SVG_view\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_path_base = QtWidgets.QLineEdit(self.centralwidget)
        self.le_path_base.setObjectName("le_path_base")
        self.verticalLayout.addWidget(self.le_path_base)
        self.le_path = QtWidgets.QLineEdit(self.centralwidget)
        self.le_path.setObjectName("le_path")
        self.verticalLayout.addWidget(self.le_path)
        self.tbl = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl.setObjectName("tbl")
        self.tbl.setColumnCount(0)
        self.tbl.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl)
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setObjectName("btn_ok")
        self.verticalLayout.addWidget(self.btn_ok)
        self.le_name = QtWidgets.QLineEdit(self.centralwidget)
        self.le_name.setObjectName("le_name")
        self.verticalLayout.addWidget(self.le_name)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.le_path_base.setPlaceholderText(_translate("MainWindow", "папка с иконками"))
        self.le_path.setPlaceholderText(_translate("MainWindow", "путь для сохранения"))
        self.btn_ok.setText(_translate("MainWindow", "ОК"))
        self.le_name.setPlaceholderText(_translate("MainWindow", "имя новго файла"))