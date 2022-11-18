from translator import MorseCode
from logo import logo
from clear import clear


def print_morse():
    coding: object = MorseCode()
    user_message: str = input('\nPlease enter the message you would like to send: \n')
    while not coding.valid(user_message):
        user_message = input("\nOops sorry, please don't include symbols or punction in your message\n")
    morse_code: str = coding.translate(user_message)
    print(morse_code)


def state_check(state:str):
    if (state != 'q') and (state !=  'e') and (state !=  'd'):
        state: str = input('please enter a valid option\n')
        state_check(state=state)
    return state

def sm():
    print('\nWelcome to my morse code translator \nShow off to your friends that you know "I love you" in morse code')
    state_buff: str = input('\nPress q to quit   e to encode to morse    d to decode from morse\n')
    state: str = state_check(state=state_buff)
    return state


def main():
    clear()
    logo()
    mode: str = sm()
    if mode == 'q':
        return
    elif mode == 'e':
        print_morse()
    else:
        print('coming soon')
    try_again: str = input('Would you like to go continue using the Morse Code translator?\ny/n\n')
    if try_again == 'y':
        main()
    else:
        return


main = main()