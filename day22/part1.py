lines = [l.strip() for l in open('input.txt').readlines()]

nodes = [
    [{} for _ in xrange(38)]
    for _ in xrange(26)
]

for line in lines:
    parts = line.split()
    coords = parts[0].split('-')
    x = int(coords[1][1:])
    y = int(coords[2][1:])
    nodes[y][x] = {
        'x': x,
        'y': y,
        'size': int(parts[1][:-1]),
        'used': int(parts[2][:-1]),
        'avail': int(parts[3][:-1])
    }


def count_viable_nodes(node):
    viable_count = 0
    for row in nodes:
        for col in row:
            if node['x'] == col['x'] and node['y'] == col['y']:
                continue
            if node['used'] == 0:
                continue
            if node['used'] <= col['avail']:
                viable_count += 1

    return viable_count

viable = 0
for row in nodes:
    for col in row:
        viable += count_viable_nodes(col)

print viable
