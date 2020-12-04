#  Vigenere Cracking (A05) - Semeion Stafford
##  Incidence of Coincidence
### Overview
----------------------------------------------------------------------

This program attempts to crack a vigenere cipher by calculating the incidence of coincidence and and the key length. A dictionary is then used to try decoding the code with the words that are the same size.

----------------------------------------------------------------------

##### Method
Using the dictionary provided here and the newly discovered keylength, find all words in the dictionary of same length and proceed to brute force your way into decrypting the ciphertext.

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | break_vig.py         | Main driver of my project that launches code.      |
|   2   | decrypted.txt         | Decrption when manual key size of 7 is entered      |
|   3   | dictionary.json         | JSON file with dictoionary words and definitions      |
|   4   | plaintext.txt         | Plain text for decrypted.txt      |


Issues Faced:
Tried several methods for determining the actual key size. But eventually could not get it to work.

### Instructions
- My program expects four parameters to be placed on the command line when you run the program.
- Parameters `<input file>`

- Example Command:
    - `python python adfgx.py inputfile
    - `python adfgx.py input.txt key1=superbad key2=hijack op=encrypt 
