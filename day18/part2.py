input = ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"
row_count = 400000
rows = [input]


def get_tile(l, c, r):
    if l == '^' and c == '^' and r == '.':
        return '^'
    if l == '.' and c == '^' and r == '^':
        return '^'
    if l == '^' and c == '.' and r == '.':
        return '^'
    if l == '.' and c == '.' and r == '^':
        return '^'
    return '.'


for i in xrange(row_count-1):
    new_row = "".join([
        get_tile(rows[i][j-1] if j-1 >= 0 else '.', rows[i][j], rows[i][j+1] if j+1 < len(input) else '.')
        for j in xrange(len(input))
    ])
    rows.append(new_row)

print sum(r.count('.') for r in rows)
