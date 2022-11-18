from translator import MorseCode

coding: object = MorseCode()
user_message: str = input('Please enter the message you would like to send: \n')
morse_code: str = coding.translate(user_message)
print(morse_code)