# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:43:14 2018

@author: Chris Dryden
"""
import re




pointsmatch




endstring = "\n"
letters = "wi\n"
containedletters = "no"
finalword = []
longest = 0

def validword(string, word):
    letters = list(string)
    for i in list(word):
        if i in letters:
            letters.remove(i)
        else:
            return False
    return True


def scrabblesearch():
    f = open('words_alpha.txt', 'r')
    longest = 0
    longestword = []
    searchlist = []
    for word in f:
        if containedletters in word:
            searchlist.append(word)
    print(searchlist)
    for word in searchlist:
        if(validword(letters+containedletters, word)):
            print(word)
            length = len(word)
            print(length)
            if length == longest:
                longestword.append(word)
            if length > longest:
                longestword = []
                longestword.append(word)
                longest = length
    print("longest word is " + str(longestword))
        
    
        
    
def oldsearch():
    for word in f:
        if re.match("^[abcdef]*$", word):
            length = len(word)
            if length == longest:
                longestword.append(word)
            if length > longest:
                longestword = []
                longestword.append(word)
                longest = length
scrabblesearch()

