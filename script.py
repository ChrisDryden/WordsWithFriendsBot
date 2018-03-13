# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:43:14 2018

@author: Chris Dryden
"""

#required libraries
import re
import numpy as np

#additional project libraries
import mousecommands
import screencapture


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

class base_words:
    horizontal = False
    word = ''
    wordlist = []
    coordinates = []
    def __init__(self, list_of_characters, orientation):
        for item in list_of_characters:
            self.addcharacter(item)
        self.horizontal = orientation
        self.createword()
    def addcharacter(self, object):
        character = object[0]
        x_coordinate = object[1]
        y_coordinate = object[2]
        self.wordlist.append(character)
        self.coordinates.append({x_coordinate,y_coordinate})
    def createword(self):
        self.word = "".join(self.wordlist)
    def word(self):
        return word
    def length(self):
        return len(wordlist)



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


def board_word_points():
    board = np.array([
            [0,0,0,3,0,0,0,0,0,0,0,3,0,0,0],#1
            [0,0,0,0,0,2,0,0,0,2,0,0,0,0,0],#2
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#3
            [3,0,0,0,0,0,0,2,0,0,0,0,0,0,3],#4
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#5
            [0,2,0,0,0,0,0,0,0,0,0,0,0,2,0],#6
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#7
            [0,0,0,2,0,0,0,0,0,0,0,2,0,0,0],#8
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#9
            [0,2,0,0,0,0,0,0,0,0,0,0,0,2,0],#10
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#11
            [3,0,0,0,0,0,0,2,0,0,0,0,0,0,3],#12
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#13
            [0,0,0,0,0,2,0,0,0,2,0,0,0,0,0],#14
            [0,0,0,3,0,0,0,0,0,0,0,3,0,0,0],#15
            ])
    print(board.shape)
    return board


def board_letter_points():
    board = np.array([
            [0,0,0,0,0,0,3,0,3,0,0,0,0,0,0],#1
            [0,0,2,0,0,0,0,0,0,0,0,0,2,0,0],#2
            [0,2,0,0,2,0,0,0,0,0,2,0,0,2,0],#3
            [0,0,0,3,0,0,0,0,0,0,0,3,0,0,0],#4
            [0,0,2,0,0,0,2,0,2,0,0,0,2,0,0],#5
            [0,0,0,0,0,3,0,0,0,3,0,0,0,0,0],#6
            [3,0,0,0,2,0,0,0,0,0,2,0,0,0,3],#7
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#8
            [3,0,0,0,2,0,0,0,0,0,2,0,0,0,3],#9
            [0,0,0,0,0,3,0,0,0,3,0,0,0,0,0],#10
            [0,0,2,0,0,0,2,0,2,0,0,0,2,0,0],#11
            [0,0,0,3,0,0,0,0,0,0,0,3,0,0,0],#12
            [0,2,0,0,2,0,0,0,0,0,2,0,0,2,0],#13
            [0,0,2,0,0,0,0,0,0,0,0,0,2,0,0],#14
            [0,0,0,0,0,0,3,0,3,0,0,0,0,0,0],#15
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
                stack.append((board[i,j], i, j))
            elif stack != []:
                basewords.append(stack)
                stack = []
        if basewords != []:
            horizontalwords = horizontalwords + basewords
            
    #Vertical Words: shifted i and j in the  board[]        
    for i in range(15):
        basewords = []
        stack = []
        for j in range(15):
            if board[j,i] != "~":
                stack.append((board[j,i], i, j))
            elif stack != []:
                basewords.append(stack)
                stack = []
        if basewords != []:
            verticalwords = verticalwords + basewords     
    horizontalwordsobjects = []
    verticalwordsobjects = []
    print("Vertical Words")
    print(verticalwords)
    print("Horizontal Words")
    print(horizontalwords)
    for item in verticalwords:
        objectword = base_words(item, False)
        verticalwordsobjects.append(objectword)
    for item in horizontalwords:
        objectword = base_words(item, True)
        horizontalwordsobjects.append(objectword)
    return horizontalwordsobjects, verticalwordsobjects #, verticalwords
    



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
    horizontal_words, verticalwords = determineBaseWords(board())
    print(horizontal_words)
    print(vertical_words)
    for word in horizontalwords:
        scrabblesearch(word)
    for word in verticalwords:
        scrabblesearch(word)



    
        
#scrabblesearch()
#board()
