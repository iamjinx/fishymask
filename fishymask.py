import os
from requests import post

# - > Cheaks Url
def urlcheck(string):
    if 'http://' not in string and 'https://' not in string:
            print(f"{ERR}\n Invalid Url !!! Insert Url with http or https \n\n{RESET}")
            exit()

# - > Shorts Url
def short(url):
    is_gd = post(f"https://is.gd/create.php?format=json&url={url}").json()['shorturl'].replace("https://",'@')
    return is_gd

# - > USED COLORS
RESET='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
NOC = '\033[0;37m' + '\033[46m'
SUC = '\033[0;37m' + '\033[42m'
ERR = '\033[0;37m' + '\033[41m'

header = """
█▀▀ █ █▀ █ █ █▄█ █▀▄▀█ █▀█ █▀ █▄▀
█▀  █ ▄█ █▀█  █  █ ▀ █ █▀█ ▄█ █ █
"""
hint = "\nType keywords like : Insta-auto-likes, free-coins.\nDon't Use spaces just use '-' between the keywords."

if __name__ == "__main__":
    os.system('cls||clear')
    print(f"{GREEN}{header}{RESET}")
    print(f"{ERR} Phishing URL : {RESET}", end=' ')
    phish = input()
    urlcheck(phish)

    print(f"{ERR}\n Masking Domain URL : {RESET}", end=' ')
    md = input()
    urlcheck(md)

    print(f"{RED}{hint}{RESET}")

    while True:
        print(f"{ERR}\n Keywords : {RESET}", end=' ')
        seword = input()         # - > Takes Keywords
        if seword != '':
            break
    try:
        link = short(phish) 
    except:     # - > Error Handeling
        print(f"{ERR}\n Internet Connection Failed ! \n\n{RESET}")
        exit()

    print(f"{SUC}\n Masked URL : {RESET}",end=' ')
    print(f"{md}-{seword}{link}\n\n")
