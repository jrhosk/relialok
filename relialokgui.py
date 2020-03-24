from PyQt5 import QtCore
from PyQt5.QtCore import QThreadPool
from PyQt5 import QtGui
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtWidgets

from relialok import *
import serial
import serial.tools.list_ports
import time
import sys

class RelialokMainWindow(object):
    def __init__(self, MainWindow, *args, **kwargs):
        '''
        Main front-end GUI class. Defines backend functions for hardware interface and front-end widgets for control and
        monitoring of interlock.

        :param MainWindow:
        :param args: MainWindow (QtWidgets.QMainWindow())
        :param kwargs:
        '''

        # Class variables and flags
        self.com_set = False
        self.continue_query = True
        self.com_ports = [comport.device for comport in serial.tools.list_ports.comports()]
        self.serial = serial.Serial()
        self.setup_ui(MainWindow)


    def setup_ui(self, MainWindow):
        '''
        Definition of GUI widgets, positioning, and framing. Also connects functions to widget hooks.
        '''
        # Gui definition
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 725)
        MainWindow.setMinimumSize(QtCore.QSize(933, 725))
        MainWindow.setMaximumSize(QtCore.QSize(934, 726))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 650, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 650, 75, 23))
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(830, 650, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")

        self.textBox = QtWidgets.QTextEdit(self.centralwidget)
        self.textBox.setGeometry(QtCore.QRect(20, 240, 881, 381))
        self.textBox.setObjectName("textBox")

        self.cursor = QTextCursor(self.textBox.document())

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

        self.led_25 = LedIndicatorWidget.LedIndicator(color='blue')
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
        self.led_f1 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_f1.setObjectName("led_fault_1")
        self.horizontalLayout.addWidget(self.led_f1)
        self.led_f1.setChecked(False)

        # Fault 2
        self.led_f2 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_f2.setObjectName("led_fault_2")
        self.horizontalLayout.addWidget(self.led_f2)
        self.led_f2.setChecked(False)

        # Fault 3
        self.led_f3 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_f3.setObjectName("led_fault_3")
        self.horizontalLayout.addWidget(self.led_f3)
        self.led_f3.setChecked(False)

        # Fault 4
        self.led_f4 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_f4.setObjectName("led_fault_4")
        self.horizontalLayout.addWidget(self.led_f4)
        self.led_f4.setChecked(False)

        # Fault 5
        self.led_f5 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_f5.setObjectName("led_fault_5")
        self.horizontalLayout.addWidget(self.led_f5)
        self.led_f5.setChecked(False)

        # Fault 6
        self.led_f6 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_f6.setObjectName("led_fault_6")
        self.horizontalLayout.addWidget(self.led_f6)
        self.led_f6.setChecked(False)

        # Fault 7
        self.led_f7 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_f7.setObjectName("led_fault_7")
        self.horizontalLayout.addWidget(self.led_f7)
        self.led_f7.setChecked(False)

        # Fault 8
        self.led_f8 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_f8.setObjectName("led_fault_8")
        self.horizontalLayout.addWidget(self.led_f8)
        self.led_f8.setChecked(False)

        # ON-1
        self.led_on_1 = LedIndicatorWidget.LedIndicator(color='green')
        self.led_on_1.setObjectName("led_on_1")
        self.gridLayout_3.addWidget(self.led_on_1, 1, 0, 1, 1)
        self.led_on_1.setChecked(False)

        # OFF-1
        self.led_off_1 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_off_1.setObjectName("led_off_2")
        self.gridLayout_3.addWidget(self.led_off_1, 2, 0, 1, 1)
        self.led_off_1.setChecked(False)

        # ON-2
        self.led_on_2 = LedIndicatorWidget.LedIndicator(color='green')
        self.led_on_2.setObjectName("led_on_2")
        self.gridLayout_3.addWidget(self.led_on_2, 1, 1, 1, 1)
        self.led_on_2.setChecked(False)

        # OFF-2
        self.led_off_2 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_off_2.setObjectName("led_off_2")
        self.gridLayout_3.addWidget(self.led_off_2, 2, 1, 1, 1)
        self.led_off_2.setChecked(False)

        # ON-3
        self.led_on_3 = LedIndicatorWidget.LedIndicator(color='green')
        self.led_on_3.setObjectName("led_on_3")
        self.gridLayout_3.addWidget(self.led_on_3, 1, 2, 1, 1)
        self.led_on_3.setChecked(False)

        # OFF-3
        self.led_off_3 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_off_3.setObjectName("led_off_3")
        self.gridLayout_3.addWidget(self.led_off_3, 2, 2, 1, 1)
        self.led_off_3.setChecked(False)

        # ON-4
        self.led_on_4 = LedIndicatorWidget.LedIndicator(color='green')
        self.led_on_4.setObjectName("led_on_4")
        self.gridLayout_3.addWidget(self.led_on_4, 1, 3, 1, 1)
        self.led_on_4.setChecked(False)

        # OFF-4
        self.led_off_4 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_off_4.setObjectName("led_off_4")
        self.gridLayout_3.addWidget(self.led_off_4, 2, 3, 1, 1)
        self.led_off_4.setChecked(False)

        # ON-5
        self.led_on_5 = LedIndicatorWidget.LedIndicator(color='green')
        self.led_on_5.setObjectName("led_on_5")
        self.gridLayout_3.addWidget(self.led_on_5, 1, 4, 1, 1)
        self.led_on_5.setChecked(False)

        # OFF-5
        self.led_off_5 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_off_5.setObjectName("led_off_5")
        self.gridLayout_3.addWidget(self.led_off_5, 2, 4, 1, 1)
        self.led_off_5.setChecked(False)

        # ON-6
        self.led_on_6 = LedIndicatorWidget.LedIndicator(color='green')
        self.led_on_6.setObjectName("led_on_6")
        self.gridLayout_3.addWidget(self.led_on_6, 1, 5, 1, 1)
        self.led_on_6.setChecked(False)

        # OFF-6
        self.led_off_6 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_off_6.setObjectName("led_off_6")
        self.gridLayout_3.addWidget(self.led_off_6, 2, 5, 1, 1)
        self.led_off_6.setChecked(False)

        # ON-7
        self.led_on_7 = LedIndicatorWidget.LedIndicator(color='green')
        self.led_on_7.setObjectName("led_on_7")
        self.gridLayout_3.addWidget(self.led_on_7, 1, 6, 1, 1)
        self.led_on_7.setChecked(False)

        # OFF-7
        self.led_off_7 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_off_7.setObjectName("led_off_7")
        self.gridLayout_3.addWidget(self.led_off_7, 2, 6, 1, 1)
        self.led_off_7.setChecked(False)

        # ON-8
        self.led_on_8 = LedIndicatorWidget.LedIndicator(color='green')
        self.led_on_8.setObjectName("led_on_8")
        self.gridLayout_3.addWidget(self.led_on_8, 1, 7, 1, 1)
        self.led_on_8.setChecked(False)

        # OFF-8
        self.led_off_8 = LedIndicatorWidget.LedIndicator(color='red')
        self.led_off_8.setObjectName("led_off_8")
        self.gridLayout_3.addWidget(self.led_off_8, 2, 7, 1, 1)
        self.led_off_8.setChecked(False)


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
        self.gridLayout_3.addWidget(self.label_8, 0, 7, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 3, 1, 1)


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

        self.dispatcher = {'FAULT': [self.led_f1.setChecked,
                                     self.led_f2.setChecked,
                                     self.led_f3.setChecked,
                                     self.led_f4.setChecked,
                                     self.led_f5.setChecked,
                                     self.led_f6.setChecked,
                                     self.led_f7.setChecked,
                                     self.led_f8.setChecked],
                           'ON-OFF': [[self.led_on_1.setChecked, self.led_off_1.setChecked],
                                      [self.led_on_2.setChecked, self.led_off_2.setChecked],
                                      [self.led_on_3.setChecked, self.led_off_3.setChecked],
                                      [self.led_on_4.setChecked, self.led_off_4.setChecked],
                                      [self.led_on_5.setChecked, self.led_off_5.setChecked],
                                      [self.led_on_6.setChecked, self.led_off_6.setChecked],
                                      [self.led_on_7.setChecked, self.led_off_7.setChecked],
                                      [self.led_on_8.setChecked, self.led_off_8.setChecked]]}

        # Button hooks
        self.pushButton.clicked.connect(self.connect)
        self.pushButton_2.clicked.connect(self.disconnect)
        self.pushButton_3.clicked.connect(self.listen)
        self.pushButton_4.clicked.connect(self.get_status)
        self.pushButton_6.clicked.connect(lambda: self.decode('DISABLE '))
        self.pushButton_7.clicked.connect(self.close)


    def retranslateUi(self, MainWindow):
        '''
        Redefines label and button names for front-end usages.
        :param MainWindow: QtWidgets.QMainWindow()
        :return: None
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.pushButton_2.setText(_translate("MainWindow", "Disconnect"))
        self.pushButton_3.setText(_translate("MainWindow", "Listen"))
        self.pushButton_4.setText(_translate("MainWindow", "Status"))
        self.pushButton_5.setText(_translate("MainWindow", "Reset"))
        self.pushButton_6.setText(_translate("MainWindow", "Disable"))
        self.pushButton_7.setText(_translate("MainWindow", "Close"))
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

        # Start thread
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def connect(self):
        '''
        Create instance of serial port handler, SerialPort(). Passes combo boxx selection containing current serial port.
        :return: None
        '''
        self.print_output("Initializing serial connection on port: {port}".format(port=self.comboBox.currentText()))
        self.serial = SerialPort(self.comboBox.currentText())
        self.connection_open = True

    def close(self):
        '''
        Ends MainWindow session.
        :return: None
        '''
        MainWindow.close()


    def disconnect(self):
        '''
        Waits for completion of current thread in threadpool and closes serial port connection. If current connection
        doesn't exist, function passes and does nothing.
        :return: None
        '''

        if self.serial.is_open:
            try:
                self.print_output("Disconnecting serial connection on port: {port}".format(port=self.comboBox.currentText()))
                self.threadpool.waitForDone(2000)
                self.serial.disconnect()
            except Exception as ex:
                pass
        else:
            self.print_output('Connection not active. Please connect.')
 
    def print_output(self, s):
        '''
        Wrapper function to print to front-end text box.
        :param s: string-type to send to text box.
        :return: None
        '''

        self.cursor.setPosition(0)
        self.textBox.setTextCursor(self.cursor)
        self.textBox.insertPlainText('[{ts}] {msg}\n'.format(ts=time.ctime(time.time())[11:-5], msg=s))

    def decode(self, reply):
        '''
        Parses and decodes incoming communication from hardware device.
        :param reply: string-type reply or interrupt message from hardware.
        :return: None
        '''

        self.print_output('Decoding response ...')
        type, reply = reply.split(' ')
        reply = reply.strip()

        self.status = reply[::2]
        self.state = reply[1::2]
        self.status = [bool(int(self.status[i])) for i in range(len(self.status))]
        self.state = [bool(int(self.state[i])) for i in range(len(self.state))]

        if type == 'STATUS':
            for (on, off), i in zip(self.dispatcher['ON-OFF'], range(len(self.dispatcher['ON-OFF']))):
                if not self.status[i]:
                    on(False)
                    off(False)
                else:
                    on(self.state[i])
                    off(not self.state[i])
        elif type == 'DISABLE':
            for (on, off), i in zip(self.dispatcher['ON-OFF'], range(len(self.dispatcher['ON-OFF']))):
                on(False)
                off(False)

        elif type == 'FAULT':
            self.fault = [bool(int(self.reply[i])) for i in range(len(self.reply))]
            for fault, i in zip(self.dispatcher['FAULT'], range(len(self.dispatcher['FAULT']))):
                fault(self.fault[i])
        else:
            pass


    def data_received(self, data):
        print('Data at COM port:')
        self.print_output(data)


    def listen(self):
        '''
        Spanwns polling thread to look for interrupt communication form hardware device at COM port. Function has
        secondary priority to serial port resource.
        :return: None
        '''

        if self.serial.is_open:
            try:
                # Pass the function to execute
                worker = WorkerThreading.Worker(self.serial.listen)
                worker.signals.result.connect(self.decode)
                #        worker.signals.finished.connect(self.thread_complete)
                worker.signals.progress.connect(self.data_received)

                # Execute
                self.threadpool.start(worker)
            except Exception as ex:
                self.print_output('Error listening on port: {0}. Check log for more details.'.format(ex))
        else:
            self.print_output('Connection not active. Please connect.')
            return

    def get_status(self):
        '''
        Spawns thread for sending command to hardware. Sends STATUS? command to hardware ans then waits for reply. Reply
        is sent to decode fucntion. Has top priority to serial port resource.
        :param cmd:
        :return:
        '''

        if self.serial._is_open():
            try:
                # Pass the function to execute
                worker = WorkerThreading.Worker(self.serial.send, command='STATUS?')
                worker.signals.result.connect(self.decode)
        #        worker.signals.finished.connect(self.thread_complete)
                # Execute
                self.threadpool.start(worker)
            except Exception as ex:
                self.print_output('Error reading on port: {0}. Check log for more details.'.format(ex))
        else:
            self.print_output('Connection not active. Please connect.')
            return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RelialokMainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
