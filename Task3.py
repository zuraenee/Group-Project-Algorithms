import string

scores = {}

try:
    with open("scores.txt") as f:
        for line in f.readlines():
            line = line.strip().replace(" ", "")
            scores[line[0]] = int(line[1:])
except FileNotFoundError:
    print("The scores file cannot be found.")
    raise SystemExit(0)
except:
    print(f"Error processing scores file...")
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


print(getLetterScore("Z"))
print(getLetterScore("55"))
print(getLetterScore("P"))
print(getLetterScore("PT"))
print(getLetterScore("3"))