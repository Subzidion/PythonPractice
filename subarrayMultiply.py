combos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

def  count(numbers, k):
    total = 0
    for split_size in xrange(1, (len(numbers) + 1)):
        happened = False
        for i in xrange(0, (len(numbers) - split_size) + 1):
            combo = numbers[i:i + split_size]
            prod = 1
            for num in numbers[i:i + split_size]:
                prod = prod * num
            if prod < k:
                total += 1
                happened = True
        if not happened:
            return total
    return total

print count(combos, 300)
