# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:43:14 2018

@author: Chris Dryden
"""
import re
import numpy as np

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

#
#Sidenote corner case: if a word can be extended by another word and then another word is made off of that
#
#To-Do List:
# - add the position of the longest word
# - begin the integration of triple words on the board
#
#
#

endstring = ""
finalword = []
longest = 0


def board():
    board = np.array([
            ["~","h","e","l","~","~","a","n","d","~","~","~","~","~","~"],#1
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#2
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#3
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#4
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#5
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#6
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#7
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#8
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#9
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#10
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#11
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#12
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#13
            ["~","~","~","~","~","~","~","~","~","~","~","~","~","~","~"],#14
            ["~","~","~","~","~","~","~","~","~","~","~","~","a","~","~"],#15
            ])
    print(board.shape)
    return board


def determineBaseWords(board):
    horizontalwords = []
    verticalwords = []

    #Horizontal Words
    for i in range(15):
        basewords = []
        stack = []
        for j in range(15):
            if board[i,j] != "~":
                stack.append(board[i,j])
            elif stack != []:
                basewords.append(''.join(stack))
                stack = []
        if basewords != []:
            horizontalwords = horizontalwords + basewords
            
    #Vertical Words: shifted i and j in the  board[]        
    for i in range(15):
        basewords = []
        stack = []
        for j in range(15):
            if board[j,i] != "~":
                stack.append(board[j,i])
            elif stack != []:
                basewords.append(''.join(stack))
                stack = []
        if basewords != []:
            verticalwords = verticalwords + basewords     
    
    return horizontalwords #, verticalwords
    



def pointsmatch(word):
    totalscore = 0
    for i in list(word):
        totalscore = totalscore +  score[i]
    return totalscore


def validword(string, word):
    letters = list(string)
    for i in list(word):
        if i in letters:
            letters.remove(i)
        else:
            return False
    return True


def scrabblesearch(containedletters):
    f = open('words_alpha.txt', 'r')
    highestpoints = 0
    bestword = []
    searchlist = []
    for word in f:
        if containedletters in word:
            searchlist.append(word)
    searchlist = [word[:-1] for word in searchlist]
    for word in searchlist:
        if(validword(letters+containedletters, word)):
            points = pointsmatch(word)
            if points == highestpoints:
                bestword.append(word)
            if points > highestpoints:
                bestword = []
                bestword.append(word)
                highestpoints = points
    print("for " + containedletters + " the highest points is " + str(bestword))
    

if __name__ == "__main__":
    letters = "smaoeu"
    basewords = determineBaseWords(board())
    print(basewords)
    for word in basewords:
        scrabblesearch(word)


    
        
#scrabblesearch()
#board()
