#!/usr/bin/python3

# gfx usage, abc & strings, etc.
import os, string, time, datetime
import tkinter as tk
from PIL import ImageTk
from gtts import gTTS
import vlc

# import LIS configuration
import LISconfig

class frameSpelling:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # define class variables
        self.intSpellPointer = -1
        self.idFrameAfterEvent = 0
        self.bolInMenue = False

        # set fullscreen & resolution
        self.master.overrideredirect(LISconfig.bolScreenFull)
        if not LISconfig.strScreenGeometry:
            strScreenGeometry = str(self.master.winfo_screenwidth()) + "x" + str(self.master.winfo_screenheight())
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
        # load menu images
        self.rawMenuIcons = []
        for strIconFile in LISconfig.arrMenu:
            self.rawMenuIcons.append(ImageTk.Image.open(strIconFile[1]))
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
        self.idFrameAfterEvent = self.frame.after(0, self.update_label, self.intSpellPointer, False)
        # set up root bindings
        self.master.bind("<Configure>", self.windowReconfigure)

    # function to resize window contents if root window was resized
    def windowReconfigure(self,event):
        logConsole('width=',event.width, 'height=', event.height)

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

        #resize images to frame size
        # menu images
        self.MenuIcons = []
        for self.binRawImage in self.rawMenuIcons:
            tmpRatio = self.getRatio(self.frame.label, self.binRawImage)
            tmpimg = self.binRawImage.resize(tmpRatio, ImageTk.Image.ANTIALIAS)
            self.MenuIcons.append(ImageTk.PhotoImage(tmpimg))

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
    def update_label(self, i, bolManual, event = None):
        # auto move pointer forward if auto called by frame after event
        if not bolManual: i += 1

        if self.bolInMenue:
            # correct automatic and manual pointer jumping
            if i < 1 : i = len(LISconfig.arrMenu) - 1
            if i > len(LISconfig.arrMenu) - 1: i = 1

            self.updateLabelImage(LISconfig.arrMenu[i][0])
            if LISconfig.gTTSenable:
                if not LISconfig.gTTSdeactivateSpelling:
                    self.gttsPlayer(LISconfig.arrMenu[i][0]+'2', True)
        else:
            # correct automatic and manual pointer jumping
            if i < -1: i = len(LISconfig.strABC) - 1
            if i > len(LISconfig.strABC) - 1: i = -1

            if i == -1:
                # show menue item (for the case only "yes" is possible)
                tmpMenueEntry = '#ME'
                self.frame.labelText.set(tmpMenueEntry)
                tmpMenuEntryIndex = self.findInArray(LISconfig.arrMenu, tmpMenueEntry)
                self.frame.label.configure(image=self.MenuIcons[tmpMenuEntryIndex])
                if LISconfig.gTTSenable:
                    if not LISconfig.gTTSdeactivateSpelling:
                        self.gttsPlayer(LISconfig.arrMenu[tmpMenuEntryIndex][0], False)
            else:
                # Just rotate letters
                self.frame.label.configure(image='')
                self.frame.labelText.set(LISconfig.arrABC[i])
                if LISconfig.gTTSenable:
                    if not LISconfig.gTTSdeactivateSpelling:
                        self.gttsPlayer(LISconfig.arrABC[i], False)

        # save global pointer state
        self.intSpellPointer = i
        logConsole('pointer=', self.intSpellPointer, 'bolManual=', bolManual)
        # set up Frame After Event
        self.idFrameAfterEvent = self.frame.after(LISconfig.intLettersInterval, self.update_label, self.intSpellPointer, False)

    def findInArray(self, Array, Text):
        tmpCounter = -1
        for Line in Array:
            tmpCounter += 1
            if Line[0] == Text: return tmpCounter
        return tmpCounter

    def updateLabelImage(self, MenuEntry):
        tmpMenueEntry = MenuEntry
        self.frame.labelText.set(tmpMenueEntry)
        tmpMenuEntryIndex = self.findInArray(LISconfig.arrMenu, tmpMenueEntry)
        self.frame.label.configure(image=self.MenuIcons[tmpMenuEntryIndex])
        self.frame.label.update_idletasks()

    def keypressBackspace(self, event = None):
        # delete the last character
        logConsole('key pressed: backspace')
        MenueEntry = '#DL'
        self.updateLabelImage(MenueEntry)
        if LISconfig.gTTSenable:
            self.gttsPlayer(MenueEntry, True)
        self.frame.txt.delete('end-2c')

    def keypressSpace(self, event = None):
        # new word / space between the words
        logConsole('key pressed: space')
        MenueEntry = ' '
        self.updateLabelImage(MenueEntry)
        if LISconfig.gTTSenable:
            self.gttsPlayer(MenueEntry, True)
        self.labelMouseClickLeft(self)

    def keypressDelete(self, event = None):
        # delete the last word
        logConsole('key pressed: delete')
        MenueEntry = '#DW'
        self.updateLabelImage(MenueEntry)
        if LISconfig.gTTSenable:
            self.gttsPlayer(MenueEntry, True)
        tmpText = self.frame.txt.get('0.0', 'end')
        tmpText = tmpText.rstrip()
        self.frame.txt.delete('0.0', 'end')
        if tmpText.count(' ') > 0:
            tmpDelWord = tmpText.rsplit(' ', 1)
            tmpDelWord[0] = tmpDelWord[0].rstrip()
            self.frame.txt.insert('0.0', tmpDelWord[0])
            self.frame.txt.insert('end', ' ')

    def keypressHome(self, event = None):
        # delete the complete sentance
        logConsole('key pressed: home')
        MenueEntry = '#DS'
        self.updateLabelImage(MenueEntry)
        if LISconfig.gTTSenable:
            self.gttsPlayer(MenueEntry, True)
        self.frame.txt.delete('0.0', 'end')

    def keypressEnd(self, event = None):
        # send the sentance
        logConsole('key pressed: end')
        MenueEntry = '#SS'
        self.updateLabelImage(MenueEntry)
        if LISconfig.gTTSenable:
            self.gttsPlayer(MenueEntry, True)
            self.gttsPlayer(self.frame.txt.get('0.0', 'end'), True)
        # behavior: delete sentance in textfield
        if LISconfig.bolSentanceDeleteAfterSpoken:
            self.keypressHome()
        # behavior: start at A after sentance is spoken
        if LISconfig.bolSentanceStartAtAAfterSpoken:
            self.frame.after_cancel(self.idFrameAfterEvent)
            self.intSpellPointer = 0
            self.update_label(self.intSpellPointer, True)

    def keypressEscape(self, event = None):
        # escape application
        logConsole('key pressed: escape')
        MenueEntry = '#MB'
        self.updateLabelImage(MenueEntry)
        if LISconfig.gTTSenable:
            self.gttsPlayer(MenueEntry, True)

        # Exit menue if inside
        self.bolInMenue = False

        # Start at A
        self.frame.after_cancel(self.idFrameAfterEvent)
        self.intSpellPointer = -1
        self.update_label(self.intSpellPointer, True)


    def buttonPressLeft(self, event = None):
        # stop Frame After Event
        self.frame.after_cancel(self.idFrameAfterEvent)
        self.intSpellPointer -= 1
        logConsole('button pressed: left')
        # call function manually not by event
        self.update_label(self.intSpellPointer, True)

    def buttonPressRight(self, event = None):
        # stop Frame After Event
        self.frame.after_cancel(self.idFrameAfterEvent)
        self.intSpellPointer += 1
        logConsole('button pressed: right')
        # call function manually not by event
        self.update_label(self.intSpellPointer, True)

    def labelMouseClickLeft(self, event=None):
        chrLetterPressed = self.frame.labelText.get()
        # check if letter or menue item is pressed
        if chrLetterPressed[0] == "#":
            logConsole("menu item:", chrLetterPressed)
            # LISconfig.arrMenu 00 is allways the main menue icon
            if chrLetterPressed == LISconfig.arrMenu[0][0]:
                # stop Frame After Event, enter menue
                self.frame.after_cancel(self.idFrameAfterEvent)
                self.bolInMenue = True
                # call function manually not by event
                self.intSpellPointer = 1
                self.update_label(self.intSpellPointer, True)
            else:
                tmpMenuEntryIndex = self.findInArray(LISconfig.arrMenu, chrLetterPressed)
                # call function keypress dynamically
                getattr(self, LISconfig.arrMenu[tmpMenuEntryIndex][4])()
                # get out of menue
                self.frame.after_cancel(self.idFrameAfterEvent)
                self.bolInMenue = False
                self.intSpellPointer = -1
                self.update_label(self.intSpellPointer, True)
        else:
            logConsole("letter pressed: ", chrLetterPressed)
            # add letter to text widget
            self.frame.txt.insert('end', chrLetterPressed)
            self.frame.txt.see('end')
            self.frame.txt.update_idletasks()
            # Behavior settings
            if LISconfig.bolLetterStartAtAAfterLetter:
                self.frame.after_cancel(self.idFrameAfterEvent)
                self.intSpellPointer = 0
                self.update_label(self.intSpellPointer, True)

    # Calls gTTS and plays the output
    def gttsPlayer(self, strText, bolSleep, Event=None):

        instance = vlc.Instance(['--no-video'])
        VLCplayer = instance.media_player_new()

        # check cache if audio was downloaded before
        gTTScachefile = LISconfig.gTTStempFolder + LISconfig.gTTSlanguage + '_' + strText + '.mp3'
        if os.path.exists(gTTScachefile):
            # use file in cache
            pTTScache = instance.media_new(gTTScachefile)
            VLCplayer.set_media(pTTScache)
        else:
            # download to cache
            tmpgTTS = gTTS(text=strText, lang=LISconfig.gTTSlanguage)
            tmpFile = LISconfig.gTTStempFolder + '_last.mp3'
            tmpgTTS.save(tmpFile)
            pTTScache = instance.media_new(tmpFile)
            VLCplayer.set_media(pTTScache)
        # play resource with or without sleep
        VLCplayer.play()
        # this code is blocking. It really annoys me. The next code refactoring will fix that.
        if bolSleep:
            # "nothing special" also, because wait to start. Pause is liked stopped for us
            VLCplaying = set([0,1,2,3])
            while True:
                state = VLCplayer.get_state()
                if state not in VLCplaying:
                    break
                time.sleep(.10)
                continue

