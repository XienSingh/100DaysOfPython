alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    encoded = []
    for char in text:
        if char != " ":
            indexOfLetter = alphabet.index(char)
            if (indexOfLetter + shift) > 25:
                encoded.append(alphabet[shift - 1])
            else:
                encoded.append(alphabet[indexOfLetter + shift])
        else:
            encoded.append(" ")
    print("".join(encoded))


def decode(text, shift):
    decoded = []
    for char in text:
        if char != " ":
            indexOfLetter = alphabet.index(char)
            if (indexOfLetter - shift) > 25:
                decoded.append(alphabet[shift + 1])
            else:
                decoded.append(alphabet[indexOfLetter - shift])
        else:
            decoded.append(" ")
    print("".join(decoded))


runApp = True
while runApp:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'end' to exit:\n")
    if direction.lower() == "end":
        runApp = False
        break
    textToProcess = input("Type your message:\n").lower()
    shiftToAdd = int(input("Type the shift number:\n"))
    if direction.lower() == "encode":
        encrypt(textToProcess, shiftToAdd)
    elif direction.lower() == "decode":
        decode(textToProcess, shiftToAdd)

