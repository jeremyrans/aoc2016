lines = [l.strip() for l in open('input.txt').readlines()]
total = 0

for line in lines:
    in_brackets = False

    aba = []
    bab = []
    for i in xrange(len(line) - 1):
        piece = line[i:i + 3]
        if '[' in piece:
            in_brackets = True
        if ']' in piece:
            in_brackets = False
        if piece == piece[::-1] and piece[0] != piece[1]:
            if in_brackets:
                bab.append('{}{}{}'.format(piece[1], piece[0], piece[1]))
            else:
                aba.append(piece)
    if any(x in aba for x in bab):
        total += 1

print total

