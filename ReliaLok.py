import tkinter as tk
import serial
import tk_tools
import serial.tools.list_ports
import time
import _thread
import sys

from tkinter import *
from tkinter import scrolledtext

class ReliaLok():

    def __init__(self, root):
        self.serial = serial.Serial()
        self.com_set = False
        self.continue_query = True
        self.resource_free = True
        self.port = StringVar()

        self.root = root
        self.root.title("Relia-Lok: QuadLock Edition")
        self.root.geometry('900x600')
        self.frame1 = Frame(self.root, padx=10, pady = 10)
        self.frame1.pack(fill=BOTH)
        self.frame2 = Frame(self.root, padx=10, pady = 10)
        self.frame2.pack(fill=BOTH)
        self.frame3 = Frame(self.root, padx=10, pady = 10)
        self.frame3.pack(fill=BOTH,  expand=True)
        self.frame4 = Frame(self.root, padx=10, pady=10)
        self.frame4.pack(fill=BOTH)
        self.frame5 = Frame(self.root, padx=10, pady=10)
        self.frame5.pack(fill=BOTH)
        self.frame6 = Frame(self.root, padx=10, pady=10)
        self.frame6.pack(fill=BOTH)
        self.frame7 = Frame(self.root, padx=10, pady=10)
        self.frame7.pack(fill=BOTH)
        self.frame8 = Frame(self.root, padx=10, pady=10)
        self.frame8.pack(fill=BOTH)

        self.canvas_c1 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c1.pack(side=LEFT)
        self.canvas_c2 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c2.pack(side=LEFT)
        self.canvas_c3 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c3.pack(side=LEFT)
        self.canvas_c4 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c4.pack(side=LEFT)
        self.canvas_c5 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c5.pack(side=LEFT)
        self.canvas_c6 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c6.pack(side=LEFT)
        self.canvas_c7 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c7.pack(side=LEFT)
        self.canvas_c8 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c8.pack(side=LEFT)

        self.canvas_c9 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c9.pack(side=LEFT)
        self.canvas_c10 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c10.pack(side=LEFT)
        self.canvas_c11 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c11.pack(side=LEFT)
        self.canvas_c12= tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c12.pack(side=LEFT)
        self.canvas_c13 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c13.pack(side=LEFT)
        self.canvas_c14 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c14.pack(side=LEFT)
        self.canvas_c15 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c15.pack(side=LEFT)
        self.canvas_c16 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c16.pack(side=LEFT)

        self.led_on_c1 = tk_tools.Led(self.canvas_c1, size=25)
        self.led_on_c1.pack()
        self.led_on_c1.to_green()
        self.led_off_c1 = tk_tools.Led(self.canvas_c1, size=25)
        self.led_off_c1.pack()
        self.led_off_c1.to_red()

        self.led_on_c2 = tk_tools.Led(self.canvas_c2, size=25)
        self.led_on_c2.pack()
        self.led_on_c2.to_green()
        self.led_off_c2 = tk_tools.Led(self.canvas_c2, size=25)
        self.led_off_c2.pack()
        self.led_off_c2.to_red()

        self.led_on_c3 = tk_tools.Led(self.canvas_c3, size=25)
        self.led_on_c3.pack()
        self.led_on_c3.to_green()
        self.led_off_c3 = tk_tools.Led(self.canvas_c3, size=25)
        self.led_off_c3.pack()
        self.led_off_c3.to_red()

        self.led_on_c4 = tk_tools.Led(self.canvas_c4, size=25)
        self.led_on_c4.pack()
        self.led_on_c4.to_green()
        self.led_off_c4 = tk_tools.Led(self.canvas_c4, size=25)
        self.led_off_c4.pack()
        self.led_off_c4.to_red()

        self.led_on_c5 = tk_tools.Led(self.canvas_c5, size=25)
        self.led_on_c5.pack()
        self.led_on_c5.to_green()
        self.led_off_c5 = tk_tools.Led(self.canvas_c5, size=25)
        self.led_off_c5.pack()
        self.led_off_c5.to_red()

        self.led_on_c6 = tk_tools.Led(self.canvas_c6, size=25)
        self.led_on_c6.pack()
        self.led_on_c6.to_green()
        self.led_off_c6 = tk_tools.Led(self.canvas_c6, size=25)
        self.led_off_c6.pack()
        self.led_off_c6.to_red()

        self.led_on_c7 = tk_tools.Led(self.canvas_c7, size=25)
        self.led_on_c7.pack()
        self.led_on_c7.to_green()
        self.led_off_c7 = tk_tools.Led(self.canvas_c7, size=25)
        self.led_off_c7.pack()
        self.led_off_c7.to_red()

        self.led_on_c8 = tk_tools.Led(self.canvas_c8, size=25)
        self.led_on_c8.pack()
        self.led_on_c8.to_green()
        self.led_off_c8 = tk_tools.Led(self.canvas_c8, size=25)
        self.led_off_c8.pack()
        self.led_off_c8.to_red()

        self.led_off_c9 = tk_tools.Led(self.canvas_c9, size=25)
        self.led_off_c9.pack()
        self.led_off_c9.to_red()

        self.led_off_c10 = tk_tools.Led(self.canvas_c10, size=25)
        self.led_off_c10.pack()
        self.led_off_c10.to_red()

        self.led_off_c11 = tk_tools.Led(self.canvas_c11, size=25)
        self.led_off_c11.pack()
        self.led_off_c11.to_red()

        self.led_off_c12 = tk_tools.Led(self.canvas_c12, size=25)
        self.led_off_c12.pack()
        self.led_off_c12.to_red()

        self.led_off_c13 = tk_tools.Led(self.canvas_c13, size=25)
        self.led_off_c13.pack()
        self.led_off_c13.to_red()

        self.led_off_c14 = tk_tools.Led(self.canvas_c14, size=25)
        self.led_off_c14.pack()
        self.led_off_c14.to_red()

        self.led_off_c15 = tk_tools.Led(self.canvas_c15, size=25)
        self.led_off_c15.pack()
        self.led_off_c15.to_red()

        self.led_off_c16 = tk_tools.Led(self.canvas_c16, size=25)
        self.led_off_c16.pack()
        self.led_off_c16.to_red()

        self.com_ports = [comport.device for comport in serial.tools.list_ports.comports()]

        self.option = OptionMenu(self.frame4, self.port, *self.com_ports).pack(side=LEFT)
        self.status_button = Button(self.frame4, text="Status", height = 2, width = 18, pady = 5, command=self._get_status).pack(side=LEFT)
        self.init_button = Button(self.frame4, text="Initialize", height=2, width=18, pady=5, command=self._listen_thread).pack(side=LEFT)
        self.connect_button = Button(self.frame4, text="Connect", height=2, width=18, pady = 5, command=self.connect).pack(side=LEFT)
        self.stop_button = Button(self.frame4, text="Stop", height = 2, width = 18, pady = 5, background ="red", command=self._stop_query).pack(side=LEFT)
        self.scroll_text = scrolledtext.ScrolledText(self.frame3, width = 100, height = 20)
        self.scroll_text.pack(side=LEFT)
        self.print_tb("Initializing ReliaLok: QuadLock Edition ...")


    def connect(self):
        self.serial.port = self.port.get()
        self.print_tb('Connecting to ReliaLok on port: {port}\n'.format(port=self.port.get()))
        try:
            self.serial.open()
            self.print_tb('>>>>> {object}\n'.format(object=self.serial))
            self.print_tb("Successfully connected to device ...\n")
        except serial.serialutil.SerialException:
            self.print_tb("Could not open connection on {port} ...\n".format(port=self.port.get()))
            pass
        return

    def _listen(self, thread_name:str, delay:int):
        print('Beginning listening thread ...\n')
        try:
            while self.continue_query:
                if self.serial.inWaiting() and self.resource_free:
                    self.serial.flush()
                    line = self.serial.readline().decode()
                    self.print_tb("Interrupt: {msg}".format(msg=line))
                else:
                    pass

        except _thread.error as err:
            self.print_tb("Failed to start status thread: {error}.".format(error=err))
            pass
        except:
            e = sys.exc_info()[0]
            self.print_tb("Exception thrown: {error}.".format(error=e))
            pass

    def _listen_thread(self):
        try:
            _thread.start_new_thread(self._listen, ('thread-2', 1))
        except _thread.error as err:
            self.print_tb("Failed to start status thread: {error}.".format(error=err))
            pass

    def _get_status(self):
        self.resource_free = False
        self.print_tb("Entering queue for resource.")
        try:
            _thread.start_new_thread(self._status_query, ('thread-1', 1))
        except _thread.error as err:
            self.print_tb("Failed to start status thread: {error}.".format(error=err))
            pass

    def _status_query(self, thread_name:str, delay:int):
        try:
            self.write('STATUS?')
        except serial.serialutil.SerialException:
            self.print_tb("Serial port: {port} not connected ...\n".format(port=self.port.get()))
            pass
        self.print_tb("Exiting queue for resource.")
        self.resource_free = True


    def _stop_query(self):
        self.continue_query = False
        self.print_tb("Stopping.")
        return

    def write(self, message:str):
        self.serial.write(message.encode())
        self.serial.flush()
        line = self.serial.readline().decode()
        self.print_tb("Initialization check: {resp}".format(resp=line))

    def print_tb(self, str:str):
        self.scroll_text.insert(INSERT, '[{ts}] {msg}\n'.format(ts=time.ctime(time.time())[11:-5], msg=str))

if __name__ == '__main__':
    root = tk.Tk()
    gui = ReliaLok(root)
    root.mainloop()