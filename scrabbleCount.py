count = { 'a': 9, 'b': 2, 'c': 2, 'd': 4, 'e': 12, 'f': 2, 'g': 3, 'h': 2, 'i': 9, 'j': 1, 'k': 1, 'l': 4, 'm': 2, 'n': 6, 'o': 8, 'p': 2, 'q': 1, 'r': 6, 's': 4, 't': 6, 'u': 4, 'v': 2, 'w': 2, 'x': 1, 'y': 2, 'z': 1, '_':2 }

currentCount = dict(count)

board = input()

for character in board:
    characterCount = currentCount[character.lower()] - 1
    if characterCount < 0:
        print('Invalid input. More ' + character.upper() + '\'s have been taken from the bag than possible.')
        exit()
    currentCount[character.lower()] = currentCount[character.lower()] - 1

def generateCount():
    for i in range(12, -1, -1):
        ithCount = []
        for key, value in currentCount.items():
            if value is i:
                ithCount.append(key)
        if len(ithCount) != 0:
            print(str(i) + ': ' + '{}'.format(', '.join(sorted(ithCount))))

generateCount()
