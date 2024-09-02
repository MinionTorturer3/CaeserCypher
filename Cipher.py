def cipherAlg(inputText, shiftNumber):
    ans = ""
    for i in range(len(inputText)):
        char = inputText[i]
        if char == " ":
            ans += " "
        elif (char.isupper()):
            ans += chr((ord(char) + shiftNumber - 65) % 26 + 65)
        else:
            ans += chr((ord(char)+ shiftNumber - 97) % 26 + 97)
    return ans
inputText = "Hello Everyone"
shiftNumber = 1
print("Plain Text  is: " + inputText)
print("Shift Number is: " + shiftNumber)
print("Encrytption is: " +  cipherAlg(inputText, shiftNumber))