def gttsDownload():
    if not os.path.exists(LISconfig.gTTStempFolder): os.makedirs(LISconfig.gTTStempFolder)
    # letters
    for charLetter in LISconfig.strABC:
        tmpFile = LISconfig.gTTStempFolder + LISconfig.gTTSlanguage + '_' + charLetter + '.mp3'
        # download only if new
        if not os.path.exists(tmpFile):
            logConsole('gTTS cache, creating: ' + tmpFile)
            tmpgTTS = gTTS(text=charLetter, lang=LISconfig.gTTSlanguage)
            tmpgTTS.save(tmpFile)
    # menue entries
    for arrMenueEntry in LISconfig.arrMenu:
        tmpFile = LISconfig.gTTStempFolder + LISconfig.gTTSlanguage + '_' + arrMenueEntry[0] + '.mp3'
        tmpFile2 = LISconfig.gTTStempFolder + LISconfig.gTTSlanguage + '_' + arrMenueEntry[0] + '2.mp3'
        # download only if new
        if not os.path.exists(tmpFile):
            # solve better!
            logConsole('gTTS cache, creating: ' + tmpFile)
            tmpgTTS = gTTS(text=arrMenueEntry[2], lang=LISconfig.gTTSlanguage)
            tmpgTTS.save(tmpFile)
        if not os.path.exists(tmpFile2):
            logConsole('gTTS cache, creating: ' + tmpFile2)
            tmpgTTS = gTTS(text=arrMenueEntry[3], lang=LISconfig.gTTSlanguage)
            tmpgTTS.save(tmpFile2)

def logConsole(*String):
    if LISconfig.bolConsoleOutput:
        now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M") + ' -', String)

def main():
    # Do some preparation stuff
    # gTTS pre-downloading
    if LISconfig.gTTSenable: gttsDownload()

    root = tk.Tk()
    app = frameSpelling(root)
    root.title("LIShelpers - SimpleSpellMachine")
    root.mainloop()

if __name__ == '__main__':
    main()
