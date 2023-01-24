import random

scores = {}
dictionary = []
tiles = []

#task1
with open("scores.txt") as f:
    for line in f.readlines():
        scores[line[0]] = int(line[2])

with open("tiles.txt") as f:
    for line in f.readlines():
        tiles.append(line.strip())

with open("dictionary.txt") as f:
    for line in f.readlines():
        dictionary.append(line.strip())

#task2
def onlyEnglishLetters(word):
    english_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    english_check = False
    for char in word:
        if char.lower() in english_alphabet:
            english_check = True
        elif char.lower() not in english_alphabet:
            english_check = False
            break
    return english_check

#task3
def getLetterScore(letter):
    if onlyEnglishLetters(letter):
        score = scores[letter.upper()]
        return score
    else:
        return 0

#task4
def getWordScore(word):
    total_score = 0
    if word.upper().strip() in dictionary:
        for char in word:
            score = getLetterScore(char)
            total_score += score
        return total_score
    else:
        return 0

#task5
def canBeMade(word, myTiles):
    tile_bank = {}
    word_bank = {}
    bemade_check = False
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
                    bemade_check = True
                else:
                    bemade_check = False
                    break
            else:
                bemade_check = False
                break
        return bemade_check
    else:
        return False

#task6
def isValid(word_checked, myTiles):
    if onlyEnglishLetters(word_checked):
        if getWordScore(word_checked) > 0:
            return canBeMade(word_checked, myTiles)
        else:
            print("Word not in dictionary.")
            return False
    else:
        return False

#task7
def bestWord(myTiles,given):
    choice = input(
        "Would you like to see the best word and score for these tiles? (yes/no): ")
    if choice.lower().strip() == "yes":
        print("loading...")
        topscore = 0
        word = []
        for words in dictionary:
            if isValid(words, myTiles):
                currentscore = getWordScore(words)
                if currentscore > topscore:
                    topscore = currentscore
        if topscore == 0:
            print("Wow. There is no word.... MY BAD!")
        else:
            for words in dictionary:
                if isValid(words, myTiles):
                    currentscore = getWordScore(words)
                    if currentscore == topscore:
                        word.append(words)
            print(f"The best score is {topscore} from the words {word}")
            if given.upper() in word:
                print("You got the highest score!")
    else:
        pass


#part2
def gameStart():
    print("Generating Random Tiles...")
    tilespicked = []
    for i in range(7):
        tilerando = random.choice(tiles)
        tilespicked.append(tilerando)
    print("Tiles: " + " ".join(tilespicked))
    scoreprint = []
    for x in tilespicked:
        scoreprint.append(str(getLetterScore(x)))
    print("Scores: " + " ".join(scoreprint))
    wordx = input("Enter your word: ")
    while onlyEnglishLetters(wordx) == False:
        if wordx == "&&&":
            print("Thanks for using this application, better luck next time!!!")
            break
        else:
            print("Only use English letters...")
            wordx = input("Enter your word: ")
    else:
        if isValid(wordx, tilespicked):
            print("You got it right, this is a valid word.")
            print(f"Score of this word is: {getWordScore(wordx)}")
            bestWord(tilespicked,wordx)
        else:
            print(f"This is wrong, Score of this word is: 0")
            bestWord(tilespicked,wordx)

gameStart()
