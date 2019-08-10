
def is_palindrom(word):
    word_reverse = word[::-1]

    if word == word_reverse:
        return True
    else:
        return False


is_palindrom("kajak")
