#!/usr/bin/python3

# import configuration
import LISconfig

# gfx usage, abc & strings, etc.
import tkinter as tk
import string

class frameSpelling:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # define class variables
        self.intSpellPointer = 0
        self.idFrameAfterEvent = 0

        # set fullscreen & resolution
        self.master.overrideredirect(LISconfig.bolScreenFull)
        if not LISconfig.strScreenGeometry:
            strScreenGeometry = str(self.winfo_screenwidth()) + "x" + str(self.winfo_screenheight())
            self.master.geometry(strScreenGeometry)
        else:
            self.master.geometry(LISconfig.strScreenGeometry)

        # create button left
        self.frame.btnLeft = tk.Button(text ="left", command = self.buttonPressLeft)
        self.frame.btnLeft.pack()
        self.frame.btnLeft.place(relx=0.0, rely=0.0, relheight=0.7, relwidth=0.3)
        # create button right
        self.frame.btnRight = tk.Button(text ="right", command = self.buttonPressRight)
        self.frame.btnRight.pack()
        self.frame.btnRight.place(relx=0.7, rely=0.0, relheight=0.7, relwidth=0.3)
        # create txt widget
        self.frame.txt = tk.Text(font=("Helvetica",32))
        self.frame.txt.pack()
        self.frame.txt.place(relx=0.0, rely=0.7, relheight=0.3, relwidth=1.0)
        # create txt lable and bindings
        self.frame.lableText = tk.StringVar()
        self.frame.lable = tk.Label(master, textvariable=self.frame.lableText, font=("Helvetica",90))
        self.frame.lable.bind("<Button-1>",self.LableMouseClickLeft)
        self.frame.lable.pack()
        self.frame.lable.place(relx=0.3, rely=0.0, relheight=0.7, relwidth=0.4)

        # set up frame and update hook
        self.frame.pack()
        self.idFrameAfterEvent = self.frame.after(0, self.update_text, self.intSpellPointer, False)
        # set up root bindings
        self.master.bind("<Configure>", self.windowReconfigure)

    # function to resize window contents if root window was resized
    def windowReconfigure(self,event):
        print(event.width,event.height)

        # resize lable font
        intLableWidth = self.frame.lable.winfo_width()
        intLableHeight = self.frame.lable.winfo_height()
        intLableFontSize = 0
        # going into negative values is px size
        if intLableHeight > intLableWidth:
            intLableFontSize = intLableHeight - intLableHeight * 2
        else:
            intLableFontSize = intLableWidth - intLableWidth * 2
        self.frame.lable.config(font=("Helvetica", intLableFontSize))

        # resize text widget size
        intTextWidth = self.frame.txt.winfo_width()
        intTextHeight = self.frame.txt.winfo_height()
        intTextFontSize = 0
        # going into negative values is px size
        intTextFontSize = intTextHeight - intTextHeight * 2
        self.frame.txt.config(font=("Helvetica", intTextFontSize))

    # function to write the letters to the screen
    def update_text(self,i, bolManual, event = None):
        # auto move pointer forward if auto called by frame after event
        if not bolManual: i += 1

        # correct automatic and manual pointer jumping
        if i < 0: i = len(LISconfig.strABC) - 1
        if i > len(LISconfig.strABC) - 1: i = 0

        # update text in lable
        self.frame.lableText.set(arrABC[i])

        # save global pointer state
        self.intSpellPointer = i
        print('pointer=', self.intSpellPointer, 'bolManual=', bolManual)
        # set up Frame After Event
        self.idFrameAfterEvent = self.frame.after(LISconfig.intLettersInterval, self.update_text, self.intSpellPointer, False)

    def buttonPressLeft(self, event = None):
        # stop Frame After Event
        self.frame.after_cancel(self.idFrameAfterEvent)
        self.intSpellPointer -= 1
        print('button pressed: left')
        # call function manually not by event
        self.update_text(self.intSpellPointer, True)

    def buttonPressRight(self, event = None):
        # stop Frame After Event
        self.frame.after_cancel(self.idFrameAfterEvent)
        self.intSpellPointer += 1
        print('button pressed: right')
        # call function manually not by event
        self.update_text(self.intSpellPointer, True)

    def LableMouseClickLeft(self, event=None):
        chrLetterPressed = self.frame.lableText.get()
        print("letter pressed: ", chrLetterPressed)
        self.frame.txt.insert('end', chrLetterPressed)
        self.frame.txt.see('end')
        self.frame.txt.update_idletasks()

def main():
    root = tk.Tk()
    app = frameSpelling(root)
    root.mainloop()

# load letters into array arrABC[]
arrABC = []
arrABC.extend(range(0,len(LISconfig.strABC) + 1))
intCount = 0
for charLetter in LISconfig.strABC:
    arrABC[intCount] = charLetter
    intCount += 1

if __name__ == '__main__':
    main()
