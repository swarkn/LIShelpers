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
strScreenGeometry = "320x200"
bolScreenFull = False

# Control how the letters should behave
intLettersInterval = 1000

# system icons
strImage_ArrowLeft = 'icons/arrow_left.png'
strImage_ArrowRight = 'icons/arrow_right.png'

# editing menue (0 is allways the Menue)
arrMenu = [
    ['ME', 'icons/menu.png'],
    ['NW', 'icons/new_word.png'],
    ['DL', 'icons/del_letter.png'],
    ['DW', 'icons/del_word.png'],
    ['DS', 'icons/del_sentance.png']
]
