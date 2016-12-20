lines = [l.strip() for l in open('input.txt').readlines()]

max_ip = 4294967295

blocks = []

for line in lines:
    blocks.append(tuple([int(x) for x in line.split('-')]))
blocks.sort()

to_check = 0
while True:
    blocked = False
    for b in blocks:
        if b[0] <= to_check <= b[1]:
            to_check = b[1] + 1
            blocked = True
            break
    if not blocked:
        print to_check
        exit()
