lines = [l.strip() for l in open('input.txt').readlines()]

registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}


def _get_value(x):
    try:
        x = int(x)
    except:
        x = registers[x]
    return x


def cpy(x, y):
    x = _get_value(x)
    registers[y] = x


def inc(x):
    registers[x] += 1


def dec(x):
    registers[x] -= 1


def jnz(x, y):
    x = _get_value(x)
    y = _get_value(y)

    if x != 0:
        return int(y)
    else:
        return 1


index = 0
while index < len(lines):
    parts = lines[index].split()
    if parts[0] == 'cpy':
        cpy(*parts[1:])

    elif parts[0] == 'inc':
        inc(*parts[1:])

    elif parts[0] == 'dec':
        dec(*parts[1:])

    elif parts[0] == 'jnz':
        to_jump = jnz(*parts[1:])
        index += to_jump
        continue

    index += 1


print registers['a']
