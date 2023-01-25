import string

scores = {}
dictionary = []

try:
    with open("scores.txt") as f:
        for line in f.readlines():
            line = line.strip().replace(" ", "")
            scores[line[0]] = int(line[1:])
except FileNotFoundError:
    print("The scores file cannot be found.")
except:
    print(f"Error processing scores file...")

try:
    with open("dictionary.txt") as f:
        for line in f.readlines():
            dictionary.append(line.strip())
except FileNotFoundError:
    print("The dictionary cannot be found.")
    raise SystemExit(0)
except:
    print(f"Error processing dictionary...")
    raise SystemExit(0)


def onlyEnglishLetters(word):
    alpha = string.ascii_uppercase
    for char in (word.upper()):
        if char not in alpha:
            return False
    else:
        return True


def getLetterScore(letter):
    if onlyEnglishLetters(letter):
        score = scores[letter.upper()]
        return score
    else:
        return 0


def getWordScore(word):
    total_score = 0
    if word.upper() in dictionary:
        for char in word:
            score = getLetterScore(char)
            total_score += score
        return total_score
    else:
        return 0


print(getWordScore("hammer"))
print(getWordScore("hamm er"))
print(getWordScore("Milk"))
print(getWordScore("M1^K"))
print(getWordScore("Milk   "))
