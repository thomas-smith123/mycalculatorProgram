# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myprogram.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(1048, 834)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Calculator)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Calculator)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(11, 11, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(680, 50, 139, 57))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_1.setObjectName("radioButton_1")
        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 222, 711))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.page1Cal = QtWidgets.QPushButton(self.tab)
        self.page1Cal.setGeometry(QtCore.QRect(680, 120, 121, 41))
        self.page1Cal.setObjectName("page1Cal")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(120, 140, 61, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(180, 210, 671, 541))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_2.addWidget(self.textBrowser_2)
        self.lineEdit_epsilon = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_epsilon.setGeometry(QtCore.QRect(230, 140, 51, 41))
        self.lineEdit_epsilon.setObjectName("lineEdit_epsilon")
        self.lineEdit_Fl = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Fl.setGeometry(QtCore.QRect(320, 140, 101, 41))
        self.lineEdit_Fl.setObjectName("lineEdit_Fl")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(220, 110, 72, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(340, 110, 71, 21))
        self.label_15.setObjectName("label_15")
        self.lineEdit_Fu = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Fu.setGeometry(QtCore.QRect(470, 140, 101, 41))
        self.lineEdit_Fu.setObjectName("lineEdit_Fu")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(490, 110, 71, 20))
        self.label_16.setObjectName("label_16")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(50, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(230, 120, 361, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.gridLayout.addWidget(self.plainTextEdit_8, 4, 2, 1, 1)
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.gridLayout.addWidget(self.plainTextEdit_7, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout.addWidget(self.plainTextEdit_3, 2, 1, 1, 1)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.gridLayout.addWidget(self.plainTextEdit_4, 2, 2, 1, 1)
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.gridLayout.addWidget(self.plainTextEdit_6, 3, 2, 1, 1)
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.gridLayout.addWidget(self.plainTextEdit_5, 3, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(380, 550, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(380, 460, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(210, 520, 481, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(170, 250, 621, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Calculator)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "你大哥的小程序"))
        self.label.setText(_translate("Calculator", "G Parameter Calculate"))
        self.radioButton_1.setText(_translate("Calculator", "Butterworth"))
        self.radioButton_2.setText(_translate("Calculator", "Cheby"))
        self.label_2.setText(_translate("Calculator", "Order:"))
        self.label_3.setText(_translate("Calculator", "Result:"))
        self.label_13.setText(_translate("Calculator", "EVEN/ODD \n"
"Resistance:"))
        self.page1Cal.setText(_translate("Calculator", "Calculate"))
        self.label_14.setText(_translate("Calculator", "Epsilon"))
        self.label_15.setText(_translate("Calculator", "Fl(MHz)"))
        self.label_16.setText(_translate("Calculator", "Fu(MHz)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Calculator", "Function1"))
        self.label_4.setText(_translate("Calculator", "StableFactor"))
        self.label_5.setText(_translate("Calculator", "S parameter"))
        self.label_9.setText(_translate("Calculator", "S22"))
        self.label_8.setText(_translate("Calculator", "S12"))
        self.label_6.setText(_translate("Calculator", "S21"))
        self.label_7.setText(_translate("Calculator", "S11"))
        self.label_10.setText(_translate("Calculator", "Mag"))
        self.label_11.setText(_translate("Calculator", "Ang"))
        self.pushButton.setText(_translate("Calculator", "Cal"))
        self.label_12.setText(_translate("Calculator", "K="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Calculator", "Function2"))
        self.label_18.setText(_translate("Calculator", "本程序由我独家开发，版本还有很多bug，后续还将继续改进，谢谢！"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Calculator", "Graph"))

