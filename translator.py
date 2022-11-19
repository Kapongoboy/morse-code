class MorseCode:
    def __init__(self):
        self.letters: dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..',
                             'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                             'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
                             'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
                             'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                             'U':'..-', 'V':'...-', 'W':'.--','X':'-..-',
                             'Y':'-.--', 'Z':'--..',
        } 
        self.numbers: dict = {'1':'.----','2':'..---','3':'...--','4':'....-',
                        '5':'.....','6':'-....','7':'--...','8':'---..',
                        '9':'----.','0':'-----',' ':'   ',
                        }
        # self.sorted_letters = self.format_letters()


    def valid(self) -> bool:
        """The method checks whether the input message can be encoded or decoded

        Args:
            message (str): the string to encode or decode

        Returns:
            bool: True or False flag for whether the input is usuable
        """
        message = self.user_message.upper()
        check_list = [False for i in message if i not in self.letters.keys() and self.numbers.keys()]
        if len(check_list) != 0:
            return False
        else:
            return True
        
        
    def encode(self) -> str:
        """a simple morse code translator which takes an input string and prints the morse code translation

        Args:
            message (str): the string to translation

        Returns:
            str: the morse code equivalent of the message
        """
        message = self.user_message.upper()
        translation_buffer: list = []
        for char in message:
            if char in self.numbers:
                translation_buffer.append(self.numbers[char])
            else:
                translation_buffer.append(self.letters[char])
        self.translation = ''.join(translation_buffer)
        return f'The morse code encoding for your message is: \n{self.translation}'


    # def format_letters(self):
    #     return {k: v for k, v in sorted(self.letters.items(), key=lambda item: item[1])}
    def print_morse(self):
        self.user_message: str = input('\nPlease enter the message you would like to send: \n')
        if not self.valid():
            print("\nOops sorry, please don't include symbols or punction in your message\n")
            # self.user_message = input("\nOops sorry, please don't include symbols or punction in your message\n")
            self.print_morse()
        morse_code: str = self.encode()
        print(morse_code)

