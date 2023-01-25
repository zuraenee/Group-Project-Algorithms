import string

def onlyEnglishLetters(word):
    alpha = string.ascii_uppercase
    for char in (word.upper()):
        if char not in alpha:
            return False
    else:
        return True



print(onlyEnglishLetters("HELLO"))
print(onlyEnglishLetters("HE LLO"))
print(onlyEnglishLetters("HE3LLO"))

word = str(input('Enter a word: '))
print(onlyEnglishLetters(word))
