lines = [l.strip() for l in open('input.txt').readlines()]

registers = {
    'a': 12,
    'b': 0,
    'c': 0,
    'd': 0
}

index = 0
toggles = []


def _get_value(x):
    try:
        x = int(x)
    except:
        x = registers[x]
    return x


def mul(x, y):
    registers[x] *= _get_value(y)


def cpy(x, y, toggle=False):
    if toggle:
        return jnz(x, y)
    else:
        x = _get_value(x)
        if y == _get_value(y):
            return
        registers[y] = x


def inc(x, toggle=False):
    if toggle:
        dec(x)
    else:
        if x == _get_value(x):
            return
        registers[x] += 1


def dec(x, toggle=False):
    if toggle:
        inc(x)
    else:
        if x == _get_value(x):
            return
        registers[x] -= 1


def jnz(x, y, toggle=False):
    if toggle:
        cpy(x, y)
    else:
        x = _get_value(x)
        y = _get_value(y)

        if x != 0:
            return int(y)
        else:
            return 1


def tgl(x, toggle=False):
    if toggle:
        inc(x)
    else:
        x = _get_value(x)
        toggles.append(index+x)


while index < len(lines):
    parts = lines[index].split()
    toggle = index in toggles

    if parts[0] == 'cpy':
        to_jump = cpy(*parts[1:], toggle=toggle)
        if to_jump:
            index += to_jump
            continue

    elif parts[0] == 'inc':
        inc(*parts[1:], toggle=toggle)

    elif parts[0] == 'dec':
        dec(*parts[1:], toggle=toggle)

    elif parts[0] == 'jnz':
        to_jump = jnz(*parts[1:], toggle=toggle)
        if to_jump:
            index += to_jump
            continue

    elif parts[0] == 'tgl':
        tgl(*parts[1:], toggle=toggle)

    elif parts[0] == 'mul':
        mul(*parts[1:])

    index += 1


print registers['a']
