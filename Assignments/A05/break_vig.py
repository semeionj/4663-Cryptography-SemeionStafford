from __future__ import division
from io import IncrementalNewlineDecoder
import sys
import os
import pprint
import json

ALPHABET = [chr(x+97) for x in range(26)]

def mykwargs(argv):
    '''
    Processes argv list into plain args (list) and kwargs (dict).
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}
        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
        Flags aren't handled at all. Maybe in the future but this function
            is meant to be simple.
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs

def usage(message=None):
    if message:
        print(message)
    print("Usage: python break_vig.py [input_file_name=string]")
    print("Example:\n\t python reak_vig.py filename.txt\n")
    sys.exit()

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


def crack(encrypted_text, dick, nchars):
    for key in dick:
        if len(key) - key.count(" ") - key.count("-") == nchars:
            print(key)
            convert(key, encrypted_text)

def keyLength(text):

    ###LENGTH 2
    ######################################
    index_c2 = 0.0
    key2 = []

    for i in range(0, len(text) - 1, 2):
        key2.append(text[i])
    num = 0
    den2 = len(key2) * (len(key2) - 1)
    for letter in ALPHABET:
        fi = (str(key2).count(letter))
        #print(letter, fi)
        num += fi * (fi - 1)
        
    index_c2 = num / den2
    
    print(index_c2, "2")
    ######################################

    ###LENGTH 3
    ######################################
    index_c3 = 0.0
    key3 = []

    for i in range(0, len(text) - 1, 3):
        key3.append(text[i])

    den3 = len(key3) * (len(key3) - 1)
    for letter in ALPHABET:
        fi = (str(key3).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c3 += num / den3
    
    print(index_c3, "3")
    ######################################

    ###LENGTH 4
    ######################################
    index_c4 = 0.0
    key4 = []

    for i in range(0, len(text) - 1, 4):
        key4.append(text[i])

    den4 = len(key4) * (len(key4) - 1)
    for letter in ALPHABET:
        fi = (str(key4).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c4 += num / den4
    
    print(index_c4, "4")
    ######################################

    ###LENGTH 5
    ######################################
    index_c5 = 0.0
    key5 = []

    for i in range(0, len(text) - 1, 5):
        key5.append(text[i])

    den5 = len(key5) * (len(key5) - 1)
    for letter in ALPHABET:
        fi = (str(key5).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c5 += num / den5
    
    print(index_c5, "5")
    ######################################

    ###LENGTH 6
    ######################################
    index_c6 = 0.0
    key6 = []

    for i in range(0, len(text) - 1, 6):
        key6.append(text[i])

    den6 = len(key6) * (len(key6) - 1)
    for letter in ALPHABET:
        fi = (str(key6).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c6 += num / den6
    
    print(index_c6, "6")
    ######################################

    ###LENGTH 7
    ######################################
    index_c7 = 0.0
    key7 = []

    for i in range(0, len(text) - 1, 7):
        key7.append(text[i])

    den7 = len(key7) * (len(key7) - 1)
    for letter in ALPHABET:
        fi = (str(key7).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c7 += num / den7
    
    print(index_c7, "7")
    ######################################

    ###LENGTH 8
    ######################################
    index_c8 = 0.0
    key8 = []

    for i in range(0, len(text) - 1, 8):
        key8.append(text[i])

    den8 = len(key8) * (len(key8) - 1)
    for letter in ALPHABET:
        fi = (str(key8).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c8 += num / den8
    
    print(index_c8, "8")
    ######################################

    ###LENGTH 9
    ######################################
    index_c9 = 0.0
    key9 = []

    for i in range(0, len(text) - 1, 9):
        key9.append(text[i])

    den9 = len(key9) * (len(key9) - 1)
    for letter in ALPHABET:
        fi = (str(key9).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c9 += num / den9
    
    print(index_c9, "9")
    ######################################

    ###LENGTH 10
    ######################################
    index_c10 = 0.0
    key10 = []

    for i in range(0, len(text) - 1, 10):
        key10.append(text[i])

    den10 = len(key10) * (len(key10) - 1)
    for letter in ALPHABET:
        fi = (str(key10).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c10 += num / den10
    
    print(index_c10, "10")
    ######################################

    ###LENGTH 11
    ######################################
    index_c11 = 0.0
    key11 = []

    for i in range(0, len(text) - 1, 11):
        key11.append(text[i])

    den11 = len(key11) * (len(key11) - 1)
    for letter in ALPHABET:
        fi = (str(key11).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c11 += num / den11
    
    print(index_c11, "11")
    ######################################

    ###LENGTH 12
    ######################################
    index_c12 = 0.0
    key12 = []

    for i in range(0, len(text) - 1, 12):
        key12.append(text[i])

    den12 = len(key12) * (len(key12) - 1)
    for letter in ALPHABET:
        fi = (str(key12).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c12 += num / den12
    
    print(index_c12, "12")
    ######################################

    ###LENGTH 13
    ######################################
    index_c13 = 0.0
    key13 = []

    for i in range(0, len(text) - 1, 13):
        key13.append(text[i])

    num = 0
    den13 = len(key13) * (len(key13) - 1)
    for letter in ALPHABET:
        fi = (str(key13).count(letter))
        #print(letter, fi)
        num += fi * (fi - 1)
    
    index_c13 = num / den13
    print(index_c13, "13")
    ######################################

    ###LENGTH 14
    ######################################
    index_c14 = 0.0
    key14 = []

    for i in range(0, len(text) - 1, 14):
        key14.append(text[i])

    den14 = len(key14) * (len(key14) - 1)
    for letter in ALPHABET:
        fi = (str(key14).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c14 += num / den14
    
    print(index_c14, "14")
    ######################################

    ###LENGTH 15
    ######################################
    index_c15 = 0.0
    key15 = []

    for i in range(0, len(text) - 1, 15):
        key15.append(text[i])

    den15 = len(key15) * (len(key15) - 1)
    for letter in ALPHABET:
        fi = (str(key15).count(letter))
        #print(letter, fi)
        num = fi * (fi - 1)
        index_c15 += num / den15
    
    print(index_c15, "15")
    ######################################

###############
#   METHOD 2
###############
def calculate_ic(ciphertext):

    letterFreq = []
    for letter in ALPHABET:
        letterFreq.append(encrypted_text.count(letter))

    N = len(ciphertext)

    IC = 0
    i = 1
    for l in letterFreq:
        ni = letterFreq[l]
        IC = IC + (ni*(ni-1))/(N*(N-1))
        print(IC, i)
        i += 1

def main(args, **kwarg):
    
    #Open dictionary
    with open('dictionary.json') as f:
        dick = json.load(f)
    

    #Cipher
    with open(args[0], "r") as file:
      encrypted_text = file.read().replace('\n', '')
    
    print(encrypted_text)

    encrypted_text = encrypted_text.lower()
    
    #keyLength(encrypted_text.replace(" ", ""))

    #Numerator
    num = 0.0

    #Characters in cipher
    N = 0.0

    #I.C.
    index_c = 0.0
    
    #Additional subtractions was to cater for a particular test case. Ignore
    N = len(encrypted_text) - encrypted_text.count(" ") - encrypted_text.count(".") - encrypted_text.count(":") - encrypted_text.count("-") - encrypted_text.count(",") - encrypted_text.count(")") - encrypted_text.count("(")
    den = N * (N - 1)

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

    #calculate_ic(encrypted_text)
    print("I.C. is ", index_c, "Number of chars is ", nchars)

    crack(encrypted_text, dick, nchars)

if __name__ == '__main__':
    required_params = 1 # adjust accordingly
    argv = sys.argv[1:] # strip file name (skeleton.py) out of args

    # print usage if not called correctly
    if len(argv) < required_params:
        usage()

    # get processed command line args
    args,kwargs = mykwargs(argv)

    main(args,**kwargs)