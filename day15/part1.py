import itertools


def rotate_discs(x):
    for disc in discs:
        disc[1] += x
        disc[1] %= disc[0]


for i in itertools.count():
    discs = [
        [17, 1],
        [7, 0],
        [19, 2],
        [5, 0],
        [3, 0],
        [13, 5],
    ]
    rotate_discs(i)
    success = True
    for j in xrange(len(discs)):
        rotate_discs(1)
        if discs[j][1] != 0:
            success = False
            break

    if success:
        print i
        exit()
