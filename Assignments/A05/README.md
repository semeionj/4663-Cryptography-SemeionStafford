#  Vigenere Cracking (A05) - Semeion Stafford
##  Incidence of Coincidence
### Overview
----------------------------------------------------------------------

This program attempts to crack a vigenere cipher by calculating the incidence of coincidence and and the key length. A dictionary is then used to try decoding the code with the words that are the same size.

----------------------------------------------------------------------

##### Method



|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [break_vig.py](./main.cpp)     | solution file.                                             |

Issues Faced:
Tried several methods for determining the actual key size. But eventually could not get it to work.

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | break_vig.py         | Main driver of my project that launches code.      |

### Instructions
- My program expects four parameters to be placed on the command line when you run the program.
- Parameters `<input file>`

- Example Command:
    - `python python adfgx.py inputfile
    - `python adfgx.py input.txt key1=superbad key2=hijack op=encrypt 
