#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:56:12 2019

@author: jishanmsharif
"""

#f = open("newfile.txt","w+")
#for i in range(10):
    #print("This is line \n" (i +1))

#How to use a dictionary in this scenario?
#Built in input function allows users to interact with the program
#str converts the added text into a string
loop = "Yes"
while loop == "Yes":
    text = str(input("Enter text here"))
    if text == "x":
        break 
#any unique charecter is converted to an empty space
#This is so that the program doesn't count these charecters as a separate word
    for char in '-,.\n':
        text = text.replace(char, ' ')
    text = text.lower()
#text is converted to lower case letters for consistency
    text_list = text.split()
#split converts the text into a list of words
    new_dict= {}
    for word in text_list:
        new_dict[word] = new_dict.get(word,0)+1
    new_list = []
    for (value,key) in new_dict.items():
       new_list.append((value,key))
    new_list.sort()
    print(new_list)
    

   
    


