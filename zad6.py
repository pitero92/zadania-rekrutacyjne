
def charfinding(char, word):
    num = 0
    for i in word:
        if i == char:
            num += 1
    print num

charfinding("h", "hello")
