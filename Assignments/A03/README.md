#   Frequency Analysis (A03) - Semeion Stafford
##  Using Typical Letter Frequency Distribution
### Overview
----------------------------------------------------------------------

This program decrypts a text file using a substitution cipher. A frequency analysis is ran on the letters and the typical Letter distribution for the english language is used to crack the text. Since the key was not given, just using the typical distribution does not work. So in the decryption process, we would need to figure out the additional mappings for each letter used.

----------------------------------------------------------------------

##### Method
After the initial substitution is done, I analyed the text by hand and made the most likely substitutions. For example, seeing a word like "tae" could most likely mean that the 'a' is in the wrong position and should be mapped to a 'h' instead. Using these "proximity guesses" allowed me to bit by bit decrypt what the message said. For both the cypher texts, an updated frequency distribution table was subsequently used in order to decrypt the text file. Only one is showed in the python file for brevity, but the PDF here (https://github.com/semeionj/4663-Cryptography-SemeionStafford/blob/master/Assignments/A03/A03.pdf) lists what changes were made.

Issues Faced:
Originally expected the typically frequency substitution to crack code, before I realized that it had to be further edited.
