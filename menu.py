import sys
from tkinter import *
from tkinter.colorchooser import *


class MenuBar:
    def __init__(self, parent):
        self.parent = parent
        self.menubar = Menu(parent)
        self.Create()

    def Create(self):
        self.parent.config(menu=self.menubar)

    def add_menu(self, menuname, commands):
        menu = Menu(self.menubar, tearoff=0)
        for command in commands:
            menu.add_command(label=command[0], command=command[1])
            if command[2]:
                menu.add_separator()
        self.menubar.add_cascade(label=menuname, menu=menu)

    def onExit(self):
        sys.exit()

    def onOpen(self):
        print
        'Open'

    def ColourChooser(self):
        color = askcolor()[1]
        print(str(color))
        return 'yellow'
