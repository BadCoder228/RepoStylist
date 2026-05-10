from colorama.ansi import AnsiFore
from os import getlogin, system
from es3_modifier import ES3
from colorama import Fore
from time import sleep
from art import tprint
from json import dumps
from sys import exit

LE_PATH: str = f"C:/Users/{getlogin()}/AppData/LocalLow/semiwork/Repo/MetaSave.es3"
LE_PASSWORD: str = "Why would you want to cheat?... :o It's no fun. :') :'D"

def BeautifulString(word: str) -> str:
    return f"you need to type \"{word}\" in the console below."

def BannerPattern(color: AnsiFore, title: str, text: str):
    print(color)
    tprint(title)
    print(Fore.WHITE)
    print(text + "\n")

def Banner() -> None:
    system("cls")

    BannerPattern(Fore.MAGENTA, "R.E.P.O.   STYLIST", 
        f"\nIn order to unlock cosmetic items, {BeautifulString('meow')}\nIn order to leave, {BeautifulString('done')}\n\n(C) This program was written and developed by {Fore.YELLOW}Wormyy{Fore.WHITE}, no rights were reserved")

def Inject() -> None:
    try:
        with open(LE_PATH, 'rb') as f:
            file_data: ES3 = ES3(f.read(), LE_PASSWORD)
            data: dict = file_data.load()

        data["cosmeticUnlocks"]["value"] = list(range(1, 548))

        with open(LE_PATH, 'wb') as f:
            f.write(file_data.save(dumps(data)))

        print("\nSuccess! You may now close the window.")
        
    except Exception as e:
        print(f"\n{Fore.RED}[An error occurred!] {Fore.WHITE}Here's the error: {e}. Try to fix it. You may now close the window.")
    
    input()
    exit(0)

if __name__ == "__main__":
    
    while True:
        Banner(True)
        input_data: str = input(f"C:\\\\{getlogin()} >>> ")

        match(input_data):
            case "done":
                exit(0)

            case "meow":
                print("\n")
                                
                for i in range(10): #imitating the process... looks beautiful in my eyes, ngl
                    print(f"Hold on{'.' * i}", end="\r")
                    sleep(0.1)
                
                else:
                    Inject()
