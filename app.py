# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, \
        NavigationToolbar2Tk
from matplotlib.figure import Figure
import logging
import numpy as np
import tkinter
import serial

SERIAL_PORT='/dev/ttyUSB0'
BAUDRATE=115200
serial_if = serial.Serial()
serial_if.port = SERIAL_PORT
serial_if.baudrate = BAUDRATE

def do_connect_bms():
    try:
        serial_if.open()
        tkinter.messagebox.\
                showinfo("Success", "{} connected to bms scope".
                         format(SERIAL_PORT))
        connect_button.configure(text="Disconnect {}".format(SERIAL_PORT))
        connect_button.configure(command=do_disconnect_bms)
        do_read_serial()
    except serial.serialutil.SerialException as e:
        logging.error(e)
        tkinter.messagebox.\
                showinfo("Failure", "Check USB-UART connection to BMS")



def do_disconnect_bms():
    serial_if.close()
    tkinter.messagebox.\
            showinfo("Success", "{} disconnected to bms scope".
                     format(SERIAL_PORT))
    connect_button.configure(text="Disconnect {}".format(SERIAL_PORT))
    connect_button.configure(command=do_disconnect_bms)


def do_read_serial():
    line = serial_if.readline()
    if line:
        logging.warning(line)
    root.after(10, do_read_serial)

root = tkinter.Tk()
root.wm_title("BMS scope")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent

bottom = tkinter.Frame(root)
bottom.pack(side=tkinter.BOTTOM)
quit_button = tkinter.Button(master=root, text='Quit', command=_quit)
quit_button.pack(in_=bottom, side=tkinter.LEFT)
connect_button = tkinter.Button(master=root, text='Connect BMS',
                                command=do_connect_bms)
connect_button.pack(in_=bottom, side=tkinter.LEFT)


tkinter.mainloop()
