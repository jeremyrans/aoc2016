from Queue import Queue
from hashlib import md5

open = ['b', 'c', 'd', 'e', 'f']
input = "mmsxrhfx"
q = Queue()
best = 0

q.put((0, 0, []))

while not q.empty():
    cur_x, cur_y, path = q.get()
    if cur_x == 3 and cur_y == 3:
        best = len(path)
        continue
    to_hash = input + "".join(path)
    hashed = md5(to_hash).hexdigest().lower()
    up = hashed[0] in open and cur_y > 0
    down = hashed[1] in open and cur_y < 3
    left = hashed[2] in open and cur_x > 0
    right = hashed[3] in open and cur_x < 3

    if up:
        new_path = list(path) + ['U']
        q.put((cur_x, cur_y - 1, new_path))
    if down:
        new_path = list(path) + ['D']
        q.put((cur_x, cur_y + 1, new_path))
    if left:
        new_path = list(path) + ['L']
        q.put((cur_x - 1, cur_y, new_path))
    if right:
        new_path = list(path) + ['R']
        q.put((cur_x + 1, cur_y, new_path))


print best
