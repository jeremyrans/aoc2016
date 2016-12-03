lines = [l.strip() for l in open('input.txt').readlines()]


possible = 0

for triangle in lines:
    sides = [int(t.strip()) for t in triangle.split()]
    if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
        possible += 1

print possible
