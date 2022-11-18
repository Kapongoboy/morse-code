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

        
    # def format_letters(self):
    #     return {k: v for k, v in sorted(self.letters.items(), key=lambda item: item[1])}
    def valid(self, message: str) -> bool:
        """The method checks whether the input message can be encoded or decoded

        Args:
            message (str): the string to encode or decode

        Returns:
            bool: True or False flag for whether the input is usuable
        """
        try:
            message = message.upper()
        except AttributeError:
            pass
        check_list = [False for i in message if i not in self.letters.keys() and self.numbers.keys()]
        if len(check_list) != 0:
            return False
        else:
            return True
        
    def translate(self, message: str) -> str:
        """a simple morse code translator which takes an input string and prints the morse code translation

        Args:
            message (str): the string to translation

        Returns:
            str: the morse code equivalent of the message
        """
        message = message.upper()
        translation_buffer: list = []
        for char in message:
            if char in self.numbers:
                translation_buffer.append(self.numbers[char])
            else:
                translation_buffer.append(self.letters[char])
        self.translation = ''.join(translation_buffer)
        return f'The morse code encoding for your message is: \n{self.translation}'
                