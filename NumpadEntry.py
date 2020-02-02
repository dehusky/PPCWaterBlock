from tkinter import *
from tkinter import simpledialog


class NumpadEntry(Entry):
    def __init__(self, parent=None, **kw):
        Entry.__init__(self, parent, **kw)
        self.bind('<FocusIn>', self.numpadEntry)
        self.bind('<FocusOut>', self.numpadExit)
        self.edited = False

    def numpadEntry(self, event):
        if self.edited == False:
            print("You Clicked on me")
            self['bg'] = '#ffffcc'
            self.edited = True
            new = numPad(self)
        else:
            self.edited = False

    def numpadExit(self, event):
        self['bg'] = '#ffffff'


class numPad(simpledialog.Dialog):
    def __init__(self, master=None, textVariable=None):
        self.top = Toplevel(master=master)
        self.top.protocol("WM_DELETE_WINDOW", self.ok)
        self.createWidgets()
        self.master = master

    def createWidgets(self):
        btn_list = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', 'Close', 'Del']
        # create and position all buttons with a for-loop
        # r, c used for row, column grid values
        r = 1
        c = 0
        n = 0
        # list(range()) needed for Python3
        btn = []
        for label in btn_list:
            # partial takes care of function and argument
            cmd = lambda x=label: self.click(x)
            # create the button
            cur = Button(self.top, text=label, width=10, height=5, command=cmd)
            btn.append(cur)
            # position the button
            btn[-1].grid(row=r, column=c)
            # increment button index
            n += 1
            # update row/column position
            c += 1
            if c == 3:
                c = 0
                r += 1

    def click(self, label):
        print(label)
        if label == 'Del':
            currentText = self.master.get()
            self.master.delete(0, END)
            self.master.insert(0, currentText[:-1])
        elif label == 'Close':
            self.ok()
        else:
            currentText = self.master.get()
            self.master.delete(0, END)
            self.master.insert(0, currentText + label)

    def ok(self):
        self.top.destroy()
        self.top.master.focus()


class App(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, **kw)
        self.textEntryVar1 = StringVar()
        self.e1 = NumpadEntry(self, textvariable=self.textEntryVar1)
        self.e1.grid()

        self.textEntryVar2 = StringVar()
        self.e2 = NumpadEntry(self, textvariable=self.textEntryVar2)
        self.e2.grid()

        self.btn = Button(self, text="Add", command=self.add)
        self.btn.grid()

    def add(self):
        result = int(self.textEntryVar1.get()) + int(self.textEntryVar2.get())
        print(result)


if __name__ == '__main__':
    root = Tk()
    root.geometry("200x100")
    app = App(root)
    app.grid()
    root.mainloop()
