#  Name:        Semeion Stafford
#  Repo:        4663 Cyptography
#  Email:       semeionsta@hotmail.com
#  Assignment:  A04
#  Website:     https://github.com/semeionj/4663-Cryptography
"""
    This file implements a class that creates a Adfgx lookup table using a keyword
    to build a polybuis square of format:
                      A D F G X
                    A s u p e r
                    D b a t z y
                    F c d f g h
                    G i k l m n
                    X o q v w x
    And then a dictionary lookup
"""
import sys
import pprint as pp
import os

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
    print("Usage: python adfgx.py [input_file_name=string] [keyword1=string] [keyword2=string] op=[encrypt,decrypt]")
    print("Example:\n\t python adfgx.py filename.txt arg1 arg2 decrypt\n")
    sys.exit()

class AdfgxLookup:
    def __init__(self, k=None):
        self.key = self.remove_duplicates(k)

        self.alphabet = [chr(x+97) for x in range(26)]
        self.adfgx = ['A', 'D', 'F', 'G', 'X']
        self.keylen = 0

        if self.key:
            self.keylen = len(self.key)

        self.polybius = None
        self.lookup = None

    def remove_duplicates(self, key):
        """ Removes duplicate letters from a given key, since they
            will break the encryption.
            Example:
                key = 'helloworldhowareyou'
                returns 'helowrdayu'
        """
        newkey = []             # create a list for letters
        for i in key:           # loop through key
            if not i in newkey:  # skip duplicates
                newkey.append(i)

        # create a string by joining the newkey list as a string
        return ''.join(str(x) for x in newkey)

    def build_polybius_string(self, key=None):
        """Builds a string consisting of a keyword + the remaining
           letters of the alphabet.
           Example:
                key = 'superbatzy'
                polybius = 'superbatzycdfghiklmnoqvwx'
        """
        # no key passed in, used one from constructor
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # key exists ... continue
        self.keylen = len(self.key)

        # prime polybius_string variable with key
        self.polybius = self.key

        for l in self.alphabet:
            if l == 'j':        # no j needed!
                continue
            if not l in self.key:    # if letter not in key, add it
                self.polybius += l
        return self.polybius

    def build_polybius_lookup(self, key=None):
        """ Builds a lookup dictionary so we can get the two letter pairs for each
            polybius letter.
            Example:
                key = superbatzy
                polybius = superbatzycdfghiklmnoqvwx
                lookup =
                {'a': 'DD',
                'b': 'DA',
                'c': 'FA',
                'd': 'FD',
                'e': 'AG',
                'f': 'FF',
                'g': 'FG',
                'h': 'FX',
                'i': 'GA',
                'k': 'GD',
                'l': 'GF',
                'm': 'GG',
                'n': 'GX',
                'o': 'XA',
                'p': 'AF',
                'q': 'XD',
                'r': 'AX',
                's': 'AA',
                't': 'DF',
                'u': 'AD',
                'v': 'XF',
                'w': 'XG',
                'x': 'XX',
                'y': 'DX',
                'z': 'DG'}
        """
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        # init our dictionary
        self.lookup = {}            # dict as our adfgx reverse lookup
        for l in self.polybius:     # loop through the 1D matrix we created
            self.lookup[l] = ''     # init keys in the dictionary

        row = 0
        col = 0

        # loop through the polybius 1D string and get the 2 letter pairs
        # needed to do the initial encryption
        for row in range(5):
            for col in range(5):
                i = (5 * row) + col
                self.lookup[self.polybius[i]] = self.adfgx[row]+self.adfgx[col]

        return self.lookup

    def make_sense(self, decrypt):
      x = 0
      y = 1
      english = ""
      message_length = int(len(decrypt)/2)

      for i in range(message_length):
        pair = decrypt[x] + decrypt[y]
        for k, v in self.lookup.items():
          if v == pair:
            english += k
            x = x + 2
            y = y + 2
            break
      return english

    """
        Decryption Funtion
        REQUIRES: first key, second key, and encrypted text
        RETURNS: The fully decrypted english text
    """

    def decrypt(self, key1, key2, decryp):

    # Same logic as encrypt (see encrypt.)
      cols = len(key2)
      rows = int(len(decryp)/cols) + 1

      if len(decryp) % cols != 0:
        rows = rows + 1

      arr = [["" for i in range(cols)] for j in range(rows)]

    # Figure out the rows and how many short columns.
    # Griffin Code... idk why it works but yeah.
      short_cols = len(key2) - ((len(decryp)) % len(key2))

    # Based on the key 2 word, lets make an array that stores its letters
    # And their index. Example hijack give (0, h), (1, i), (2, j), (3, a)... etc
      a = 0
      key2_list = []
      for b in key2:
        key2_list.insert(a, b)
        a = a + 1

    # Load keyword in first row
      i = 0
      for l in sorted(key2):
        arr[0][i] = l
        i = i + 1

    # Okay so this is basically the highest index we can go to. Whatever it is can be implemented with a
    # (row - 1) condition, yes. But it was just easier to use when its an actual variable
      hiC = cols - 1
      hiR = rows - 1

    # Array that stores which are the short columns
      actual_short = []

      for k in range(short_cols):
        # The short rows would obviously start from the end of the word
        actual_short.insert(k, key2_list[hiC])
        hiC = hiC - 1  # however many

    # This block of code fills the short column spaces with a "0". This could be joined with the above for loop
    # Seperated them for readability purposes.
      i = 0
      for k in range(short_cols):   # For however number of short rows we have
        for j in range(cols):       # We need to go column by column to check the condition
          if arr[0][j] == actual_short[i]:  # Condition is if the first row values are equal
            arr[hiR][j] = "0"               # to that particular short column value. It checks
            break                           # each column against each short column value
        i = i + 1


    # Loads thestring into the blocks that are free
      c = 0
      i = 0
      for y in range(cols):
        for x in range(1, rows):
          if (arr[x][y] != "0") and (i < len(decryp)):    #Once there isn't a zero and there are more letters
            arr[x][y] = decryp[i]
            i = i + 1
          else:
            arr[x][y] = " "     #Replaces the zeroes with a space. Could've used strip(0)... but why not.

      print("Recreated")        #This is the matrix we recreated
      pp.pprint(arr)
      print("\n")

      arr2 = [["" for i in range(cols)] for j in range(rows)]

      for c in range(cols):
        letter = arr[0][c]
        letter_index = key2_list.index(letter)  # correct col index
        for d in range(rows):
          arr2[d][letter_index] = arr[d][c]

      result = ""
      for m in range(1, rows):
        for n in range(cols):
          result += arr2[m][n]

      print("ORDER")
      pp.pprint(arr2)
      print("\n")
      print("Result:", result)
      return(self.make_sense(result))

    """
        Encryption Funtion
        REQUIRES: second key, and word to encrypt
        RETURNS: The fully encrypted ADGFX text 
    """
    def encrypt(self, key2, word):

      encrypted = ""

    # This loop reads the polybius square to begin encryption process
    # And creates a string based on the original word inputed.
      for l in word:
        encrypted += self.pull(l)

    # Calculate the number of rows and columns we need based on the size of keyword 2
    # Add an additional row to account for the "header" of the table
      cols = len(key2)
      rows = int(len(encrypted)/cols) + 1

    # If the word doesn't perfectly fit the square and there are rows not filled
    # Add another row to account for the "ceiling value". That is, if there are 24 letters
    # And the keyword is 5, 24/5 leaves us with four rows. 4 rows * 5columns leave us with 20
    # Blocks. So we need an extra row for the remaining 4 letters.
      if len(encrypted) % cols != 0:
        rows = rows + 1

    # Arrays we are going to use to do the crazy stuff
    # The first one is based the dimentions just calculated
    # The second one has inverted dimentions
      arr = [["" for i in range(cols)] for j in range(rows)]
      arr2 = [["" for i in range(rows)] for j in range(cols)]

      r = 0
      c = 0
      i = 0

    # Let's load the keyword into first row
      for l in key2:
        arr[0][i] = l
        i = i + 1

    # Load encrypted text into the remainder of rows
      for l in encrypted:
        if (c >= cols):         #if we're at the far right end of the array
          r = r+1               #go to the next row to continue loading
          c = 0                 #we want load from the left of array
        arr[r + 1][c] = l       #insert value... factoring the first row +1 as a sorta dummy
        c = c+1                 #Next column --->>>>>>>

      print("Initial Array")
      pp.pprint(arr)            #This is going to show you the array after we load em up
      print("\n")

    # Flip arrays. We are loading the first array into the second array as line 264.
    # Why? Made it easier to fractionate/sort the rows alphabetically by the keyword later on
      for x in range(rows):
        for y in range(cols):
          arr2[y][x] = arr[x][y]

    # Sort columns of the array. Basically sorts all the rows based on that first index value.
    # First index value in row was previously the column headers so we can get them in alphabetical 
    # Qrder now
      arr2 = sorted(arr2)

    # Lets copy it back to its original form (dimentions)
      for x in range(rows):
        for y in range(cols):
          arr[x][y] = arr2[y][x]
      
      print("Fractioning...")   #This is how it looks after fractionating
      pp.pprint(arr)
      print("\n")


    # Reads the final array column by column to store to a string. This is the final encrypted text
      r = 1
      c = 0
      final = ""
      for a in range(cols):
        for b in range(1, rows):
          final += arr[b][a]
      
    # Send answer to main
      return final

    """
        Pull Funtion
        REQUIRES: key
        RETURNS: the 2 characted representation using the ADFGX lookup table
    """
    def pull(self, key):
      return self.lookup[key]

    def sanity_check(self):
        """ This method lets you look at an actual "matrix" that you built using 
            a keyword. 
            Example: 
                key = 'superbatzy'
                output = 
                      A D F G X 
                    A s u p e r 
                    D b a t z y 
                    F c d f g h 
                    G i k l m n 
                    X o q v w x 
            This is not what you would use to encrypt!! Its only a sanity check
            meaning that it visualizes the lookup table just to see proof it's correct.
        """

        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        row = 0
        col = 0

        sys.stdout.write('\n  ')
        for l in self.adfgx:
            sys.stdout.write(l+' ')
        sys.stdout.write('\n')
        for l in self.adfgx:
            sys.stdout.write(l+' ')
            for ll in self.adfgx:
                i = (5 * row) + col
                sys.stdout.write(self.polybius[i]+' ')
                col += 1
            row += 1
            col = 0
            sys.stdout.write("\n")


def main(args, **kwargs):
    #     A D F G X
    # A | p h q g m
    # D | e a y n o
    # F | f d x k r
    # G | c v s z w
    # X | b u t i l
    
    print(kwargs, "ARG")
    op = kwargs["op"]
    key1 = kwargs["key1"]
    key2 = kwargs["key2"]

    with open(args[0], "r") as file:
      word = file.read().replace('\n', '')

    word_encrypt = ""
    key2_encrypt = ""

    # init and input my keyword
    A = AdfgxLookup(key1)

    # build my lookup table
    lookup = A.build_polybius_lookup()

    # print out my adfgx lookup table
    # pp.pprint(lookup)

    if op == "encrypt":
      # ENCRYPT
      encrypt = A.encrypt(key2, word)
      print("Encrypted text", encrypt)
    elif op == "decrypt":
      # DECRYPT
      decrypt = A.decrypt(key1, key2, word)
      print("Converted to english is", decrypt)

if __name__ == '__main__':

  required_params = 4 # adjust accordingly
  argv = sys.argv[1:] # strip file name (skeleton.py) out of args

  # print usage if not called correctly
  if len(argv) < required_params:
      usage()

  # get processed command line args
  args,kwargs = mykwargs(argv)

  main(args,**kwargs)
