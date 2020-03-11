from tkinter import *
from tkinter import simpledialog


class NumpadEntry(Entry):
    def __init__(self, parent, **kw):
        Entry.__init__(self, parent, **kw)
        self.bind('<FocusIn>', self.numpadEntry)
        self.bind('<FocusOut>', self.numpadExit)
        self.edited = False
        self.value = StringVar()
        self.parent = parent
        self.bind('<Button-1>', self.numpadClick)

    def numpadClick(self, event):
        print("numpadClicked")
        self.value = Entry.get()
        print(self.value)

    def numpadEntry(self, event):
        self.np_parent = self.parent
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
    def __init__(self, master, textVariable=None):
        self.top = Toplevel(master=master)
        # self.top.attributes("-topmost", True)
        w = 228
        h = 325
        x = 550
        y = 180
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.top.protocol("WM_DELETE_WINDOW", self.ok)
        self.top.title("Enter Value")
        self.mum = self.top.winfo_parent()
        print(self.mum)
        self.np_master = master
        self.createWidgets()

    def createWidgets(self):
        btn_list = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', 'Enter', 'Del']
        # create and position all buttons with a for-loop
        # r, c used for row, column grid values
        r = 1
        c = 0
        n = 0
        # current entry display
        # self.display_label = Label(self.top)
        # self.display_label.configure(text=self.value, bg="yellow",fg="black",font=("default", 10, "bold"), width=200, height=40,anchor="w")
        # list(range()) needed for Python3
        btn = []
        for label in btn_list:
            # partial takes care of function and argument
            cmd = lambda x=label: self.click(x)
            # create the button
            cur = Button(self.top, text=label, width=6, height=4, command=cmd)
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
            currentText = self.np_master.get()
            self.np_master.delete(0, END)
            self.np_master.insert(0, currentText[:-1])
        elif label == 'Enter':
            self.ok()
        else:
            currentText = self.np_master.get()
            self.np_master.delete(0, END)
            self.np_master.insert(0, currentText + label)

    def ok(self):
        currentText = self.np_master.get()
        print("currentText")
        print(currentText)
        if currentText == '':
            self.np_master.insert(0, '0')
        elif type(int(currentText)) != int:
            print("currenttext not an int")
            self.np_master.delete(0, END)
            self.np_master.insert(0, '0')
        elif int(currentText) < 0:
            print("currentText < 0")
            self.np_master.insert(0, '0')
        else:
            masterStr = str(self.np_master)
            value = int(currentText)
            # check Days
            if masterStr == ".!frame2.!frame2.!numpadentry" or masterStr == ".!frame2.!frame3.!numpadentry" or masterStr == ".!frame2.!frame4.!numpadentry" or masterStr == ".!frame2.!frame5.!numpadentry":
                if value > 7:
                    self.np_master.delete(0, END)
                    self.np_master.insert(0, '7')
                    print('days over range')

            # check hours
            if masterStr == ".!frame2.!frame2.!numpadentry2" or masterStr == ".!frame2.!frame3.!numpadentry2" or masterStr == ".!frame2.!frame4.!numpadentry2" or masterStr == ".!frame2.!frame5.!numpadentry2":
                if value > 23:
                    self.np_master.delete(0, END)
                    self.np_master.insert(0, '23')
                    print('hours over range')
            # check mins
            if masterStr == ".!frame2.!frame2.!numpadentry3" or masterStr == ".!frame2.!frame3.!numpadentry3" or masterStr == ".!frame2.!frame4.!numpadentry3" or masterStr == ".!frame2.!frame5.!numpadentry3":
                if value > 59:
                    self.np_master.delete(0, END)
                    self.np_master.insert(0, '59')
                    print('mins over range')
            # check secs
            if masterStr == ".!frame2.!frame2.!numpadentry4" or masterStr == ".!frame2.!frame3.!numpadentry4" or masterStr == ".!frame2.!frame4.!numpadentry4" or masterStr == ".!frame2.!frame5.!numpadentry4":
                if value > 59:
                    self.np_master.delete(0, END)
                    self.np_master.insert(0, '59')
                    print('seconds over range')
        print("time to lose the keypad")
        # self.np_master.tk_focusNext().focus_set()
        # self.np_master.master.focus_set()
        # self.master.update()
        self.top.destroy()





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
