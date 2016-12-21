#!/usr/bin/python3
import string

# String off possible characters to be shown for spelling
strABC = string.ascii_uppercase[:26]

# Manual string off max. screen resolution (double "" to otherwise let tk detect the max resolution)
strScreenGeometry = "320x200"
bolScreenFull = False

# Control how the letters should behave
intLettersInterval = 1000
