import string

def char_index(char):
    return string.ascii_lowercase.index(char)


def char_from_index(index):
    if index >= 26:
        index = index % 26
    results = string.ascii_lowercase[index]

    return results


def char_from_index_substitution(index):
    if index >= 26:
        index = index % 26
    results = list('zyxwvutsrqponmlkjihgfedcba')[index]

    return results


def ceasar_cipher(string, key):
    cipher_text = []

    for word in string.split():
        plain_text_positions = [char_index(char) for char in word.lower()]
        ciphered = [i + key for i in plain_text_positions]

        cipher_text.append(''.join([char_from_index(index) for index in ciphered]))

    return ' '.join(cipher_text)


def modified_ceasar_cipher(string, key):
    cipher_text = []

    for word in string.split():
        plain_text_positions = [char_index(char) for char in word.lower()]
        cipher_positions = list(range(3, len(string)*3+1))[::3] # create keys

        # check for encryp/decrypt
        if key > 0:
            ciphered = [sum(i) for i in zip(plain_text_positions, cipher_positions)]
        else:
            ciphered = [sum(i) for i in zip(plain_text_positions, [-i for i in cipher_positions])]

        cipher_text.append(''.join([char_from_index(index) for index in ciphered]))

    return ' '.join(cipher_text)


def ceasar_cipher_substitution(string):
    cipher_text = []

    for word in string.split():
        plain_text_positions = [char_index(char) for char in word.lower()]
        cipher_text.append(''.join([char_from_index_substitution(index) for index in plain_text_positions]))

    return ' '.join(cipher_text)

print('Simple Alrogithm:')
print(ceasar_cipher('comehere', 8)) # plain text
print(ceasar_cipher('kwumpmzm', -8)) # cipher text
print('\n')
print('Modified Algorithm:')
print(modified_ceasar_cipher("text hello", 3)) # plain text
print(modified_ceasar_cipher("wkgf kkuxd", -3)) # cipher text
print('\n')
print('Substitution:')
print(ceasar_cipher_substitution('todsanai chum')) # plain text
print(ceasar_cipher_substitution('glwhzmzr')) # cipher text
