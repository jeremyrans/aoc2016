from copy import deepcopy

lines = [l.strip() for l in open('input.txt').readlines()]

screen = [
    ['.' for _ in xrange(50)]
    for _ in xrange(6)
]

for line in lines:
    old_screen = deepcopy(screen)
    command, _, rest = line.partition(' ')
    if command == 'rect':
        x, _, y = rest.partition('x')
        x = int(x)
        y = int(y)
        for i in xrange(y):
            for j in xrange(x):
                screen[i][j] = 'x'

    if command == 'rotate':
        row_or_column, _, rest = rest.partition(' ')
        if row_or_column == 'row':
            row, _, shift = rest.partition(' by ')
            _, _, row = row.partition('=')
            row = int(row)
            shift = int(shift)
            for i in xrange(0, 50):
                screen[row][i] = old_screen[row][i-shift]

        else:
            col, _, shift = rest.partition(' by ')
            _, _, col = col.partition('=')
            col = int(col)
            shift = int(shift)
            for i in xrange(0, 6):
                screen[i][col] = old_screen[i-shift][col]

print '\n'.join(''.join(s) for s in screen)
