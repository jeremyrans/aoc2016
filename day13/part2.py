from Queue import Queue

puzzle_input = 1362
start = (1, 1)

visited = set()
q = Queue()


def is_wall(x, y):
    if x < 0 or y < 0:
        return True
    result = (x * x + 3 * x + 2 * x * y + y + y * y) + puzzle_input
    binary_rep = "{0:b}".format(result)
    return binary_rep.count('1') % 2 == 1


def find_destination():
    while not q.empty():
        location, steps = q.get()

        if steps > 50:
            print len(visited)
            exit()

        if location in visited:
            continue
        else:
            visited.add(location)

        steps += 1

        if not is_wall(location[0]+1, location[1]):
            q.put(((location[0]+1, location[1]), steps))
        if not is_wall(location[0]-1, location[1]):
            q.put(((location[0]-1, location[1]), steps))
        if not is_wall(location[0], location[1]+1):
            q.put(((location[0], location[1]+1), steps))
        if not is_wall(location[0], location[1]-1):
            q.put(((location[0], location[1]-1), steps))


q.put(((1, 1), 0))
find_destination()


