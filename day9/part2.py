file_contents = open('input.txt').readline().strip()

def decompress(contents):
    length = 0
    if '(' not in contents:
        return len(contents)

    while len(contents) > 0:
        if contents[0] == '(':
            marker_end = contents.find(')')
            marker = contents[1:marker_end]
            count, _, repeat = marker.partition('x')
            to_repeat = contents[marker_end + 1:marker_end + 1 + int(count)]
            length += decompress(to_repeat) * int(repeat)
            contents = contents[int(count) + marker_end + 1:]
        else:
            length += 1
            contents = contents[1:]

    return length

print decompress(file_contents)
