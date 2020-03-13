# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import serial
import serial.tools.list_ports
import time
import _thread

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from LedIndicatorWidget import LedIndicator

class Ui_MainWindow(object):
    def __init__(self):
        self.serial = serial.Serial()
        self.com_set = False
        self.continue_query = True
        self.resource_free = True
        self.port = []
        self.com_ports = [comport.device for comport in serial.tools.list_ports.comports()]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 725)
        MainWindow.setMinimumSize(QtCore.QSize(933, 725))
        MainWindow.setMaximumSize(QtCore.QSize(934, 726))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 650, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 650, 75, 23))
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setObjectName("pushButton_2")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 240, 881, 381))
        self.textEdit.setObjectName("textEdit")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 160, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(759, 30, 141, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 3, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget_2)
        self.widget.setObjectName("widget")

        self.led_25 = LedIndicator(color='blue')
        self.gridLayout_2.addWidget(self.led_25, 0, 0, 1, 1)
        self.led_25.setGeometry(QtCore.QRect(40, 0, 61, 31))
        self.led_25.setObjectName("led_25")
        self.led_25.setChecked(not self.led_25.isChecked())

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 190, 721, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 29, 721, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setSpacing(20)

        # Fault 1
        self.led_24 = LedIndicator(color = 'red')
        self.led_24.setObjectName("led_24")
        self.horizontalLayout.addWidget(self.led_24)
        self.led_24.setChecked(False)

        # Fault 2
        self.led_23 = LedIndicator(color = 'red')
        self.led_23.setObjectName("led_23")
        self.horizontalLayout.addWidget(self.led_23)
        self.led_23.setChecked(False)

        # Fault 3
        self.led_22 = LedIndicator(color = 'red')
        self.led_22.setObjectName("led_22")
        self.horizontalLayout.addWidget(self.led_22)
        self.led_22.setChecked(False)

        # Fault 4
        self.led_21 = LedIndicator(color = 'red')
        self.led_21.setObjectName("led_21")
        self.horizontalLayout.addWidget(self.led_21)
        self.led_21.setChecked(False)

        # Fault 5
        self.led_20 = LedIndicator(color = 'red')
        self.led_20.setObjectName("led_20")
        self.horizontalLayout.addWidget(self.led_20)
        self.led_20.setChecked(False)

        # Fault 6
        self.led_19 = LedIndicator(color = 'red')
        self.led_19.setObjectName("led_19")
        self.horizontalLayout.addWidget(self.led_19)
        self.led_19.setChecked(False)

        # Fault 7
        self.led_18 = LedIndicator(color = 'red')
        self.led_18.setObjectName("led_18")
        self.horizontalLayout.addWidget(self.led_18)
        self.led_18.setChecked(False)

        # Fault 8
        self.led_17 = LedIndicator(color = 'red')
        self.led_17.setObjectName("led_17")
        self.horizontalLayout.addWidget(self.led_17)
        self.led_17.setChecked(False)

        # ON-4
        self.led_16 = LedIndicator(color = 'green')
        self.led_16.setObjectName("led_16")
        self.gridLayout_3.addWidget(self.led_16, 1, 3, 1, 1)
        self.led_16.setChecked(False)

        # ON-3
        self.led_15 = LedIndicator(color = 'green')
        self.led_15.setObjectName("led_15")
        self.gridLayout_3.addWidget(self.led_15, 1, 2, 1, 1)
        self.led_15.setChecked(False)

        # ON-2
        self.led_14 = LedIndicator(color = 'green')
        self.led_14.setObjectName("led_14")
        self.gridLayout_3.addWidget(self.led_14, 1, 1, 1, 1)
        self.led_14.setChecked(False)

        # ON-1
        self.led_13 = LedIndicator(color = 'green')
        self.led_13.setObjectName("led_13")
        self.gridLayout_3.addWidget(self.led_13, 1, 0, 1, 1)
        self.led_13.setChecked(False)

        # OFF-1
        self.led_12 = LedIndicator(color = 'red')
        self.led_12.setObjectName("led_12")
        self.gridLayout_3.addWidget(self.led_12, 2, 0, 1, 1)
        self.led_12.setChecked(False)

        # OFF-2
        self.led_11 = LedIndicator(color = 'red')
        self.led_11.setObjectName("led_11")
        self.gridLayout_3.addWidget(self.led_11, 2, 1, 1, 1)
        self.led_11.setChecked(False)

        # OFF-3
        self.led_10 = LedIndicator(color = 'red')
        self.led_10.setObjectName("led_10")
        self.gridLayout_3.addWidget(self.led_10, 2, 2, 1, 1)
        self.led_10.setChecked(False)

        # OFF-4
        self.led_9 = LedIndicator(color = 'red')
        self.led_9.setObjectName("led_9")
        self.gridLayout_3.addWidget(self.led_9, 2, 3, 1, 1)
        self.led_9.setChecked(False)

        # ON-5
        self.led_8 = LedIndicator(color = 'green')
        self.led_8.setObjectName("led_8")
        self.gridLayout_3.addWidget(self.led_8, 1, 4, 1, 1)
        self.led_8.setChecked(False)

        # OFF-5
        self.led_7 = LedIndicator(color = 'red')
        self.led_7.setObjectName("led_7")
        self.gridLayout_3.addWidget(self.led_7, 2, 4, 1, 1)
        self.led_7.setChecked(False)

        # OFF-6
        self.led_6 = LedIndicator(color = 'red')
        self.led_6.setObjectName("led_6")
        self.gridLayout_3.addWidget(self.led_6, 2, 5, 1, 1)
        self.led_6.setChecked(False)

        # ON-6
        self.led_5 = LedIndicator(color = 'green')
        self.led_5.setObjectName("led_5")
        self.gridLayout_3.addWidget(self.led_5, 1, 5, 1, 1)
        self.led_5.setChecked(False)

        # OFF-7
        self.led_4 = LedIndicator(color = 'red')
        self.led_4.setObjectName("led_4")
        self.gridLayout_3.addWidget(self.led_4, 2, 6, 1, 1)
        self.led_4.setChecked(False)

        # ON-7
        self.led_3 = LedIndicator(color = 'green')
        self.led_3.setObjectName("led_3")
        self.gridLayout_3.addWidget(self.led_3, 1, 6, 1, 1)
        self.led_3.setChecked(False)

        # ON-8
        self.led_2 = LedIndicator(color = 'green')
        self.led_2.setObjectName("led_2")
        self.gridLayout_3.addWidget(self.led_2, 1, 7, 1, 1)
        self.led_2.setChecked(False)

        # OFF-8
        self.led = LedIndicator(color = 'red')
        self.led.setObjectName("led")
        self.gridLayout_3.addWidget(self.led, 2, 7, 1, 1)
        self.led.setChecked(False)

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 650, 69, 22))
        self.comboBox.setObjectName("com_ports")
        self.comboBox.addItems(self.com_ports)

        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.label_8, 0, 7, 1, 1)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(420, 160, 321, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 160, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 21))
        self.menubar.setObjectName("menubar")
        self.menuOctolok = QtWidgets.QMenu(self.menubar)
        self.menuOctolok.setObjectName("menuOctolok")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOctolok.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.connect)
        self.pushButton_2.clicked.connect(self._disconnect)
        self.pushButton_4.clicked.connect(self._get_status)
