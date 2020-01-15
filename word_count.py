#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:56:12 2019

@author: jishanmsharif
"""
def main():
    f = open("newfile.txt", "r")
    if f.mode == "r":
        # text reads the file, the ouput is a string.
        text = f.read()
        # We are coverting the text into lowercase so words with uppercase letter is treated
        # the same way as words with lowercase.
        for specialcharecters in '.,-\n':
            # We are removing special charecters for homogenity. 
            texts = text.replace(specialcharecters,'')
        texts = text.lower()
        # split converts the string into a list using whitespace as separators. 
        words = texts.split(" ")
        # table is a dictionary.
        table = {}
        for word in words:
            # the value is assigned onto the variable count. 
            # table.get(word) returns the value to the key 'word'
            count = table.get(word)
            if count == None:
                # if the key does not exist, table[word] will be one.  
                # if the key does not exist, the key is created with the value being one. 
                table[word] = 1
            else: 
                # if the key exists, the value of the key is added to it's previous value.
                table[word] = 1 + table[word]

        newlist = []
        # items converts the value and the key into a tuple type.
        for (key,value) in table.items():
            # append adds the tuple onto the newlist. This is done 
            # because a list can only take values of the same type.
            newlist.append((value,key))
        newlist.sort()
        mostfrequentword = newlist.pop()
        print(mostfrequentword)
                        
    f.close()
if __name__== "__main__":
  main()        

    
        



