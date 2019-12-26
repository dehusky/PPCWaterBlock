#!/usr/bin/python3
import time
from tkinter import *

from stopwatch import Stopwatch


class App():
    apps = []

    def __init__(self, root, **kwargs):
        self.stopwatch_digit_size = 20
        self.root = root
        self.name = 'Stopwatch'
        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
        self.apps.append(self)
        self.stopwatch = Stopwatch(name=self.name)
        self.currentTestTime = self.stopwatch.getCurrentDuration()
        self.remainingTestTime = self.stopwatch.getRemainingTestTime()
        self.testStatus = "Running"  # "Running", "Passed", "Failed"

        # GUI
        self.name_label = Label(self.root)
        self.clock_frame = Label(self.root)
        self.timeRemaining_label = Label(self.root)
        self.frame = Frame(self.root)

        self.tgt_D = '1'
        self.tgt_H = '0'
        self.tgt_M = '0'
        self.tgt_S = '0'

        self.tgtTimeEntry_D = Entry(self.root)
        self.tgtTimeEntry_H = Entry(self.root)
        self.tgtTimeEntry_M = Entry(self.root)
        self.tgtTimeEntry_S = Entry(self.root)

        self.tgtTimeEntry_D.insert(2, self.tgt_D)
        self.tgtTimeEntry_H.insert(2, self.tgt_H)
        self.tgtTimeEntry_M.insert(2, self.tgt_M)
        self.tgtTimeEntry_S.insert(2, self.tgt_S)

        self.tgtTimeEntry_D.bind("<Key>", self.callback_updateTgt)
        self.tgtTimeEntry_H.bind('<Key>', self.callback_updateTgt)
        self.tgtTimeEntry_M.bind('<Key>', self.callback_updateTgt)
        self.tgtTimeEntry_S.bind('<Key>', self.callback_updateTgt)

        self.tgtTimeEntry_D.bind("<FocusOut>", self.callback_updateTgt)
        self.tgtTimeEntry_H.bind('<FocusOut>', self.callback_updateTgt)
        self.tgtTimeEntry_M.bind('<FocusOut>', self.callback_updateTgt)
        self.tgtTimeEntry_S.bind('<FocusOut>', self.callback_updateTgt)

        self.toggle_button = Button(self.root)
        self.lap_button = Button(self.root)
        self.reset_button = Button(self.root)
        self.quitButton = Button(self.root)

        self.setup(self.stopwatch)
        print("out of setup")

    def setup(self, sw):
        # Create all of the GUI components and build all the visuals
        print("setup")
        self.name_label.configure(text=sw.name, font=("default", 10, "bold"), bg="blue", fg="white")
        self.clock_frame.configure(text="00:00:00", bg="white", fg="blue",
                                   font=("default", self.stopwatch_digit_size, "bold"), width=500, height=200)
        self.timeRemaining_label.configure(text="00:00:00", bg="white", fg="blue",
                                           font=("default", self.stopwatch_digit_size, "bold"), width=500, height=200)
        self.tgtTimeEntry_D.configure(bg="white", fg="blue", font=("default", self.stopwatch_digit_size, "bold"),
                                      width=40)
        self.tgtTimeEntry_H.configure(bg="white", fg="blue", font=("default", self.stopwatch_digit_size, "bold"),
                                      width=40)
        self.tgtTimeEntry_M.configure(bg="white", fg="blue", font=("default", self.stopwatch_digit_size - 2, "bold"),
                                      width=40)
        self.tgtTimeEntry_S.configure(bg="white", fg="blue", font=("default", self.stopwatch_digit_size - 2, "bold"),
                                      width=40)
        self.toggle_button.configure(text="START", bg="green", fg="black", command=self.toggle,
                                     font=("default", 10, "bold"))
        self.reset_button.configure(text="RESET", bg="orange", fg="black", command=self.reset,
                                    font=("default", 10, "bold"))
        self.quitButton.configure(text="Quit", bg="red", fg="white", command=self.quit(), font=("default", 10, "bold"))

        self.name_label.place(x=10, y=10, width=100, height=30)
        self.clock_frame.place(x=120, y=10, width=200, height=30)
        self.tgtTimeEntry_D.place(x=330, y=10, width=40, height=30)
        self.tgtTimeEntry_H.place(x=380, y=10, width=40, height=30)
        self.tgtTimeEntry_M.place(x=430, y=10, width=40, height=30)
        self.tgtTimeEntry_S.place(x=480, y=10, width=40, height=30)
        self.timeRemaining_label.place(x=530, y=10, width=200, height=30)
        self.toggle_button.place(x=740, y=10, width=100, height=30)
        self.reset_button.place(x=850, y=10, width=100, height=30)
        print("finished setup, about to run self.updateTimer")
        self.updateTimer()

        print("finished self.updateTimer")

    def callback_updateTgt(self, e):
        try:
            self.tgt_D = int(self.tgtTimeEntry_D.get())
        except:
            if not type(self.tgt_D) is int:
                self.tgtTimeEntry_D.insert(2, '0')
        try:
            self.tgt_H = int(self.tgtTimeEntry_H.get())
        except:
            if not type(self.tgt_H) is int:
                self.tgtTimeEntry_H.insert(2, '0')
        try:
            self.tgt_M = int(self.tgtTimeEntry_M.get())
        except:
            if not type(self.tgt_M) is int:
                self.tgtTimeEntry_M.insert(2, '0')
        try:
            self.tgt_S = int(self.tgtTimeEntry_S.get())
        except:
            if not type(self.tgt_S) is int:
                self.tgtTimeEntry_S.insert(2, '0')
        try:
            tgtSeconds = (self.tgt_D * 24 * 60 * 60) + (self.tgt_H * 60 * 60) + (self.tgt_M * 60) + self.tgt_S
            print("in callback_updateTgt, tgtSecs: " + str(tgtSeconds))
            self.stopwatch.setTargetTime(tgtSeconds)
        except:
            print('Error Found: ' + str(e))

    def showTimeDigits(self, digit):
        display = str(digit)
        if digit <= 9:
            display = str(0) + display
        return display

    def toggle(self):
        if self.stopwatch.getRunning():
            self.stop()
        else:
            self.start()

    def start(self):
        self.stopwatch.start()  # let it do the logical work
        # do your GUI updates
        self.toggle_button.configure(text="Stop")
        self.updateTimer()

    def stop(self):
        self.stopwatch.stop()  # Logic and math here
        # Do GUI updates for stop
        self.toggle_button.configure(text="Start")
        self.updateTimer()

    def reset(self):
        self.stopwatch.reset()  # Logic again handled in the Stopwatch class
        # Clean up GUI components
        self.clock_frame.configure(text=self.stopwatch.display_time())

    def updateTimer(self):
        now = time.time()
        if self.stopwatch.running:
            duration = self.stopwatch.display_time()
            remainingTime = self.stopwatch.display_remainingTime(now=now)
            self.clock_frame.configure(text=duration)
            self.timeRemaining_label.configure(text=remainingTime)
            self.frame.after(500, self.updateTimer)

    def getRunning(self):
        return self.stopwatch.running

    def quit(self):
        self.frame.destroy()
