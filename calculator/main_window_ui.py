# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Thu Jul 25 17:29:31 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setStyleSheet("QPushButton {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 3, 0, 1, 1)
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy)
        self.btn_point.setStyleSheet("QPushButton {\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #bebebe, stop: 1 #d7d7d7);\n"
"}")
        self.btn_point.setObjectName("btn_point")
        self.gridLayout.addWidget(self.btn_point, 5, 1, 1, 1)
        self.btn_subtract = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_subtract.sizePolicy().hasHeightForWidth())
        self.btn_subtract.setSizePolicy(sizePolicy)
        self.btn_subtract.setStyleSheet("QPushButton {\n"
"    border: 1px solid gary;\n"
"    color: white;\n"
"    background-color: rgb(255, 151, 57);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #ff7832, stop: 1 #ff9739);\n"
"}\n"
"")
        self.btn_subtract.setObjectName("btn_subtract")
        self.gridLayout.addWidget(self.btn_subtract, 3, 3, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setStyleSheet("QPushButton {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setStyleSheet("QPushButton {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 4, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setStyleSheet("QPushButton {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 3, 1, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setStyleSheet("QPushButton {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 5, 0, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setStyleSheet("QPushButton {\n"
"    border: 1px solid gary;\n"
"    color: white;\n"
"    background-color: rgb(255, 151, 57);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #ff7832, stop: 1 #ff9739);\n"
"}\n"
"")
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 4, 3, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setStyleSheet("QPushButton {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 3, 2, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setStyleSheet("QPushButton {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setStyleSheet("QPushButton {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setStyleSheet("QPushButton {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 4, 2, 1, 1)
        self.output_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_line.sizePolicy().hasHeightForWidth())
        self.output_line.setSizePolicy(sizePolicy)
        self.output_line.setAutoFillBackground(False)
        self.output_line.setStyleSheet("QWidget{\n"
"    font: 35px;\n"
"    qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"    border: 1px solid gray;\n"
"}")
        self.output_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.output_line.setCursorPosition(1)
        self.output_line.setReadOnly(True)
        self.output_line.setObjectName("output_line")
        self.gridLayout.addWidget(self.output_line, 0, 0, 1, 4)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setStyleSheet("QPushButton {\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 4, 0, 1, 1)
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_divide.sizePolicy().hasHeightForWidth())
        self.btn_divide.setSizePolicy(sizePolicy)
        self.btn_divide.setAutoFillBackground(False)
        self.btn_divide.setStyleSheet("QPushButton {\n"
"    border: 1px solid gary;\n"
"    color: white;\n"
"    background-color: rgb(255, 151, 57);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #ff7832, stop: 1 #ff9739);\n"
"}\n"
"")
        self.btn_divide.setAutoDefault(False)
        self.btn_divide.setDefault(False)
        self.btn_divide.setFlat(False)
        self.btn_divide.setObjectName("btn_divide")
        self.gridLayout.addWidget(self.btn_divide, 1, 3, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy)
        self.btn_equal.setStyleSheet("QPushButton {\n"
"    border: 1px solid gary;\n"
"    color: white;\n"
"    background-color: rgb(255, 151, 57);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #ff7832, stop: 1 #ff9739);\n"
"}\n"
"")
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout.addWidget(self.btn_equal, 5, 2, 1, 2)
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_multiply.sizePolicy().hasHeightForWidth())
        self.btn_multiply.setSizePolicy(sizePolicy)
        self.btn_multiply.setStyleSheet("QPushButton {\n"
"    border: 1px solid gary;\n"
"    color: white;\n"
"    background-color: rgb(255, 151, 57);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #ff7832, stop: 1 #ff9739);\n"
"}\n"
"")
        self.btn_multiply.setObjectName("btn_multiply")
        self.gridLayout.addWidget(self.btn_multiply, 2, 3, 1, 1)
        self.btn_percent = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_percent.sizePolicy().hasHeightForWidth())
        self.btn_percent.setSizePolicy(sizePolicy)
        self.btn_percent.setAutoFillBackground(False)
        self.btn_percent.setStyleSheet("QPushButton {\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #bebebe, stop: 1 #d7d7d7);\n"
"}")
        self.btn_percent.setAutoDefault(False)
        self.btn_percent.setDefault(False)
        self.btn_percent.setFlat(False)
        self.btn_percent.setObjectName("btn_percent")
        self.gridLayout.addWidget(self.btn_percent, 1, 2, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setAutoFillBackground(False)
        self.btn_clear.setStyleSheet("QPushButton {\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #bebebe, stop: 1 #d7d7d7);\n"
"}")
        self.btn_clear.setAutoDefault(False)
        self.btn_clear.setDefault(False)
        self.btn_clear.setFlat(False)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 1, 0, 1, 1)
        self.inversion_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inversion_btn.sizePolicy().hasHeightForWidth())
        self.inversion_btn.setSizePolicy(sizePolicy)
        self.inversion_btn.setAutoFillBackground(False)
        self.inversion_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(215, 215, 215);\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #bebebe, stop: 1 #d7d7d7);\n"
"}")
        self.inversion_btn.setAutoDefault(False)
        self.inversion_btn.setDefault(False)
        self.inversion_btn.setFlat(False)
        self.inversion_btn.setObjectName("inversion_btn")
        self.gridLayout.addWidget(self.inversion_btn, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.btn_4.setText(QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        self.btn_point.setText(QtWidgets.QApplication.translate("MainWindow", ".", None, -1))
        self.btn_subtract.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.btn_3.setText(QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.btn_8.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.btn_5.setText(QtWidgets.QApplication.translate("MainWindow", "5", None, -1))
        self.btn_0.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.btn_add.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.btn_6.setText(QtWidgets.QApplication.translate("MainWindow", "6", None, -1))
        self.btn_2.setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.btn_1.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.btn_9.setText(QtWidgets.QApplication.translate("MainWindow", "9", None, -1))
        self.output_line.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.btn_7.setText(QtWidgets.QApplication.translate("MainWindow", "7", None, -1))
        self.btn_divide.setText(QtWidgets.QApplication.translate("MainWindow", "/", None, -1))
        self.btn_equal.setText(QtWidgets.QApplication.translate("MainWindow", "=", None, -1))
        self.btn_multiply.setText(QtWidgets.QApplication.translate("MainWindow", "*", None, -1))
        self.btn_percent.setText(QtWidgets.QApplication.translate("MainWindow", "%", None, -1))
        self.btn_clear.setText(QtWidgets.QApplication.translate("MainWindow", "AC", None, -1))
        self.inversion_btn.setText(QtWidgets.QApplication.translate("MainWindow", "+/-", None, -1))

