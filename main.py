from translator import MorseCode
from logo import logo
from clear import clear
from tui import *

coding: object = MorseCode()


def main():
    clear()
    logo()
    mode: str = sm()
    if mode == 'q':
        return
    elif mode == 'e':
        coding.print_morse()
    else:
        print('coming soon')
    try_again: str = input('Would you like to go continue using the Morse Code translator?\npress y to continue and anything else to quit\n')
    if try_again == 'y':
        main()
    else:
        return


main()
