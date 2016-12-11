from Queue import Queue
import itertools
from copy import deepcopy

input = [
    ['TH-G', 'TH-M', 'PL-G', 'ST-G'],
    ['PL-M', 'ST-M'],
    ['PR-G', 'PR-M', 'RU-G', 'RU-M'],
    []
]
seen_states = set()
q = Queue()


def is_win(floors):
    for i in xrange(3):
        if len(floors[i]) > 0:
            return False
    return True


def is_valid(floors):
    for f in xrange(3):
        microchips = [item[:2] for item in floors[f] if item[-1] == 'M']
        generators = [item[:2] for item in floors[f] if item[-1] == 'G']
        for m in microchips:
            if len(generators) > 0 and m not in generators:
                return False
    return True


def already_seen(floors, elevator):
    normalized_floors = [
        [], [], [], []
    ]

    # normalize state to P (pair), M (microchip), G (generator)
    # we don't really care which one it is
    for i in xrange(4):
        microchips = [item[:2] for item in floors[i] if item[-1] == 'M']
        generators = [item[:2] for item in floors[i] if item[-1] == 'G']
        for m in microchips:
            if m in generators:
                normalized_floors[i].append('P')
            else:
                normalized_floors[i].append('M')
        for g in generators:
            if g not in microchips:
                normalized_floors[i].append('G')

    normalized_state = tuple([tuple(sorted(f)) for f in normalized_floors] + ['E' + str(elevator)])
    if normalized_state in seen_states:
        return True
    seen_states.add(normalized_state)
    return False


def find_shortest_path():
    last_steps = 0

    while not q.empty():
        floors, elevator, steps = q.get()

        if not is_valid(floors):
            continue

        if already_seen(floors, elevator):
            continue

        if is_win(floors):
            print steps
            return

        steps += 1
        if steps > last_steps:
            print steps
            last_steps = steps

        #up
        if elevator < 3:
            skip_ones = False
            for c in list(itertools.combinations(floors[elevator], 2)) + list(itertools.combinations(floors[elevator], 1)):
                if skip_ones and len(c) == 1:
                    break
                f_copy = deepcopy(floors)
                _ = [f_copy[elevator].remove(i) for i in iter(c)]
                f_copy[elevator+1].extend(list(c))
                if is_valid(f_copy):
                    if len(c) == 2:
                        skip_ones = True
                    q.put((f_copy, elevator+1, steps))

        #down
        if elevator > 0:
            skip_twos = False
            for c in list(itertools.combinations(floors[elevator], 1)) + list(itertools.combinations(floors[elevator], 2)):
                if skip_twos and len(c) == 2:
                    break
                f_copy = deepcopy(floors)
                _ = [f_copy[elevator].remove(i) for i in iter(c)]
                f_copy[elevator-1].extend(list(c))
                if is_valid(f_copy):
                    if len(c) == 1:
                        skip_twos = True
                    q.put((f_copy, elevator-1, steps))

q.put((deepcopy(input), 0, 0))

find_shortest_path()
