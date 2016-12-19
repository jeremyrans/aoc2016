import collections

num_elves = 3017957
elves1 = collections.deque([i for i in xrange(1, num_elves / 2 + 1)])
elves2 = collections.deque([i for i in xrange(num_elves / 2 + 1, num_elves + 1)])


while True:
    if len(elves1) + len(elves2) == 1:
        print elves1, elves2
        exit()
    elves2.popleft()
    elves2.append(elves1.popleft())
    if len(elves2) - len(elves1) > 1:
        elves1.append(elves2.popleft())
