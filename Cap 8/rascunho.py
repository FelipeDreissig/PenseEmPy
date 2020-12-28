# rascunho do capítulo 8

"""fruit = 'banana'
index = -len(fruit)
while index < 0:
    letter = fruit[index]
    print(letter)
    index = index + 1

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:  # alterar para O e Q
    if letter == 'O':
        print(letter + 'u' + suffix)
    elif letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)"""


def find(word, letter, start):
    index = 0
    while (index + start) < (len(word) - start):
        if word[index+start] == letter:
            return index
        index += 1
    return -1

def count(letter, word, start):
    start = int(start)
    cnt = 0
    for l in range(0 + start, len(word)-start):
        if word[l + start] == letter:
            cnt += 1
    print(cnt)

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return print(False)
    i = 0
    j = (len(word2)-1)
    while j != (-1):
        print(i, j)
        if word1[i] != word2[j]:
            return print(False)
        i = i+1
        j = j-1
    return print(True)


is_reverse('pots', 'stop')
