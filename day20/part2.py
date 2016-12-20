lines = [l.strip() for l in open('input.txt').readlines()]

max_ip = 4294967295

blocks = []
allowed = 0

for line in lines:
    blocks.append(tuple([int(x) for x in line.split('-')]))
blocks.sort()

to_check = 0
while True:
    if to_check > max_ip:
        break

    blocked = False
    for b in blocks:
        if b[0] <= to_check <= b[1]:
            to_check = b[1] + 1
            blocked = True
            break
    if not blocked:
        skip_to = next(b for b in blocks if b[0] > to_check)
        allowed += skip_to[0] - to_check
        to_check = skip_to[1]

print allowed
