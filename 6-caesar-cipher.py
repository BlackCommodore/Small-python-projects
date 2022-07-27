"""Caesar cipher, author: Al Sweigart"""

try:
    import pyperclip  # import copy to clipboard library
except ImportError:
    pass

SYMBOLS = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUWXYZŹŻ'

# User choose to encrypt or decrypt message
while True:  # ask until user put correct answer
    print('Do you want (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encryption'
        break
    elif response.startswith('d'):
        mode = 'decryption'
        break
    print('Please write "e" or "d" ')

# user determines key
while True:  # ask till input is correct key
    maxKey = len(SYMBOLS) - 1  # len(SYMBOLS) is like 0 the same output
    print(f'Please write key (from 0 to {maxKey})')
    response = input('> ')
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# user write message to encrypt/decrypt
print(f'Write message to {mode}')
message = input('> ')

# Caesar cipher works only on capital letters'
message = message.upper()

# save encrypted/decrypted message
translated = ""

# decrypt/encrypt every letter in message
for symbol in message:
    if symbol in SYMBOLS:
        # find decrypted/encrypted number for symbol
        num = SYMBOLS.find(symbol)
        if mode == 'encryption':
            num = num + key
        else:
            num = num - key

        # numbers fix if num < 0 or num > len(SYMBOLS)
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # add encrypted/decrypted number of symbol to variable 'translated'
        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol  # symbols are the same

# print on screen encrypted/decrypted text
print(translated)

try:
    pyperclip.copy(translated)
    print(f'Text to {mode} was copied to the clipboard')
except:
    print("Download pypetclip to copy to the clipboard")