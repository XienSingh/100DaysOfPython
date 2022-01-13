import Art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(Art.logo)


def caesar(text,shift,direction):
    encoded = []
    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            indexOfLetter = alphabet.index(char)
            if (indexOfLetter + shift) > 25:
                encoded.append(alphabet[shift - 1])
            else:
                encoded.append(alphabet[indexOfLetter + shift])
        else:
            encoded.append(char)
    print("".join(encoded))


runApp = True
while runApp:
    directionToGo = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'end' to exit:\n")
    if directionToGo == "end":
        runApp = False
        break
    textToProcess = input("Type your message:\n").lower()
    shiftToAdd = int(input("Type the shift number:\n"))
    if shiftToAdd > 26:
        shiftToAdd = shiftToAdd % 26
    caesar(textToProcess, shiftToAdd, directionToGo)
