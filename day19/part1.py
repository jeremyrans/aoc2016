import itertools

num_elves = 3017957
presents = [1 for _ in xrange(num_elves)]

for i in itertools.cycle(xrange(len(presents))):
    if presents[i] == 0:
        continue

    for j in xrange(1, len(presents)):
        to_check = (j + i) % (len(presents))
        if presents[to_check] > 0:
            presents[i] += presents[to_check]
            presents[to_check] = 0
            break

    if presents[i] == num_elves:
        print i+1
        exit()
