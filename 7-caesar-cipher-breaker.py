""" caesar cipher breaker, author: Al Sweigart"""

# user write sentence to decrypt
print('Write down sentence encrypted by Caesar cipher to reveal')
message = input('> ')

SYMBOLS = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUWXYZŹŻ '  # equal to encryption version of program

for key in range(len(SYMBOLS)):  # checking every single key
    translated = ""

    # decrypt every symbol in message
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # find number of symbol
            num = num - key

            # num correction for num < 0
            if num < 0:
                num += len(SYMBOLS)

            # add decrypted text to 'tanslated' variable
            translated += SYMBOLS[num]
        else:
            translated += symbol

    # print key and decrypted text
    print(f'Key: {key}, text: {translated}')