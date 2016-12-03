lines = [[int(i) for i in l.strip().split()] for l in open('input.txt').readlines()]

possible = 0

for i in xrange(0, len(lines), 3):
    for j in xrange(3):
        sides = [lines[i][j], lines[i+1][j], lines[i+2][j]]
        if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
            possible += 1

print possible
