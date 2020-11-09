# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import requests
from lxml import etree
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 设置抓取区域
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 570, 131))
        self.groupBox.setObjectName("groupBox")
        # 设置标签目录
        self.label_dir = QtWidgets.QLabel(self.groupBox)
        self.label_dir.setGeometry(QtCore.QRect(35, 35, 125, 25))
        self.label_dir.setObjectName("label_dir")
        # 设置标签期刊
        self.label_month = QtWidgets.QLabel(self.groupBox)
        self.label_month.setGeometry(QtCore.QRect(35, 80, 125, 25))
        self.label_month.setObjectName("label_month")
        # 设置标签提示
        self.label_tips = QtWidgets.QLabel(self.groupBox)
        self.label_tips.setGeometry(QtCore.QRect(280, 80, 135, 25))
        self.label_tips.setObjectName("label_tips")
        # 单行目录输入框
        self.lineEdit_dir = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_dir.setGeometry(QtCore.QRect(170, 35, 250, 25))
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        # 单行页数输入框
        self.lineEdit_page = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_page.setGeometry(QtCore.QRect(170, 80, 90, 25))
        self.lineEdit_page.setObjectName("lineEdit_page")
        # 设置 选择 按钮
        self.pushButton_option = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_option.setGeometry(QtCore.QRect(445, 32, 95, 30))
        self.pushButton_option.setMouseTracking(False)
        self.pushButton_option.setAutoFillBackground(True)
        self.pushButton_option.setObjectName("pushButton_option")
        # 设置 确定 按钮
        self.pushButton_sure = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sure.setGeometry(QtCore.QRect(445, 76, 95, 30))
        self.pushButton_sure.setMouseTracking(False)
        self.pushButton_sure.setAutoFillBackground(True)
        # self.pushButton_sure.setFlat(False) # 设置背景
        self.pushButton_sure.setObjectName("pushButton_sure")

        # 设置tab选项卡
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 160, 570, 391))
        self.tabWidget.setObjectName("tabWidget")
        # 设置左标签
        self.tab_left = QtWidgets.QWidget()
        self.tab_left.setObjectName("tab_left")
        # 设置 QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.tab_left)
        self.tableWidget.setGeometry(QtCore.QRect(7, 7, 550, 350))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(0, 130)  # 设置第一列宽度
        # 设置自动填充容器
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 垂直滚动条
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabWidget.addTab(self.tab_left, "")
        # 设置第二个tab
        self.tab_right = QtWidgets.QWidget()
        self.tab_right.setObjectName("tab_right")
        # 对listWidget 进行设置
        self.listWidget = QtWidgets.QListWidget(self.tab_right)
        self.listWidget.setGeometry(QtCore.QRect(7, 7, 550, 350))
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_right, "")
        self.listWidget.setIconSize(QtCore.QSize(72, 72))  # 图标大小
        self.listWidget.setMaximumWidth(800)  # 最大宽度
        self.listWidget.setSpacing(12)  # 间距大小
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        # 设置窗体的底部状态栏
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 默认值在这里设置
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "读者书库——阅读使人进步"))
        self.groupBox.setTitle(_translate("MainWindow", "抓取设置"))
        self.label_dir.setText(_translate("MainWindow", "请选择保存路径:"))
        self.label_month.setText(_translate("MainWindow", "请选择抓取页数:"))
        self.lineEdit_dir.setText(_translate("MainWindow", os.getcwd()))
        self.label_tips.setText(_translate("MainWindow", "(0开头代表总页数)"))
        self.lineEdit_page.setText(_translate('MainWindow', '1'))
        self.pushButton_option.setText(_translate("MainWindow", "选择"))
        self.pushButton_sure.setText(_translate("MainWindow", "确定"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "期数"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名称"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_left), _translate("MainWindow", "按日期显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_right), _translate("MainWindow", "按名称显示"))
        self.pushButton_sure.clicked.connect(self.getpage)  # 获取数据
        self.pushButton_option.clicked.connect(self.msg)  # 为选择按钮绑定事件


    # 获取详情页
    def page_info(self, page_list):
        self.table_list = []
        for i in page_list:
            response = requests.get(i)
            response.encoding = 'gb18030'
            html = response.text
            tree_ele = etree.HTML(html)
            # 标题
            title = tree_ele.xpath('/html/body/div[2]/div[1]/div[2]/h1/text()')[0]
            # 时间
            time_author = tree_ele.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/text()')
            self.date = time_author[0].split('\u3000')[0].strip().split(':')[-1]
            author = time_author[0].split('\u3000')[1]
            self.table_list.append(self.date)
            self.table_list.append(title)
            # 内容 由于文章为两种路径, 所以做了个判断
            result = tree_ele.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/p/text()')
            if result == []:
                result = tree_ele.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/text()')
            # 存储文件夹
            path = self.lineEdit_dir.text() + '\\' + 'reader_library' + '\\' + self.date
            if not os.path.exists(path):
                os.makedirs(path)
            file = open(path + '\\' + title + '.txt', 'w', encoding='gb18030')
            file.write('<<' + title + '>>\n')
            file.write('作者:' + author + '>\n\n')
            for i in result:
                file.write(i)
            file.close()

    # 选择保存路径
    def msg(self):
        try:
            self.dir_path = QFileDialog.getExistingDirectory(None, '选择路径', os.getcwd())
            self.lineEdit_dir.setText(self.dir_path)
        except Exception as e:
            print(e)

    def show_table(self):
        for k in range(int(len(self.table_list)/2)):
            # 添加行
            self.tableWidget.insertRow(k)
            # 设置第一列
            self.tableWidget.setItem(k, 0, QtWidgets.QTableWidgetItem(self.table_list[k*2]))
            # 设置第二列
            self.tableWidget.setItem(k, 1, QtWidgets.QTableWidgetItem(self.table_list[k*2+1]))

    #将文件显示在List列表中
    def show_list(self):
        for i in range(int(len(self.table_list) / 2)):
            # 创建列表项
            self.item = QtWidgets.QListWidgetItem(self.listWidget)  # 创建列表项
            self.item.setIcon(QtGui.QIcon('note.ico'))  # 设置列表项图标
            self.item.setText(self.table_list[i*2+1][0:5] + '..')  # 截取字符串，只显示5个字符
            self.item.setToolTip(str(i))  # 设置提示文字
            self.item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # 设置选中与否

    def search_title(self, item):
        str_i = int(item.toolTip())
        title = self.table_list[str_i*2+1]
        dir_date = self.table_list[str_i*2]
        return title, dir_date

    # 列表单击方法，用来打开选中的项
    def itemClick(self, item):
        title, dir_date = self.search_title(item)
        os.startfile(self.lineEdit_dir.text() + '\\reader_library\\' + dir_date + '\\' + title + '.txt')

    # 表格单击方法，用来打开选中的项
    def tableClick(self, item):
        pass

    def getpage(self):
        num = self.lineEdit_page.text()
        if num.startswith('0') == False and num.isdigit():
            base_url = 'http://www.rensheng5.com/duzhewenzhai/list_{}.html'.format(num)
            response = requests.get(base_url)
            html = response.text
            tree_ele = etree.HTML(html)
            result = tree_ele.xpath('//body/div[2]/div/ul/li/a/@href')
            self.page_info(result)

        elif num.startswith('0') and int(num) <= 1054:
            for i in range(1, int(num)+1):
                base_url = 'http://www.rensheng5.com/duzhewenzhai/list_{}.html'.format(i)
                response = requests.get(base_url)
                html = response.text
                tree_ele = etree.HTML(html)
                result = tree_ele.xpath('//body/div[2]/div/ul/li/a/@href')
                self.page_info(result)
        else:
            pass
        QMessageBox.information(None, '提示:', '您需要的读者文章保存完成', QMessageBox.Ok)

        self.show_list()  # 对列表进行绑定
        self.show_table()  # 对表格进行绑定
        self.listWidget.itemClicked.connect(self.itemClick)  # 绑定列表单击方法
        self.tableWidget.itemClicked.connect(self.tableClick)  # 绑定表格单击方法

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()    # 创建窗体对象
    ui = Ui_MainWindow()    # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show()   # 显示窗体
    sys.exit(app.exec_())   # 程序关闭时退出进程