import string


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


print(canBeMade("SWET", ['T', 'Y', 'S', 'E', 'U', 'W', 'I']))

print(canBeMade("SWEET", ['T', 'Y', 'S', 'E', 'U', 'W', 'I']))

print(canBeMade("SWE ET", ['T', 'Y', 'S', 'E', 'U', 'W', 'I']))

print(canBeMade("SWEETU", ['T', 'Y', 'S', 'E', 'U', 'W', 'I']))

print(canBeMade("", ['T', 'Y', 'S', 'E', 'U', 'W', 'I']))
