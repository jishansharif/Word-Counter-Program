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
        # split converts the string into a list using whitespace as separators. 
        words = text.split(" ")
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

        # We initialize a new list.
        newlist = []
        # items converts the value and the key into a tuple type.
        for (value,key) in table.items():
            # append adds the tuple onto the newlist. This is done 
            # because a list can only take values of the same type.
            newlist.append((value,key))
            # We can now sort the list
        newlist.sort()
        # The most used word is now assigned to the variable mostusedword.
        mostusedword = newlist[0]
        print(mostusedword)
                        
    f.close()
if __name__== "__main__":
  main()        

    
        



