import serial
import serial.tools.list_ports
from PyQt5.QtCore import QObject
import relialok.Logger

class SerialPort(QObject):
    @relialok.Logger.function_log
    def __init__(self, port, parent = None):
        self.port = port
        self.resource_free = True
        self.connection_active = True
        self.port_release = True

        super(SerialPort, self).__init__(parent)
        self.serial = serial.Serial(self.port, '9600', timeout=5)

    @relialok.Logger.function_log
    def send(self, progress_callback=None, *args, **kwargs):
        '''
        Send command to serial port if resource is not currently in use and wait for reply.
        :param cmd: hardware command
        :param progress_callback: signal handler (unused currently)
        :return:
        '''

        self.command = kwargs['command']
        self.resource_free = False

        while self.port_release == False:  # Wait for Listen to release resource
            pass

        try:
            print('Reading serial port on {port}'.format(port=self.port))
            self.serial.write('{cmd}\n'.format(cmd=self.command).encode())
            self.serial.flush()
            line = self.serial.readline().decode()
            print("Initialization check: {resp}".format(resp=line))
            self.resource_free = True

            return line
        except serial.serialutil.SerialException:
            print('Read failed.')

    @relialok.Logger.function_log
    def listen(self, progress_callback):
        '''
        Monitors serial port for incoming data and passes it to decoding function via progress_callback signal.
        :param progress_callback: Generates a signal to pass data to the decoding function from within the thread.
        :return: None
        '''

        print('Listening on {port}'.format(port=self.port))
        while self.connection_active:
            try:
                if self.serial.inWaiting() and self.resource_free:
                    self.port_release = False
                    self.serial.flush()
                    line = self.serial.readline().decode()
                    print("Response check: {resp}".format(resp=line))
                    progress_callback.emit(line)
                    self.port_release = True
                else:
                    pass
            except serial.serialutil.SerialException:
                print('Listening error occurred.')

    @relialok.Logger.function_log
    def _is_open(self):
        '''
        Passes boolean depending on state of serial connection
        :return: serial port connection state *True/False)
        '''

        return self.serial.is_open

    @relialok.Logger.function_log
    def disconnect(self):
        '''
        Close serial port connection.
        :return: None
        '''

        self.resource_free = False
        self.connection_active = False
        self.serial.close()