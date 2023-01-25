import random
import sys
import string

scores = {}
dictionary = []
tiles = []

try:
    with open("tiles.txt") as f:
        for line in f.readlines():
            tiles.append(line.strip())
except FileNotFoundError:
    print("The tiles cannot be found.")
except:
    print(f"Error processing the tiles...")

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


def bestWord(myTiles, given, dictionary):
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
        if given.upper() in word:
            print("You got the highest score!")


def gameStart():
    print("Generating Random Tiles...")
    tiles_picked = []
    for i in range(7):
        tile_random_pick = random.choice(tiles)
        tiles_picked.append(tile_random_pick)
    print("Tiles: " + " ".join(tiles_picked))
    score_print = []
    for x in tiles_picked:
        score_print.append(str(getLetterScore(x)))
    print("Scores: " + " ".join(score_print))
    word = input("Enter your word: ")
    while onlyEnglishLetters(word) == False or word.upper() not in dictionary or canBeMade(word, tiles_picked) == False:
        if word == "&&&":
            print("Thanks for using this application, better luck next time!!!")
            raise SystemExit(0)
        else:
            if onlyEnglishLetters(word) == False:
                print("Only use English letters...")
            if word.upper() not in dictionary:
                print("Word not in dictionary")
            if canBeMade(word, tiles_picked) == False:
                print("Word cannot be made from tiles.")
            word = input("Enter your word: ")
    else:
        if isValid(word, tiles_picked, dictionary):
            print("You got it right, this is a valid word.")
            print(f"Score of this word is: {getWordScore(word)}")
        else:
            print(f"This is wrong, Score of this word is: 0")
    choice = input("Do you want to see the highest scoring words? (Yes/No): ")
    choice = choice.lower()
    valid_choices = ["yes", "no"]
    while choice not in valid_choices:
        print("Please enter a valid input....")
        choice = input(
            "Do you want to see the highest scoring words? (Yes/No): ")
    if choice == valid_choices[0]:
        bestWord(tiles_picked, word, dictionary)
    elif choice == valid_choices[0]:
        pass


def gameLoop():
    gameStart()
    choice = input("Do you want to play again? (Yes/No): ")
    valid_choices = ["yes", "no"]
    while choice not in valid_choices:
        print("Please enter a valid input....")
        choice = input("Do you want to play again? (Yes/No): ")
    if choice == valid_choices[0]:
        print("\n")
        gameStart()
    elif choice == valid_choices[0]:
        print("Goodbye!")
        raise SystemExit(0)


print("Hello welcome to our Scrabble Game.")
print("\n")
gameLoop()
