#zadanie 4.2

word = input('Enter a word:')

def polindrom(word):
    if word == word[::-1]:
        return True
    else:
        return False

result = polindrom(word)
print(result)