#!/usr/bin/env python3
import time
from tkinter import *

from NumpadEntry import NumpadEntry
from stopwatch import Stopwatch


class App():
    apps = []

    def __init__(self, root, **kwargs):
        self.now = time.time()
        self.toggle_btn_color_stopped = 'green'
        self.toggle_btn_color_stopped_text = 'blue'
        self.toggle_btn_color_running = 'red'
        self.toggle_btn_color_running_text = 'white'
        self.stopwatch_digit_size = 22
        self.testColor_ready = 'light-blue'
        self.testColor_running = 'blue'
        self.testColor_paused = 'orange'
        self.testColor_passed = 'green'
        self.testColor_failed = 'red'
        self.testColor = ['lightblue', 'blue', 'orange', 'green', 'red']
        self.root = root
        self.name = 'Stopwatch'
        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
        self.apps.append(self)
        self.stopwatch = Stopwatch(name=self.name)
        self.currentTestTime = self.stopwatch.getCurrentDuration(self.now)
        self.remainingTestTime = self.stopwatch.getRemainingTestTime(self.now)
        self.testStatus = self.stopwatch.getStatusText()  # "0:Ready, "1:Running", "2:Paused", "3:Passed", "4:Failed"
        print(self.testStatus)

        # GUI
        self.name_label = Label(self.root)
        self.clock_frame = Label(self.root)
        self.timeRemaining_label = Label(self.root)
        self.testStatus_label = Label(self.root)
        self.frame = Frame(self.root)

        self.textEntryTgt_D = StringVar()
        self.textEntryTgt_H = StringVar()
        self.textEntryTgt_M = StringVar()
        self.textEntryTgt_S = StringVar()

        self.textEntryTgt_D.set('0')
        self.textEntryTgt_H.set('1')
        self.textEntryTgt_M.set('0')
        self.textEntryTgt_S.set('0')

        #self.tgtTimeEntry_D = NumpadEntry(self.root, textvariable=self.textEntryTgt_D)
        #self.tgtTimeEntry_H = NumpadEntry(self.root, textvariable=self.textEntryTgt_H)
        #self.tgtTimeEntry_M = NumpadEntry(self.root, textvariable=self.textEntryTgt_M)
        #self.tgtTimeEntry_S = NumpadEntry(self.root, textvariable=self.textEntryTgt_S)

        self.tgtTimeEntry_D = Entry(self.root, textvariable=self.textEntryTgt_D)
        self.tgtTimeEntry_H = Entry(self.root, textvariable=self.textEntryTgt_H)
        self.tgtTimeEntry_M = Entry(self.root, textvariable=self.textEntryTgt_M)
        self.tgtTimeEntry_S = Entry(self.root, textvariable=self.textEntryTgt_S)

        self.day_plus_btn = Button(self.root)
        self.day_minus_btn = Button(self.root)
        self.hr_plus_btn = Button(self.root)
        self.hr_minus_btn = Button(self.root)
        self.min_plus_btn = Button(self.root)
        self.min_minus_btn = Button(self.root)
        self.sec_plus_btn = Button(self.root)
        self.sec_minus_btn = Button(self.root)

        self.tgtTimeEntry_D.bind("<Key>", self.callback_updateTgt)
        self.tgtTimeEntry_H.bind('<Key>', self.callback_updateTgt)
        self.tgtTimeEntry_M.bind('<Key>', self.callback_updateTgt)
        self.tgtTimeEntry_S.bind('<Key>', self.callback_updateTgt)

        self.tgtTimeEntry_D.bind("<FocusOut>", self.callback_exit)
        self.tgtTimeEntry_H.bind('<FocusOut>', self.callback_exit)
        self.tgtTimeEntry_M.bind('<FocusOut>', self.callback_exit)
        self.tgtTimeEntry_S.bind('<FocusOut>', self.callback_exit)

        self.toggle_button = Button(self.root)  # start/stop depending on state
        self.lap_button = Button(self.root)  # not currently used
        self.reset_button = Button(self.root)  # reset the timer to zero
        self.quitButton = Button(self.root)  # not currently used

        self.setup(self.stopwatch)
        print("out of setup")

    def dayPlus(self):
        result = False
        val = int(self.textEntryTgt_D.get())
        if (val < 9):
            val = val + 1
            result = True
        self.textEntryTgt_D.set(str(val))
        self.update_sw_tgt()
        return result

    def dayMinus(self):
        result = False
        val = int(self.textEntryTgt_D.get())
        if (val > 0):
            val = val - 1
            result = True
        self.textEntryTgt_D.set(str(val))
        self.update_sw_tgt()
        return result

    def hrPlus(self):
        result = False
        val = int(self.textEntryTgt_H.get())
        if (val < 23):
            val = val + 1
            result = True
        else:
            if self.dayPlus():
                val = 0
                result = True
            else:
                val = 23  # unable to increase day so hr remains unchanged
        self.textEntryTgt_H.set(str(val))
        self.update_sw_tgt()
        return result

    def hrMinus(self):
        result = False
        val = int(self.textEntryTgt_H.get())
        if (val > 0):
            val = val - 1
            result = True
        else:
            if self.dayMinus():
                val = 23
                result = True
            else:
                val = 0
        self.textEntryTgt_H.set(str(val))
        self.update_sw_tgt()
        return result

    def minPlus(self):
        result = False
        val = int(self.textEntryTgt_M.get())
        if (val < 59):
            val = val + 1
            result = True
        else:
            if self.hrPlus():
                val = 0
                result = True
            else:
                val = 59  # unable to increase day so hr remains unchanged
        self.textEntryTgt_M.set(str(val))
        self.update_sw_tgt()
        return result

    def minMinus(self):
        result = False
        val = int(self.textEntryTgt_M.get())
        if (val > 0):
            val = val - 1
            result = True
        else:
            if self.hrMinus():
                val = 59
                result = True
            else:
                val = 0
        self.textEntryTgt_M.set(str(val))
        self.update_sw_tgt()
        return result

    def secPlus(self):
        result = False
        val = int(self.textEntryTgt_S.get())
        if (val < 59):
            val = val + 1
            result = True
        else:
            if self.minPlus():
                val = 0
                result = True
            else:
                val = 59  # unable to increase day so hr remains unchanged
        self.textEntryTgt_S.set(str(val))
        self.update_sw_tgt()
        return result

    def secMinus(self):
        result = False
        val = int(self.textEntryTgt_S.get())
        if (val > 0):
            val = val - 1
            result = True
        else:
            if self.minMinus():
                val = 59
                result = True
            else:
                val = 0
        self.textEntryTgt_S.set(str(val))
        self.update_sw_tgt()
        return result

    def callback_exit(self, e):
        print("callback_exit")
        self.callback_updateTgt(e)
        self.timeRemaining_label.focus_set()

    def setup(self, sw):
        # Create all of the GUI components and build all the visuals
        print("setup")
        self.name_label.configure(text=sw.name, font=("default", 15, "bold"), bg="blue", fg="white")
        self.clock_frame.configure(text="0:00:00:00", bg="white", fg="blue",
                                   font=("default", self.stopwatch_digit_size, "bold"), width=500, height=200)
        self.timeRemaining_label.configure(text="0:00:00:00", bg="white", fg="blue",
                                           font=("default", self.stopwatch_digit_size, "bold"), width=500, height=200)
        self.tgtTimeEntry_D.configure(bg="white", fg="blue", font=("default", self.stopwatch_digit_size - 4, "bold"),
                                      width=40)
        self.day_plus_btn.configure(text="+", bg=self.toggle_btn_color_stopped,
                                    fg="white", command=self.dayPlus, font=("default", 12, "bold"))
        self.day_minus_btn.configure(text="-", bg=self.toggle_btn_color_stopped,
                                     fg="white", command=self.dayMinus, font=("default", 12, "bold"))
        self.tgtTimeEntry_H.configure(bg="white", fg="blue", font=("default", self.stopwatch_digit_size - 4, "bold"),
                                      width=40)
        self.hr_plus_btn.configure(text="+", bg=self.toggle_btn_color_stopped,
                                   fg="white", command=self.hrPlus, font=("default", 12, "bold"))
        self.hr_minus_btn.configure(text="-", bg=self.toggle_btn_color_stopped,
                                    fg="white", command=self.hrMinus, font=("default", 12, "bold"))
        self.tgtTimeEntry_M.configure(bg="white", fg="blue", font=("default", self.stopwatch_digit_size - 4, "bold"),
                                      width=40)
        self.min_plus_btn.configure(text="+", bg=self.toggle_btn_color_stopped,
                                    fg="white", command=self.minPlus, font=("default", 12, "bold"))
        self.min_minus_btn.configure(text="-", bg=self.toggle_btn_color_stopped,
                                     fg="white", command=self.minMinus, font=("default", 12, "bold"))
        self.tgtTimeEntry_S.configure(bg="white", fg="blue", font=("default", self.stopwatch_digit_size - 4, "bold"),
                                      width=40)
        self.sec_plus_btn.configure(text="+", bg=self.toggle_btn_color_stopped,
                                    fg="white", command=self.secPlus, font=("default", 12, "bold"))
        self.sec_minus_btn.configure(text="-", bg=self.toggle_btn_color_stopped,
                                     fg="white", command=self.secMinus, font=("default", 12, "bold"))
        self.toggle_button.configure(text="START", bg=self.toggle_btn_color_stopped,
                                     fg=self.toggle_btn_color_stopped_text, command=self.toggle,
                                     font=("default", 12, "bold"))
        self.reset_button.configure(text="RESET", bg="orange", fg="black", command=self.reset,
                                    font=("default", 12, "bold"))
        self.testStatus_label.configure(text=self.testStatus, bg="yellow",
                                        fg=self.testColor[self.stopwatch.getStatus_int()],
                                        font=("default", self.stopwatch_digit_size - 2, "bold"), width=980, height=180,
                                        anchor="w")
        self.quitButton.configure(text="Quit", bg="red", fg="white", command=self.quit(), font=("default", 15, "bold"))

        self.name_label.place(x=10, y=10, width=100, height=33)
        self.clock_frame.place(x=120, y=10, width=200, height=33)
        self.tgtTimeEntry_D.place(x=325, y=10, width=27, height=33)
        self.day_plus_btn.place(x=354, y=10, width=15, height=15)
        self.day_minus_btn.place(x=354, y=27, width=15, height=15)
        self.tgtTimeEntry_H.place(x=371, y=10, width=40, height=33)
        self.hr_plus_btn.place(x=411, y=10, width=15, height=15)
        self.hr_minus_btn.place(x=411, y=27, width=15, height=15)
        self.tgtTimeEntry_M.place(x=428, y=10, width=40, height=33)
        self.min_plus_btn.place(x=468, y=10, width=15, height=15)
        self.min_minus_btn.place(x=468, y=27, width=15, height=15)
        self.tgtTimeEntry_S.place(x=484, y=10, width=40, height=33)
        self.sec_plus_btn.place(x=524, y=10, width=15, height=15)
        self.sec_minus_btn.place(x=524, y=27, width=15, height=15)
        self.timeRemaining_label.place(x=535, y=10, width=195, height=33)
        self.toggle_button.place(x=740, y=10, width=100, height=33)
        self.reset_button.place(x=850, y=10, width=100, height=33)
        self.testStatus_label.place(x=10, y=45, width=1000, height=33)
        print("finished setup, about to run self.updateTimer")
        self.updateTimer()
        print("finished self.updateTimer")

    def callback_updateTgt(self, e):
        try:
            self.tgt_D = int(self.tgtTimeEntry_D.get())
            if self.tgt_D < 0:
                self.tgtTimeEntry_D.insert(2, '0')
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
        self.updateTimer()

    def update_sw_tgt(self):
        # get the current values from the target entry boxes
        tgt_D = int(self.tgtTimeEntry_D.get())
        tgt_H = int(self.tgtTimeEntry_H.get())
        tgt_M = int(self.tgtTimeEntry_M.get())
        tgt_S = int(self.tgtTimeEntry_S.get())
        # calculate the target number of seconds
        tgtSeconds = (tgt_D * 24 * 60 * 60) + (tgt_H * 60 * 60) + (tgt_M * 60) + tgt_S
        # set the target time in the related stopwatch and update the timer
        self.stopwatch.setTargetTime(tgtSeconds)
        self.updateTimer()

    def showTimeDigits(self, digit):
        display = str(digit)
        if digit <= 9:
            display = str(0) + display
        return display

    def toggle(self):
        if self.stopwatch.running:
            self.stop()
        else:
            self.start()

    def start(self):
        self.stopwatch.start()  # let it do the logical work
        # do your GUI updates
        self.toggle_button.configure(text="Stop", bg=self.toggle_btn_color_running,
                                     fg=self.toggle_btn_color_running_text)
        self.updateTimer()

    def stop(self):
        self.stopwatch.stop()  # Logic and math here
        # Do GUI updates for stop
        self.toggle_button.configure(text="Start", bg=self.toggle_btn_color_stopped,
                                     fg=self.toggle_btn_color_stopped_text)
        self.updateTimer()

    def reset(self):
        now = time.time()
        self.stopwatch.reset()  # Logic handled in the Stopwatch class
        remainingTime = self.stopwatch.display_remainingTime(drt_now=now)
        # Update GUI components
        self.clock_frame.configure(text=self.stopwatch.display_elapsedTime())
        self.timeRemaining_label.configure(text=remainingTime)

    def updateTimer(self):
        now = time.time()
        self.testStatus_label.configure(text=self.stopwatch.getStatusText(),
                                        fg=self.testColor[self.stopwatch.getStatus_int()])
        if self.stopwatch.running:
            self.clock_frame.configure(text=self.stopwatch.display_elapsedTime(now))
            self.timeRemaining_label.configure(text=self.stopwatch.display_remainingTime(now))
            self.frame.after(1000, self.updateTimer)
        else:
            self.frame.after(1000, self.updateTimer)

    def getRunning(self):
        return self.stopwatch.running

    def quit(self):
        self.frame.destroy()
