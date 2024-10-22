#!/usr/bin/python

import os
from tkinter import messagebox

import RPi.GPIO as GPIO

from WaterBlockTest_aStopWatchFrame import *

versionNumber = "1.05"

fullscreen = True
lbl_bg_color = 'yellow'
lbl_txt_color = 'blue'
toggle_btn_color_stopped = 'green'
toggle_btn_color_stopped_text = 'blue'
toggle_btn_color_running = 'red'
toggle_btn_color_running_text = 'white'

menu_font=("Verdana", 18)

header_height = 80
bottom_height = 80
center_border = 80
number_of_tubes = 4
tube_row_height = 80

final_spacer = int(round((tube_row_height / 6)))
total_rows_plus_final = int(
    round((number_of_tubes * ((tube_row_height) + 1)) + final_spacer + header_height + bottom_height + center_border))

window_width = 1024
window_height = total_rows_plus_final

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

root = Tk()
background_colour = 'yellow'
root.title('Water Block Tester')
root.geometry('{}x{}'.format(window_width, window_height))
root.attributes("-fullscreen", fullscreen)

def onExit():
    sys.exit()

def onShutdown():
    #os.system("reboot")
    shutDown = messagebox.askquestion("Quit","Are you sure you want to turn off?")
    if shutDown == "yes":
        os.system("reboot")

def aboutInfo():
    messagebox.showinfo("PPC UK", "Timer by D Earley\nVersion: " + versionNumber)

def update():
    updateQuestion = messagebox.askquestion("Update", "Warning: Update will close the application\nAll timers will be lost\nDo you wish to continue?")
    if updateQuestion == "yes":
        # do something here to update the software
        #messagebox.showinfo("Water Block Tester","Update not yet implemented")
        os.system("sudo sh update_from_github.sh 1")
        sys.exit()
        os.system("sh run.sh")

def startAll():
    if not sw1.getRunning():
        sw1.start()
    if not sw2.getRunning():
        sw2.start()
    if not sw3.getRunning():
        sw3.start()
    if not sw4.getRunning():
        sw4.start()

def stopAll():
    if sw1.getRunning():
        sw1.stop()
    if sw2.getRunning():
        sw2.stop()
    if sw3.getRunning():
        sw3.stop()
    if sw4.getRunning():
        sw4.stop()

def resetAll():
    sw1.reset()
    sw2.reset()
    sw3.reset()
    sw4.reset()

def stopGPIOPins():
    messagebox.showinfo("GPIO Pin", "Stop Timers with Pins:\nPin 8  - Tube 1 [orange]\nPin  7 - Tube 2 [green]\nPin 12 - Tube 3 [brown]\nPin 16 - Tube 4 [blue]")


menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
aboutmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='File', menu=filemenu, font=menu_font)
menubar.add_cascade(label='About', menu=aboutmenu, font=menu_font) #menu=aboutmenu

filemenu.add_command(label='GPIO Pins', command=stopGPIOPins, font=menu_font)
filemenu.add_command(label='Shutdown', command=onShutdown, font=menu_font)
filemenu.add_command(label='Exit Application', command=onExit, font=menu_font)
#aboutmenu.add_command(label='About', command=aboutInfo)
aboutmenu.add_command(label='About', command=aboutInfo, font=menu_font)
aboutmenu.add_command(label='App Update', command=update, font=menu_font)

## Logo Image
logo_image = PhotoImage(file="Belden_PPC_logo-standard.png").subsample(10, 10)
# RPi_image_small = PhotoImage(file="RPi.png").subsample(10, 10)

# create the main containers
top_frame = Frame(root, bg='white', width=root.winfo_reqwidth() - 10, height=header_height, padx=5, pady=5)
center_frame = Frame(root, bg='blue', width=root.winfo_reqwidth() - 10, height=85, borderwidth=(center_border / 4),
                     padx=0, pady=30)
btm_frame = Frame(root, bg='blue', width=root.winfo_reqwidth() - 10, height=bottom_height, borderwidth=5, padx=5,
                  pady=5)

top_frame.grid(row=0, sticky="nsew")
top_frame.grid_rowconfigure(0, weight=0)
top_frame.grid_columnconfigure(0, weight=1)

center_frame.grid(row=1, sticky="nsew")
center_frame.rowconfigure(1, weight=5)

btm_frame.grid(row=2, sticky="nsew")
btm_frame.rowconfigure(0, weight=1)

# create the widgets for the top frame
title_label = Label(top_frame, text='Water Blocker Test Station', bg='white', fg=lbl_txt_color,
                    font=('default', 20, 'bold'))
header_logo_image = Label(top_frame, image=logo_image)

# layout the widgets in the top frame
title_label.grid(row=0, sticky='e')
header_logo_image.grid(row=0, sticky='w')

# create header row
ctr_row0 = Frame(center_frame, bg=background_colour, width=980, height=tube_row_height / 2, padx=3, pady=3)
# create the individual frames for the rows to hold the stop watch objects
ctr_row1 = Frame(center_frame, bg=background_colour, width=980, height=tube_row_height, padx=3, pady=3)
ctr_row2 = Frame(center_frame, bg=background_colour, width=980, height=tube_row_height, padx=3, pady=3)
ctr_row3 = Frame(center_frame, bg=background_colour, width=980, height=tube_row_height, padx=3, pady=3)
ctr_row4 = Frame(center_frame, bg=background_colour, width=980, height=tube_row_height, padx=3, pady=3)
# ctr_row5 = Frame(center_frame, bg=background_colour, width=980, height=tube_row_height, padx=3, pady=3)
# ctr_row6 = Frame(center_frame, bg=background_colour, width=980, height=tube_row_height, padx=3, pady=3)
ctr_row_last = Frame(center_frame, bg=background_colour, width=root.winfo_reqwidth(), height=tube_row_height / 4,
                     padx=2, pady=2)

