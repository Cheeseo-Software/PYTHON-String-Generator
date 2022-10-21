from colorama import init
from colorama import Fore, Back, Style
import os
import random
import string
from random_word import RandomWords
from random import seed
from random import randint

init()

print("\n\n" + Fore.LIGHTCYAN_EX + f"    [ 1 ]" + Fore.RESET + " STRING GENERATOR" + Fore.LIGHTCYAN_EX + f"    [ 2 ]" + Fore.RESET + " WORD GENERATOR" + Fore.LIGHTCYAN_EX + f"    [ 3 ]" + Fore.RESET + " NUMBER GENERATOR")

choice = input("\n    Selection: ")

if choice == "1":
    os.system("cls")
    shift = input(f"\n {Fore.LIGHTMAGENTA_EX} [ REQUIRED ] {Fore.RESET} | How many characters? ")

    ASCUP = string.ascii_uppercase
    STRING = (''.join(random.choice(ASCUP) for i in range(int(shift))) )

    os.system("cls")

    print(f"\n {Fore.LIGHTCYAN_EX} [ RANDOM-STRING ] {Fore.RESET} | {STRING}")
    input("")

if choice == "2":
    os.system("cls")
    random_words = RandomWords()
    os.system("cls")

    print(f"\n {Fore.LIGHTCYAN_EX} [ RANDOM-WORD ] {Fore.RESET} | {random_words.get_random_word()}")
    input("")

if choice == "3":
    os.system("cls")

    froma = input(f"\n {Fore.LIGHTMAGENTA_EX} [ REQUIRED ] {Fore.RESET} | From what number? ")
    to = input(f"\n {Fore.LIGHTMAGENTA_EX} [ REQUIRED ] {Fore.RESET} | To what number? ")

    value = randint(int(froma), int(to))

    os.system("cls")

    print(f"\n {Fore.LIGHTCYAN_EX} [ RANDOM-NUMBER ] {Fore.RESET} | {value}")
    input("")