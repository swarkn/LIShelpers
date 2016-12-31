#!/usr/bin/python3
import string

# String off possible characters to be shown for spelling
strABC = string.ascii_uppercase[:26]

# load letters into array arrABC[]
arrABC = []
arrABC.extend(range(0,len(strABC) + 1))
intCount = 0
for charLetter in strABC:
    arrABC[intCount] = charLetter
    intCount += 1

# Manual string off max. screen resolution (double "" to otherwise let tk detect the max resolution)
#strScreenGeometry = ""
strScreenGeometry = "1280x720"
bolScreenFull = False

# Control how the letters should behave
intLettersInterval = 2000

# system icons
strImage_ArrowLeft = 'icons/arrow_left.png'
strImage_ArrowRight = 'icons/arrow_right.png'

# gTTS Environment
gTTSenable = True
gTTSdeactivateSpelling = False
gTTStempFolder = 'cache/'
gTTSlanguage = 'de'
# gTTSenableSpelling = True

# enable console output
bolConsoleOutput = True

# editing menue (0 is allways the Menue)
arrMenu = [
    ['#ME', 'icons/menu.png', 'Menü', 'Menü'],
    [' ', 'icons/new_word.png', 'Neues Wort', 'Neues Wort'],
    ['#DL', 'icons/del_letter.png', 'letzter Buchstabe gelöscht', 'letzen Buchstaben löschen', 'keypressBackspace'],
    ['#DW', 'icons/del_word.png', 'letzes Wort gelöscht', 'letztes Wort löschen', 'keypressDelete'],
    ['#DS', 'icons/del_sentance.png', 'gesamter Satz gelöscht', 'gesamter Satz löschen', 'keypressHome'],
    ['#SS', 'icons/send_sentance.png', 'ich sage', 'Satz sagen', 'keypressEnd'],
    ['#MB', 'icons/menu_back.png', 'zurück', 'zurück', 'keypressEscape']
]
