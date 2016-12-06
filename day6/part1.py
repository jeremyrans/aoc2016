from collections import Counter

lines = [l.strip() for l in open('input.txt').readlines()]

positions = {}
for i in xrange(len(lines[0])):
    positions[i] = []

for line in lines:
    for i, c in enumerate(line):
        positions[i].append(c)

for position, items in positions.iteritems():
    data = Counter(items)
    print position, data.most_common(1)[0][0]
