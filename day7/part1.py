lines = [l.strip() for l in open('input.txt').readlines()]
total = 0

for line in lines:
    possible = False
    in_brackets = False
    impossible = False
    for i in xrange(len(line)):
        piece = line[i:i + 4]
        if '[' in piece:
            in_brackets = True
        if ']' in piece:
            in_brackets = False
        if piece[:2] == piece[2:][::-1] and piece[0] != piece[1]:
            if in_brackets:
                impossible = True
                break
            else:
                possible = True
    if possible and not impossible:
        total += 1

print total

