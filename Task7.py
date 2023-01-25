import sys
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


def bestWord(myTiles, dictionary):
    choice = input(
        "Would you like to see the best word and score for these tiles? (yes/no): ")
    if choice.lower().strip() == "yes":
        print("loading...")
        sys.stdout.write("\033[F")
        top_score = 0
        word = {}
        keys = []
        for words in dictionary:
            if isValid(words, myTiles, dictionary):
                current_score = getWordScore(words)
                if current_score >= top_score:
                    top_score = current_score
                    word[words] = current_score
        for each in word.keys():
            if word[each] == top_score:
                keys.append(each)
        if top_score == 0:
            print("Wow. There is no word.... MY BAD!")
        else:
            print(f"The best score is {top_score} from the word/words {keys}")
    else:
        pass


bestWord(["T", "O", "I", "N", "L", "M", "L"], dictionary)
bestWord(["H", "P", "D", "X", "Z", "O", "O"], dictionary)
bestWord(["H", "C", "I", "N", "L", "A", "L"], dictionary)
bestWord(["T", 0, "T", "P", 7, 0, 0], dictionary)
bestWord(["S", "O", "I", "F", "G", "Y", "G"], dictionary)
