import string

def char_index(char):
    return string.ascii_lowercase.index(char)


def char_from_index(index):
    if index >= 26:
        index = index % 26
    results = string.ascii_lowercase[index]

    return results


def encrypt(char1, char2):
    return char_from_index((char_index(char1)) + char_index(char2))


def decrypt(char1, char2):
    return char_from_index((char_index(char1)) - char_index(char2))


def polyalphabetic_vigenere(plaintextCiphertext, keyword, option):

    zipped = zip(plaintextCiphertext, keyword)

    if option == 'encrypt':
        return ''.join([(encrypt(z[0], z[1])) for z in zipped])
    if option == 'decrypt':
        return ''.join([(decrypt(z[0], z[1])) for z in zipped])



print(polyalphabetic_vigenere('crypt', 'bosto', 'encrypt'))
print(polyalphabetic_vigenere('dfqih', 'bosto', 'decrypt'))
