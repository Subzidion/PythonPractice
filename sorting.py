def bubbleSort(swapList):
    while True:
        swapMade = False
        for i in range(1,len(swapList)):
            if swapList[i - 1] > swapList[i]: 
                swapList[i - 1], swapList[i] = swapList[i], swapList[i - 1]
                swapMade = True
        if not swapMade:
            return swapList

swapList = [6, 4, 1, 7, 3, 9, 31, 2]
print(swapList)
print(bubbleSort(swapList) + '\n')
