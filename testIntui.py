# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/liss/PycharmProjects/untitled/vk_player/testIntui.ui'
#
# Created: Fri Mar 25 21:28:04 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(340, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 341, 101))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.prevButton = QtGui.QPushButton(self.groupBox)
        self.prevButton.setGeometry(QtCore.QRect(20, 20, 21, 24))
        self.prevButton.setObjectName(_fromUtf8("prevButton"))
        self.playButton = QtGui.QPushButton(self.groupBox)
        self.playButton.setGeometry(QtCore.QRect(50, 20, 21, 24))
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.nextButton = QtGui.QPushButton(self.groupBox)
        self.nextButton.setGeometry(QtCore.QRect(80, 20, 21, 24))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 221, 23))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalSlider = QtGui.QSlider(self.groupBox)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 60, 321, 23))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 100, 341, 461))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 321, 391))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenFile_s = QtGui.QAction(MainWindow)
        self.actionOpenFile_s.setObjectName(_fromUtf8("actionOpenFile_s"))
        self.menuFile.addAction(self.actionOpenFile_s)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.prevButton.setText(_translate("MainWindow", "<<", None))
        self.playButton.setText(_translate("MainWindow", ">", None))
        self.nextButton.setText(_translate("MainWindow", ">>", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Плейлист", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionOpenFile_s.setText(_translate("MainWindow", "OpenFile(s)", None))

