import tkinter as tk
import serial
import tk_tools
import serial.tools.list_ports
import time
import _thread

from tkinter import *
from tkinter import scrolledtext

class ReliaLok():

    def __init__(self, root):
        self.serial = serial.Serial()
        self.com_set = False
        self.continue_query = False
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

        self.canvas_c1 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c1.pack(side=LEFT)
        self.canvas_c2 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c2.pack(side=LEFT)
        self.canvas_c3 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c3.pack(side=LEFT)
        self.canvas_c4 = tk.Canvas(self.frame1, width=7, height=14)
        self.canvas_c4.pack(side=LEFT)

        self.canvas_c5 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c5.pack(side=LEFT)
        self.canvas_c6 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c6.pack(side=LEFT)
        self.canvas_c7 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c7.pack(side=LEFT)
        self.canvas_c8 = tk.Canvas(self.frame2, width=7, height=14)
        self.canvas_c8.pack(side=LEFT)

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

        self.led_off_c5 = tk_tools.Led(self.canvas_c5, size=25)
        self.led_off_c5.pack()
        self.led_off_c5.to_red()

        self.led_off_c6 = tk_tools.Led(self.canvas_c6, size=25)
        self.led_off_c6.pack()
        self.led_off_c6.to_red()

        self.led_off_c7 = tk_tools.Led(self.canvas_c7, size=25)
        self.led_off_c7.pack()
        self.led_off_c7.to_red()

        self.led_off_c8 = tk_tools.Led(self.canvas_c8, size=25)
        self.led_off_c8.pack()
        self.led_off_c8.to_red()

        self.com_ports = [comport.device for comport in serial.tools.list_ports.comports()]

        self.option = OptionMenu(self.frame4, self.port, *self.com_ports).pack(side=LEFT)
        self.status_button = Button(self.frame4, text="Status", height = 2, width = 18, pady = 5, command=self.get_status).pack(side=LEFT)
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
        except SerialException:
            self.print_tb("Could not open connection on {port} ...\n".format(port=self.port.get()))
            pass
        return

    def get_status(self):
        self.continue_query = True
        try:
            _thread.start_new_thread(self._status_query, ('thread-1', 1))
        except _thread.error as err:
            self.print_tb("Failed to start status thread: {error}.".format(error=err))

    def _status_query(self, thread_name, delay):
        while self.continue_query:
            self.write('STATUS?')
        return
    def _stop_query(self):
        self.continue_query = False
        return

    def write(self, message):
        self.serial.write(message.encode())
        self.serial.flush()
        line = self.serial.readline().decode()
        self.print_tb("Initialization check: {resp}".format(resp=line))

    def print_tb(self, str):
        self.scroll_text.insert(INSERT, '[{ts}] {msg}\n'.format(ts=time.ctime(time.time())[11:-5], msg=str))

if __name__ == '__main__':
    root = tk.Tk()
    gui = ReliaLok(root)
    root.mainloop()