lengths_input = raw_input()
lengths = lengths_input.split(' ')
n = int(lengths[0])
m = int(lengths[1])

s = raw_input()
p = raw_input()

combos = [p]

for count in xrange(p.count('*')):
    new_combos = []
    for combo in combos:
        new_combos.append(combo.replace('*', 'A', 1))
        new_combos.append(combo.replace('*', 'B', 1))
        new_combos.append(combo.replace('*', 'C', 1))
        new_combos.append(combo.replace('*', 'D', 1))
    combos = new_combos

occurrences = 0
for pattern in combos:
    occurrences += s.count(pattern)

print occurrences
