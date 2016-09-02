from collections import OrderedDict

n = int(raw_input())


data = OrderedDict()

for _ in xrange(n):
    entry = raw_input()
    name, ssn = entry.split(':')
    try:
        data[ssn].append(name)
    except KeyError:
        data[ssn] = [name]

for person in data:
    aliases = data[person]
    bestName = ''
    status = 0
    for alias in aliases:
        split = alias.split(',')
        if len(split) == 2:
            if ' ' in split[1] and status < 3:
                bestName = split[1] + ' ' + split[0]
                status = 3
            elif status < 2:
                bestName = split[1] + ' ' + split[0]
                status = 2
        elif status == 0:
            bestName = split[0]
            status = 1
    data[person] = bestName

for person in data:
    print data[person]
