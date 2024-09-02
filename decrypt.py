encryptText = input("Input encrypted Text: ")
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for test in range(len(Alphabet)):
    decrypt = ''
    for char in encryptText:
        if char in Alphabet:
            numeral = Alphabet.find(char)
            numeral = numeral - test
            if numeral < 0:
                numeral = numeral +len(Alphabet)
            decrypt = decrypt + Alphabet[numeral]
        else:
            decrypt = decrypt + char
    print('Hacking Test is %s: %s' % (test, decrypt))