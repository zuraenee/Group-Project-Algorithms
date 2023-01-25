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
