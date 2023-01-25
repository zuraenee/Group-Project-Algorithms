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


def canBeMade(word, myTiles):
    tile_bank = {}
    word_bank = {}
    be_made_check = False
    if onlyEnglishLetters(word):
        for each in myTiles:
            if each in tile_bank:
                tile_bank[each] += 1
            else:
                tile_bank[each] = 1
        for char in word:
            if char in word_bank:
                word_bank[char.upper()] += 1
            else:
                word_bank[char.upper()] = 1
        for i in word_bank.keys():
            if i in tile_bank:
                if word_bank[i] == tile_bank[i] or word_bank[i] < tile_bank[i]:
                    be_made_check = True
                else:
                    be_made_check = False
                    break
            else:
                be_made_check = False
                break
        return be_made_check
    else:
        return False


def isValid(word, myTiles, dictionary):
    if onlyEnglishLetters(word):
        if word.upper() in dictionary:
            return canBeMade(word, myTiles)
        else:
            return False
    else:
        return False


print(isValid("hammer", ['T', 'A', 'H', 'E', 'M', 'M', 'R'], dictionary))
print(isValid("hammeer", ['E', 'A', 'H', 'E', 'M', 'M', 'R'], dictionary))
print(isValid("ha5mer", ['T', 'A', 'H', 'E', 'M', 'M', 'R'], dictionary))
print(isValid("", ['T', 'A', 'H', 'E', 'M', 'M', 'R'], dictionary))
print(isValid("hammer   ", ['T', 'A', 'H', 'E', 'M', 'M', 'R'], dictionary))
