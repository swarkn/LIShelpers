#!/usr/bin/python3

# import configuration
import LISconfig

# gfx usage, abc & strings, etc.
import tkinter as tk
from PIL import ImageTk
import string

class frameSpelling:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # define class variables
        self.intSpellPointer = -1
        self.idFrameAfterEvent = 0

        # set fullscreen & resolution
        self.master.overrideredirect(LISconfig.bolScreenFull)
        if not LISconfig.strScreenGeometry:
            strScreenGeometry = str(self.winfo_screenwidth()) + "x" + str(self.winfo_screenheight())
            self.master.geometry(strScreenGeometry)
        else:
            self.master.geometry(LISconfig.strScreenGeometry)

        # create keyboard bindings
        master.bind('<Left>', self.buttonPressLeft)
        master.bind('<Right>', self.buttonPressRight)
        master.bind('<Return>', self.labelMouseClickLeft)
        master.bind('<space>', self.keypressSpace)              # space = new_word
        master.bind('<BackSpace>', self.keypressBackspace)      # BackSpace = del_letter
        master.bind('<Delete>', self.keypressDelete)            # Delete = del_word
        master.bind('<Home>', self.keypressHome)                # Home = del_sentance
        master.bind('<End>', self.keypressEnd)                  # End = send_sentance
        master.bind('<Escape>', self.keypressEscape)            # Escape = Exit

        # create initial Window with contents
        self.windowConfigure(self.frame)

    def windowConfigure(self, frame):
        # load images
        self.rawicon_ArrowLeft = ImageTk.Image.open(LISconfig.strImage_ArrowLeft)
        self.rawicon_ArrowRight = ImageTk.Image.open(LISconfig.strImage_ArrowRight)
        self.rawicon_menu = ImageTk.Image.open(LISconfig.arrMenu[0][1])
        # create button left
        frame.btnLeft = tk.Button(text ="left", relief='flat', command = self.buttonPressLeft)
        frame.btnLeft.pack()
        frame.btnLeft.place(relx=0.0, rely=0.0, relheight=0.7, relwidth=0.3)
        # create button right
        frame.btnRight = tk.Button(text ="right", relief='flat', command = self.buttonPressRight)
        frame.btnRight.pack()
        frame.btnRight.place(relx=0.7, rely=0.0, relheight=0.7, relwidth=0.3)
        # create txt widget
        frame.txt = tk.Text(wrap='none',font=("Helvetica",32))
        frame.txt.pack()
        frame.txt.place(relx=0.0, rely=0.7, relheight=0.3, relwidth=1.0)
        # create scrollbar
        frame.scrollbar=tk.Scrollbar(self.frame.txt, orient='horizontal')
        frame.txt.configure(xscrollcommand=self.frame.scrollbar.set)
        frame.scrollbar.pack(side='bottom', fill='x')
        frame.scrollbar.config(command=self.frame.txt.xview)
        # create txt label and bindings
        frame.labelText = tk.StringVar()
        frame.label = tk.Label(self.master, textvariable=self.frame.labelText, font=("Helvetica",90))
        frame.label.bind("<Button-1>",self.labelMouseClickLeft)
        frame.label.pack()
        frame.label.place(relx=0.3, rely=0.0, relheight=0.7, relwidth=0.4)
        # setup frame and update hook
        frame.pack()
        self.idFrameAfterEvent = self.frame.after(0, self.update_text, self.intSpellPointer, False)
        # set up root bindings
        self.master.bind("<Configure>", self.windowReconfigure)

    # function to resize window contents if root window was resized
    def windowReconfigure(self,event):
        print(event.width,event.height)

        # resize label font
        intlabelWidth = self.frame.label.winfo_width()
        intlabelHeight = self.frame.label.winfo_height()
        intlabelFontSize = 0
        # going into negative values is px size
        if intlabelHeight > intlabelWidth:
            intlabelFontSize = intlabelHeight - intlabelHeight * 2
        else:
            intlabelFontSize = intlabelWidth - intlabelWidth * 2
        self.frame.label.config(font=("Helvetica", intlabelFontSize))

        # resize text widget size
        intTextWidth = self.frame.txt.winfo_width()
        intTextHeight = self.frame.txt.winfo_height()
        intTextFontSize = 0
        # going into negative values is px size (minus 20px because of the scrollbar)
        intTextFontSize = (intTextHeight - intTextHeight * 2) + 20
        self.frame.txt.config(font=("Helvetica", intTextFontSize))

        #resize images to frame size (need to find a better way to do so)
        # menu image
        tmpRatio = self.getRatio(self.frame.label, self.rawicon_menu)
        tmpimg = self.rawicon_menu.resize(tmpRatio, ImageTk.Image.ANTIALIAS)
        self.icon_menu = ImageTk.PhotoImage(tmpimg)
        # arrow left
        tmpRatio = self.getRatio(self.frame.btnLeft, self.rawicon_ArrowLeft)
        tmpimg = self.rawicon_ArrowLeft.resize(tmpRatio, ImageTk.Image.ANTIALIAS)
        self.icon_ArrowLeft = ImageTk.PhotoImage(tmpimg)
        self.frame.btnLeft.configure(image = self.icon_ArrowLeft)
        # arrow right
        tmpRatio = self.getRatio(self.frame.btnRight, self.rawicon_ArrowRight)
        tmpimg = self.rawicon_ArrowRight.resize(tmpRatio, ImageTk.Image.ANTIALIAS)
        self.icon_ArrowRight = ImageTk.PhotoImage(tmpimg)
        self.frame.btnRight.configure(image = self.icon_ArrowRight)

    # calculate the ratio for images on widgets
    def getRatio(self, Widget, RawImage):
        intWidthRatio = RawImage.size[0] / Widget.winfo_width()
        intHeightRatio = RawImage.size[1] / Widget.winfo_height()
        intImageRatio = max(intWidthRatio, intHeightRatio)
        return (int(RawImage.size[0] / intImageRatio), int(RawImage.size[1] / intImageRatio))

    # function to write the letters to the screen
    def update_text(self, i, bolManual, event = None):
        # auto move pointer forward if auto called by frame after event
        if not bolManual: i += 1

        # correct automatic and manual pointer jumping
        if i < -1: i = len(LISconfig.strABC) - 1
        if i > len(LISconfig.strABC) - 1: i = -1

        # update text in label (-1 is Menue)
        if not i == -1:
            self.frame.label.configure(image='')
            self.frame.labelText.set(LISconfig.arrABC[i])
        else:
            self.frame.labelText.set(LISconfig.arrMenu[0][0])
            self.frame.label.configure(image=self.icon_menu)

        # save global pointer state
        self.intSpellPointer = i
        print('pointer=', self.intSpellPointer, 'bolManual=', bolManual)
        # set up Frame After Event
        self.idFrameAfterEvent = self.frame.after(LISconfig.intLettersInterval, self.update_text, self.intSpellPointer, False)

    def keypressBackspace(self, event = None):
        # delete the last character
        print('key pressed: backspace')
        self.frame.txt.delete('end-2c')

    def keypressSpace(self, event = None):
        # new word / space between the words
        print('key pressed: space')
        self.frame.labelText.set(' ')
        self.labelMouseClickLeft(self)

    def keypressDelete(self, event = None):
        # delete the last word
        print('key pressed: delete')
        tmpText = self.frame.txt.get('0.0', 'end')
        self.keypressHome(self)
        if tmpText.count(' ') > 0:
            tmpDelWord = tmpText.rsplit(' ', 1)
            tmpDelWord[0] = tmpDelWord[0].rstrip()
            self.frame.txt.insert('0.0', tmpDelWord[0])

    def keypressHome(self, event = None):
        # delete the complete sentance
        print('key pressed: home')
        self.frame.txt.delete('0.0', 'end')

    def keypressEnd(self, event = None):
        # send the sentance
        print('key pressed: end')

    def keypressEscape(self, event = None):
        # escape application
        print('key pressed: escape')

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

    def labelMouseClickLeft(self, event=None):
        chrLetterPressed = self.frame.labelText.get()
        print("letter pressed: ", chrLetterPressed)
        self.frame.txt.insert('end', chrLetterPressed)
        self.frame.txt.see('end')
        self.frame.txt.update_idletasks()

def main():
    root = tk.Tk()
    app = frameSpelling(root)
    root.mainloop()

if __name__ == '__main__':
    main()
