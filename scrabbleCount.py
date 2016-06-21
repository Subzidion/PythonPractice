count = { 'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2 }

currentCount = dict(count)

board = input()

for character in board:
    characterCount = currentCount[character.upper()] - 1
    if characterCount < 0:
        print('Invalid input. More ' + character.upper() + '\'s have been taken from the bag than possible.')
        exit()
    currentCount[character.upper()] = currentCount[character.upper()] - 1

def generateCount():
    for i in range(12, -1, -1):
        ithCount = []
        for key, value in currentCount.items():
            if value is i:
                ithCount.append(key)
        if len(ithCount) != 0:
            print(str(i).rjust(2) + ': ' + '{}'.format(', '.join(sorted(ithCount))))

generateCount()
