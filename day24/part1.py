from collections import deque
from itertools import permutations

floor_map = [l.strip() for l in open('input.txt').readlines()]

start = (0, 0)
targets = []

for y, row in enumerate(floor_map):
    for x, col in enumerate(row):
        if col == '0':
            start = (y, x)
            targets.append(start)
        elif col.isdigit():
            targets.append((y, x))


def distance_from_to(start, end):
    q = deque([(0, start)])
    seen = {start}
    while q:
        distance, location = q.pop()
        if location == end:
            return distance

        y, x = location
        if (y,x-1) not in seen and floor_map[y][x-1] != '#':  # up
            seen.add((y, x-1))
            q.appendleft((distance + 1, (y, x-1)))

        if (y,x+1) not in seen and floor_map[y][x+1] != '#':  # down
            seen.add((y, x+1))
            q.appendleft((distance + 1, (y, x+1)))

        if (y-1,x) not in seen and floor_map[y-1][x] != '#':  # left
            seen.add((y-1, x))
            q.appendleft((distance + 1, (y-1, x)))

        if (y+1,x) not in seen and floor_map[y+1][x] != '#':  # right
            seen.add((y+1, x))
            q.appendleft((distance + 1, (y+1, x)))


distances = [
    [-1 for _ in xrange(len(targets))]
    for _ in xrange(len(targets))
]

for i in xrange(len(targets)):
    for j in xrange(len(targets)):
        distance = distance_from_to(targets[i], targets[j])
        distances[i][j] = distance
        distances[j][i] = distance

best = 999
for p in permutations(targets):
    if p[0] != start:
        continue

    distance = 0
    for i in xrange(1, len(p)):
        a, b = targets.index(p[i-1]), targets.index(p[i])
        distance += distances[a][b]

    if distance < best:
        best = distance

print best
