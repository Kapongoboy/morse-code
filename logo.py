from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

def logo():
    cprint(figlet_format('MORSE CODE', font='starwars'),
       'white', attrs=['bold'])