#        self.pushButton_5.clicked.connect(self.)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.pushButton_2.setText(_translate("MainWindow", "Disconnect"))
        self.pushButton_3.setText(_translate("MainWindow", "Extra-Dummy"))
        self.pushButton_4.setText(_translate("MainWindow", "Status"))
        self.pushButton_5.setText(_translate("MainWindow", "Reset"))
        self.pushButton_6.setText(_translate("MainWindow", "Disable"))
        self.label_5.setText(_translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "6"))
        self.label.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_7.setText(_translate("MainWindow", "7"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_8.setText(_translate("MainWindow", "8"))
        self.label_4.setText(_translate("MainWindow", "4"))
        self.label_9.setText(_translate("MainWindow", "Fault"))
        self.menuOctolok.setTitle(_translate("MainWindow", "Octolok"))

    def connect(self):
        self.serial.port = self.comboBox.currentText()
        print('Connecting to ReliaLok on port: {port}\n'.format(port=self.serial.port))
        try:
            self.serial.open()
            self.print_text_box('>>>>> {object}\n'.format(object=self.serial))
            self.print_text_box('Successfully connected to device ...\n')
#            self._get_status()

#           self._listen_thread()
        except serial.serialutil.SerialException:
            self.print_text_box('Could not open connection on {port} ...\n'.format(port=self.serial.port))
            pass
        return

    def comp(self, status, word):
        if status is word:
            return True
        else:
            return False

    def decode(self, status):
        self.print_text_box('Decoding response ...')
        status = status.split(' ')
        if status[0] is 'STATUS':
            if status[1][7] is '1':
                self.led_13.setChecked(True)
            else:
                self.led_12.setChecked(True)
            if status[1][6] is '1':
                self.led_14.setChecked(True)
            else:
                self.led_11.setChecked(True)
        else:
            pass

    def _listen(self, thread_name:str, delay:int):
        self.print_text_box('Beginning listening thread ...\n')
        try:
            while self.continue_query:
                if self.serial.inWaiting() and self.resource_free:
                    self.serial.flush()
                    line = self.serial.readline().decode()
                    self.print_text_box("Interrupt: {msg}".format(msg=line))
                else:
                    pass

        except _thread.error as err:
            self.print_text_box("Failed to start status thread: {error}.".format(error=err))
            pass
        except:
            e = sys.exc_info()[0]
            self.print_text_box("Exception thrown: {error}.".format(error=e))
            pass

    def _listen_thread(self):
        try:
            self._get_status()
            _thread.start_new_thread(self._listen, ('thread-2', 1))
        except _thread.error as err:
            self.print_text_box("Failed to start status thread: {error}.".format(error=err))
            pass

    def _get_status(self):
        self.resource_free = False
        self.print_text_box("Entering queue for resource.")
        try:
            _thread.start_new_thread(self._status_query, ('thread-1', 1))
        except _thread.error as err:
            self.print_text_box("Failed to start status thread: {error}.".format(error=err))
            pass

    @QtCore.pyqtSlot()
    def _status_query(self, thread_name:str, delay:int):
        self.print_text_box('_status_query\n')
        try:
            line = self.write('STATUS?')
            self.decode(line)
        except serial.serialutil.SerialException:
            self.print_text_box("Serial port: {port} not connected ...\n".format(port=self.serial.port))
            pass
        self.print_text_box("Exiting queue for resource.")
        self.resource_free = True
        return line

    def _disconnect(self):
        self.continue_query = False
        self.print_text_box("Releasing connection fo port {}".format(self.serial.port))
        self.serial.close()
        return

    def write(self, message:str):
        self.serial.write(message.encode())
        self.serial.flush()
        line = self.serial.readline().decode()
        self.print_text_box("Initialization check: {resp}".format(resp=line))

        return line

    def print_text_box(self, str:str):
        self.textEdit.setText('[{ts}] {msg}\n'.format(ts=time.ctime(time.time())[11:-5], msg=str))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
