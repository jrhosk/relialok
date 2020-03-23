import serial
import serial.tools.list_ports
from PyQt5.QtCore import QObject
import relialok.logger

class SerialPort(QObject):
    @relialok.logger.function_log
    def __init__(self, port, parent = None):
        self.port = port
        self.resource_free = True
        self.connection_active = True

        super(SerialPort, self).__init__(parent)
        self.serial = serial.Serial(self.port, '9600', timeout=5)

    @relialok.logger.function_log
    def read_port(self, progress_callback):
        self.resource_free = False
        try:
            print('Reading serial port on {port}'.format(port=self.port))
            self.serial.write('STATUS?\n'.encode())
            self.serial.flush()
            line = self.serial.readline().decode()
            print("Initialization check: {resp}".format(resp=line))
            self.resource_free = True

            return line
        except serial.serialutil.SerialException:
            print('Read failed.')

    @relialok.logger.function_log
    def listen_port(self, progress_callback):
        print('Listening on {port}'.format(port=self.port))
        while self.connection_active:
            try:
                if self.serial.inWaiting() and self.resource_free:
                    self.serial.flush()
                    line = self.serial.readline().decode()
                    print("Response check: {resp}".format(resp=line))
                    progress_callback.emit(line)
                else:
                    pass
            except serial.serialutil.SerialException:
                print('Listening error occurred.')

    @relialok.logger.function_log
    def _is_open(self):
        return self.serial.is_open

    @relialok.logger.function_log
    def disconnect(self):
       self.resource_free = False
       self.connection_active = False
       self.serial.close()