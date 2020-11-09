# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 424)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 501, 121))
        self.groupBox.setObjectName("groupBox")
        self.label_time = QtWidgets.QLabel(self.groupBox)
        self.label_time.setGeometry(QtCore.QRect(25, 70, 130, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.label_dir = QtWidgets.QLabel(self.groupBox)
        self.label_dir.setGeometry(QtCore.QRect(25, 30, 130, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dir.setFont(font)
        self.label_dir.setObjectName("label_dir")
        self.lineEdit_dir = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_dir.setGeometry(QtCore.QRect(168, 28, 230, 21))
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.lineEdit_time = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_time.setGeometry(QtCore.QRect(168, 68, 70, 21))
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.pushButton_sure = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sure.setGeometry(QtCore.QRect(390, 65, 92, 25))
        self.pushButton_sure.setAutoFillBackground(True)
        self.pushButton_sure.setObjectName("pushButton_sure")
        self.pushButton_option = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_option.setGeometry(QtCore.QRect(422, 27, 60, 25))
        self.pushButton_option.setObjectName("pushButton_option")
        self.label_tips = QtWidgets.QLabel(self.groupBox)
        self.label_tips.setGeometry(QtCore.QRect(250, 70, 130, 15))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(9)
        self.label_tips.setFont(font)
        self.label_tips.setObjectName("label_tips")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 160, 501, 201))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_left = QtWidgets.QWidget()
        self.tab_left.setObjectName("tab_left")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_left)
        self.tableWidget.setGeometry(QtCore.QRect(7, 7, 480, 160))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab_left, "")
        self.tab_right = QtWidgets.QWidget()
        self.tab_right.setObjectName("tab_right")
        self.listWidget = QtWidgets.QListWidget(self.tab_right)
        self.listWidget.setGeometry(QtCore.QRect(7, 7, 480, 160))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_right, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RCQ读者书库--读书使人进步"))
        self.groupBox.setTitle(_translate("MainWindow", "抓取设置"))
        self.label_time.setText(_translate("MainWindow", "请选择抓取期数:"))
        self.label_dir.setText(_translate("MainWindow", "请选择保存路径:"))
        self.lineEdit_time.setText(_translate("MainWindow", "2019-12"))
        self.pushButton_sure.setText(_translate("MainWindow", "确定"))
        self.pushButton_option.setText(_translate("MainWindow", "选择"))
        self.label_tips.setText(_translate("MainWindow", "(期数范围 01-24)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "期数"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名称"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_left), _translate("MainWindow", "按期数显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_right), _translate("MainWindow", "按名称显示"))
