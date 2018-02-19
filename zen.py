#!/usr/bin/env python3
import codecs
import os
import shutil
from this import s

# get columns (c) and rows (r) of terminal
c, r = shutil.get_terminal_size()

# importing 'this' prints Zen of Python
# so clear screen
os.system('clear')

# s is rot13 encoded
s = codecs.decode(s, 'rot13')
s = s.split("\n")
for line in s:
    # print centered to terminal
    print(line.center(c, " "))