# place the rows in the center grid
ctr_row0.grid(row=0, column=0, sticky='nsew')
ctr_row1.grid(row=1, column=0, sticky="nsew")
ctr_row2.grid(row=2, column=0, sticky="nsew")
ctr_row3.grid(row=3, column=0, sticky="nsew")
ctr_row4.grid(row=4, column=0, sticky="nsew")
# ctr_row5.grid(row=5, column=0, sticky="nsew")
# ctr_row6.grid(row=6, column=0, sticky="nsew")
ctr_row_last.grid(row=7, column=0, sticky='nsew')

# create 6 stopwatch widgets for center frame
sw1 = App(ctr_row1, name="Tube 1", stopPin=40)
sw2 = App(ctr_row2, name='Tube 2', stopPin=37)
sw3 = App(ctr_row3, name='Tube 3', stopPin=36)
sw4 = App(ctr_row4, name='Tube 4', stopPin=35)
# sw5 = App(ctr_row5, name='Tube 5', stopPin=33)
# sw6 = App(ctr_row6, name='Tube 6', stopPin=32)

# create header labels
lbl_name = Label(ctr_row0, text='Tube', bg=lbl_bg_color, fg=lbl_txt_color, font=('default', 12), anchor="center")
lbl_elapsed = Label(ctr_row0, text='Elapsed Time', bg=lbl_bg_color, fg=lbl_txt_color, font=('default', 12),
                    anchor="center")
lbl_days = Label(ctr_row0, text='Days', bg=lbl_bg_color, fg=lbl_txt_color, font=('default', 11), anchor="center")
lbl_hrs = Label(ctr_row0, text='Hrs', bg=lbl_bg_color, fg=lbl_txt_color, font=('default', 11), anchor="center")
lbl_mins = Label(ctr_row0, text='Mins', bg=lbl_bg_color, fg=lbl_txt_color, font=('default', 11), anchor="center")
lbl_secs = Label(ctr_row0, text='Secs', bg=lbl_bg_color, fg=lbl_txt_color, font=('default', 11), anchor="center")
lbl_remaining = Label(ctr_row0, text='Remaining Time', bg=lbl_bg_color, fg=lbl_txt_color, font=('default', 12),
                      anchor="center")
# Create Global Action Buttons
start_all = Button(ctr_row0, text="Start All", bg="green", fg="blue", command=startAll,
                                    font=("default", 9))  # Start all non running timers
stop_all = Button(ctr_row0, text="Stop All", bg="red", fg="white", command=stopAll,
                                    font=("default", 9))  # Stop all running timers
reset_all = Button(ctr_row0, text="Reset All", bg="orange", fg="black", command=resetAll,
                                    font=("default", 12, "bold"))  # reset all timers to zero

# Place the header labels
lbl_name.place(x=10, y=7, width=100, height=28)
lbl_elapsed.place(x=120, y=5, width=200, height=28)
lbl_days.place(x=326, y=5, width=40, height=30)
lbl_hrs.place(x=376, y=5, width=40, height=30)
lbl_mins.place(x=430, y=5, width=40, height=30)
lbl_secs.place(x=484, y=5, width=40, height=30)
lbl_remaining.place(x=530, y=7, width=200, height=28)

start_all.place(x=739, y=2, width=100, height=17)
stop_all.place(x=739, y=20, width=100, height=17)
reset_all.place(x=850, y=4, width=100, height=30)
# setup GPIO hardware switches
start_switch = [0, 8, 7, 12, 16, 20, 21]  # switch pins starting at switch[1] (0 is place holder)
start_switches = [
    {'pin': 0, 'name': "Holding Pin", 'stopwatch': NONE},
    {'pin': 8, 'name': "Tube 1", 'stopwatch': sw1},
    {'pin': 7, 'name': "Tube 2", 'stopwatch': sw2},
    {'pin': 12, 'name': "Tube 3", 'stopwatch': sw3},
    {'pin': 16, 'name': "Tube 4", 'stopwatch': sw4},
    #    {'pin': 20, 'name': "Tube 5", 'stopwatch': sw5},
    #    {'pin': 21, 'name': "Tube 6", 'stopwatch': sw6},
]

# Handle GPIO Stop sensor
def switchPin_callback(channel):
    print('edge detection on channel %s' % channel)
    #    if channel == 21 and sw6.getRunning():
    #        sw6.toggle()
    #    if channel == 20 and sw5.getRunning():
    #        sw5.toggle()
    if channel == 16 and sw4.getRunning():
        sw4.fail()
    if channel == 12 and sw3.getRunning():
        sw3.fail()
    if channel == 7 and sw2.getRunning():
        sw2.fail()
    if channel == 8 and sw1.getRunning():
        sw1.fail()

for switch in start_switch:
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(switch, GPIO.FALLING, callback=switchPin_callback)

try:
    root.mainloop()
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
