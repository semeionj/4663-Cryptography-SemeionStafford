#  ADFGX Implementation (A04) - Semeion Stafford
##  Using Typical Letter Frequency Distribution
### Overview
----------------------------------------------------------------------

This program implements an ADFGX ciper decoder, and encoder using fractionating transposition and a modified Polybius square with a single columnar transposition (See more: http://practicalcryptography.com/ciphers/adfgx-cipher/). All the steps for the column operations are displayed when the program runs 

----------------------------------------------------------------------

##### Method
1. Build a table like the following with the key square. This is known as a polybius square.

    A D F G X
A | p h q g m 
D | e a y n o 
F | f d x k r
G | c v s z w 
X | b u t i l

2. Encode the plaintext using this matrix, to encode the laetter 'a', locate it in the matrix and read off the letter on the far left side on the same row, followed by the letter at the top in the same column. In this way each plaintext letter is replaced by two cipher text letters. E.g. 'attack' -> 'DD XF XF DD GA FG'. The ciphertext is now twice as long as the original plaintext. Note that so far, it is just a simple substitution cipher, and trivial to break.

3. Write the code word with the enciphered plaintext underneath e.g.

G E R M A N
D D X F X F
D D G A F G

4. Perform a columnar transposition. Sort the code word alphabetically, moving the columns as you go. Note that the letter pairs that make up each letter get split apart during this step, this is called fractionating.

A E G M N R
X D D F F X
F D D A G G

5. Read the final ciphertext off in columns.

-> XF DD DD FA FG XG


|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [adfgx.cpp](./main.cpp)     | solution file.                                             |

Issues Faced:
Originally expected the typically frequency substitution to crack code, before I realized that it had to be further edited.

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | adfgx.cpp         | Main driver of my project that launches code.      |

### Instructions
- My program expects four parameters to be placed on the command line when you run the program.
- Parameters `<input file> <keyword1> <keyword2> <operation>`

- Example Command:
    - `python python adfgx.py decrypt.txt key1=superbad key2=hijack op=decrypt
    - `python adfgx.py encrypt.txt key1=superbad key2=hijack op=encrypt 
