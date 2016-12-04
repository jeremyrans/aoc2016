lines = [l.strip() for l in open('input.txt').readlines()]

total = 0

for line in lines:
    room_id, _, other = line.rpartition('-')
    sector_id, _, rest = other.partition('[')
    checksum = rest[:-1]
    letter_counts = {}
    for l in room_id:
        if l != '-':
            letter_counts[l] = room_id.count(l)

    letter_counts_list = []
    for letter, count in letter_counts.iteritems():
        letter_counts_list.append((letter, count))

    sorted_counts = sorted(letter_counts_list, key=lambda x: (-int(x[1]), x[0]))[:5]

    letters = "".join([s[0] for s in sorted_counts])
    print letters, checksum
    if letters == checksum:
        total += int(sector_id)

print total
