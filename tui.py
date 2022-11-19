# consider implementing this in the class for to use the public nature fo self.
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

