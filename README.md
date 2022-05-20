# ransomware
a python script that encrypts files on a linux machine. also includes the decrypt code

running voldemort.py will first generate a key and save it as thekey.key . 
the code then checks for all files in the directory it is present in, and adds them to a list which is named as "files"
using Fernet, files in "files" are encrypted with the key.

running harry.py is the opposite. 
the code checks for all the files in the directory.
using Fernet, the files are decrypted, using thekey.key. 
as an added bonus, the piece of code which decrypts the files, is placed under an if else loop, and only runs when the user inputs the correct passcode.
