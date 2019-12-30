#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:56:12 2019

@author: jishanmsharif
"""

text = str(input("Enter text here"))
loop = "Yes"
while loop == "Yes":
    for char in '-,.\n':
        text = text.replace(char, ' ')
    text = text.lower()
    text_list = text.split()
    length_list = len(text_list)
    print(length_list)
    loop = input("Enter new text here, Type \"Yes\" to continue")
