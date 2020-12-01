#  NAME:        Semeion Stafford
#  REPO:        4663 Cyptography
#  EMAIL:       semeionsta@hotmail.com
#  ASSIGNMENT:  A03
#  WEBSITE:     https://repl.it/@SemeionStafford/A03#main.py

import sys
import os
import requests

alphabet = [chr(x+97) for x in range(26)]

#Original typical frequency
#Used to get first message translation
tfreqOrig = {0:"e",
        1:"t",
        2:"a",      
        3:"o",
        4:"i",
        5:"n",
        6:"s",
        7:"r",
        8:"h",
        9:"d",
        10:"l",
        11:"u",
        12:"c",
        13:"m",
        14:"f",
        15:"y",
        16:"w",
        17:"g",
        18:"p",
        19:"b",
        20:"v",
        21:"k",
        22:"x",
        23:"q",
        24:"j",
        25:"z"       
              }

#EDITED TYPICAL FREQUENCY TABLE
tfreq = {0:"e",
        1:"t",
        2:"a",      
        3:"o",
        4:"h",
        5:"r",
        6:"n",
        7:"i",
        8:"d",
        9:"s",
        10:"l",
        11:"c",
        12:"w",
        13:"g",
        14:"f",
        15:"v",
        16:"u",
        17:"p",
        18:"b",
        19:"m",
        20:"y",
        21:"k",
        22:"q",
        23:"x",
        24:"j",
        25:"z"       
              }

class Frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.sort_freq = None
        self.total = 0

        for l in alphabet:
            self.freq[l] = 0
    
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1
                self.total += 1

        # https://realpython.com/python-lambda/
        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    def printr(self):
        if self.sort_freq:
            for f in self.sort_freq:
                print(f"{f[0]}:{f[1]}")
        else:
            print(self.freq)

    def print_table(self):
        for i in range(5):
            for j in range(5):
                if j > 0:
                    print(" , ",end="")
                pct = (int(self.sort_freq[i*5+j][1])/self.total)*100
                pct = "{:5.2f}".format(pct)
                print(f"{self.sort_freq[i*5+j][0]}:{pct}%",end=" ")
            print("")

    def getNth(self,n):
        if self.sort_freq:
            return self.sort_freq[n][0]

        return None


if __name__=='__main__':
    #url = "https://github.com/rugbyprof/4663-Cryptography/blob/master/Assignments/A03/ciphertext_1.txt"
    #url = "https://www.gutenberg.org/files/2600/2600-0.txt"
    #print("Downloading book ...")
    #f = requests.get(url)

    text = ""
    f = open("ciphertext_1.txt", "r")
    for l in f:
      text = text + l

    print(text)

    print("Calculating frequency...")
    F = Frequency()

    F.count(text)

    F.print_table()
    
    #print(F.sort_freq[1][0])

    freq = {}
    freqOrig = {}

    for i in range(26):
      freq[F.sort_freq[i][0]] = tfreq[i]
      
      freqOrig[F.sort_freq[i][0]] = tfreqOrig[i]
      
    print(freq)

    text = str(text)
    newTextOrig = ""
    newText = ""

    for i in text:
      if i in freqOrig.keys():
        newTextOrig += freqOrig[i]
      else:
        newTextOrig += " "

    #Prints out new text based on typical substitutions
    for i in text:
      if i in freq.keys():
        newText += freq[i]
      else:
        newText += " "

    print("\n\n")
    print(newTextOrig)
    print("\n\n")
    print(newText)
