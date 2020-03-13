# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from LedIndicatorWidget import LedIndicator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 711, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.led7 = LedIndicator(color='red')
        self.gridLayout.addWidget(self.led7, 1, 2, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 540, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.fill_box)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 540, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 540, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 540, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 200, 711, 311))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 709, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.textBox = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textBox.setAlignment(QtCore.Qt.AlignBottom)
        self.textBox.setGeometry(QtCore.QRect(0, 0, 711, 311))
        self.textBox.setText("Initializing ...\n")
        self.textBox.moveCursor(QtGui.QTextCursor.End)
        self.textBox.show()

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 540, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Fucking")
        self.comboBox.addItem("Carlos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 21))
        self.menubar.setObjectName("menubar")
        self.menuRelialok = QtWidgets.QMenu(self.menubar)
        self.menuRelialok.setObjectName("menuRelialok")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuRelialok.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#        self.label_7.setText(_translate("MainWindow", "TextLabel23"))
        self.label_5.setText(_translate("MainWindow", "TextLabel21"))
        self.label.setText(_translate("MainWindow", "TextLabel12"))
        self.label_8.setText(_translate("MainWindow", "TextLabel24"))
        self.label_2.setText(_translate("MainWindow", "TextLabel11"))
        self.label_6.setText(_translate("MainWindow", "TextLabel22"))
        self.label_3.setText(_translate("MainWindow", "TextLabel13"))
        self.label_4.setText(_translate("MainWindow", "TextLabel14"))
        self.pushButton.setText(_translate("MainWindow", "Stop"))
        self.pushButton_2.setText(_translate("MainWindow", "Connect"))
        self.pushButton_3.setText(_translate("MainWindow", "Status"))
        self.pushButton_4.setText(_translate("MainWindow", "Initialize"))
        self.comboBox.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "COM2"))
        self.menuRelialok.setTitle(_translate("MainWindow", "Relialok"))

    def add_text(self, number):
        self.textBox.append("{number}\n".format(number=number))

    def fill_box(self):
        for i in range(1, 1000):
            self.add_text(i)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
