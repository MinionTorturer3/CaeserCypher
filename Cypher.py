def cipherAlg(inputText, shiftNumber):
    ans = ""
    for i in range(len(inputText)):
        char = inputText[i]
        if char == " ":
            ans += " "
        #Encrypts character if it is an upper case letter
        elif (char.isupper()):
            ans += chr((ord(char) + shiftNumber - 65) % 26 + 65)
        #Encrypts Character if it is lower case
        else:
            ans += chr((ord(char)+ shiftNumber - 97) % 26 + 97)
    return ans

inputText = input("What do you want to Encrypt: ")
shiftNumber = #Input how much you want to shift characters here
print("Plain Text  is: " + inputText)
print("Shift Number is: " + str(shiftNumber))
print("Encrytption is: " +  cipherAlg(inputText, shiftNumber))