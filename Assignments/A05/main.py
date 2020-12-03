from __future__ import division
from io import IncrementalNewlineDecoder
import sys
import os
import pprint
import json

ALPHABET = [chr(x+97) for x in range(26)]

def convert(word, encrypted_text):

    word_length =  len(word)

    mapp = []
    for i in range(len(word)):
        mapp.append(ord(word[i]) % 97)
    
    new_string = ""
    new_index = 0
    map_index = 0
    letter_index = 0
    for l in encrypted_text:
        if l == " ":
            new_string += " "
        else:
            letter_index = ord(l) % 97
            new_index = (letter_index - mapp[map_index]) % 26
            new_string += chr(new_index + 97)
            map_index = (map_index + 1) % word_length
        
    print(mapp)
    print(new_string)
    """ converted_string = ""
    int_convert = 0
    word_index = 0
    shift_val = 0
    for l in encrypted_text:
        shift_val = word[word_index]

        int_convert = ord(l) + word[word_index]
        int_convert = int_convert % 97
        converted_string += chr(int_convert)
    
    print(converted_string) """


def crack(encrypted_text):
    for key in dick:
        if len(key) - key.count(" ") - key.count("-") == nchars:
            print(key)
            convert(key, encrypted_text)



if __name__ == '__main__':
    
    #Open dictionary
    with open('dictionary.json') as f:
        dick = json.load(f)
    
    #Cipher
    encrypted_text = "tensw pez yqb xyimsg dmnv fhkz jbqn vgzb glmnmfwh"
    encrypted_text = encrypted_text.lower()
    
    #Numerator
    num = 0.0

    #Characters in cipher
    N = 0.0

    #I.C.
    index_c = 0.0
    
    #Additional subtractions was to cater for a particular test case. Ignore
    N = len(encrypted_text) - encrypted_text.count(" ") - encrypted_text.count(".") - encrypted_text.count(":") - encrypted_text.count("-") - encrypted_text.count(",") - encrypted_text.count(")") - encrypted_text.count("(")
    den = N * (N - 1)
    #print(N, den)

    avg = 0
    numavg = 0
    for letter in ALPHABET:
        fi = (encrypted_text.count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c += num / den
    
    nchars = 0
    if index_c >= 0.0660:
        nchars = 1;
    elif index_c >= 0.0520:
        nchars = 2;
    elif index_c >= 0.0473:
        nchars = 3;
    elif index_c >= 0.0449:
        nchars = 4;
    elif index_c >= 0.0435:
        nchars = 5;
    elif index_c >= 0.0426:
        nchars = 6;
    elif index_c >= 0.0419:
        nchars = 7;
    elif index_c >= 0.0414:
        nchars = 8;
    elif index_c >= 0.0410:
        nchars = 9;
    elif index_c >= 0.0407:
        nchars = 10;
    else:
        nchars = 0;

    
    print("I.C. is ", index_c, "Number of chars is ", nchars)

    crack(encrypted_text)