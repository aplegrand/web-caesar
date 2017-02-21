
def alphabet_position(letter):
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    if letter.isupper():
        return uppers.find(letter)
    elif letter.islower():
        return lowers.find(letter)

def rotate_character(char, rot):
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    if not char.isalpha():
        return char
    elif char.isupper():
        return uppers[(alphabet_position(char)+rot)%26]
    elif char.islower():
        return lowers[(alphabet_position(char)+rot)%26]

def encrypt(text, rot):
    newtext = ""
    for char in text:
        newtext += rotate_character(char, rot)
    return newtext
