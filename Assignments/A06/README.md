
#  4663-Cryptography (A06) - Semeion Stafford
##  Prime Factors
### Overview
----------------------------------------------------------------------

Given a large number, determine if it is prime or if it can be factored. If it can be factored print out the prime factors.

----------------------------------------------------------------------

##### Method
1. Read each number in from input file.
2. Determine if it is prime, or factorable
3. If it is prime write out "prime"
4. If it is factorable write out the factors.

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | get_factors.py         | Main driver of my project that launches code.      |
|   2   | numbers.txt         | text file with input      |


### Instructions
- My program expects one parameter to be placed on the command line when you run the program.
- Parameters `<input file>`
- The input file should be formatted with numbers on seperate line:

- Example Command:
    - `python python get_factors.py inputfile
    - `python get_factors.py numbers.txt

### Sources
-https://github.com/rtgdk/Breaking-Vigenere-Cipher/blob/master/cip.py
-http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher/
-https://www.mygeocachingprofile.com/codebreaker.vigenerecipher.aspx
