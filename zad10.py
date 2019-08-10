
def anagram(first_word, second_word):


    first_word_sorted = (''.join(sorted(first_word))).lower()
    second_word_sorted = (''.join(sorted(second_word))).lower()

    return first_word_sorted == second_word_sorted


print(anagram("finder", "friend"))
