file_contents = open('input.txt').readline().strip()

decompressed = ''

i = 0
while i < len(file_contents):
    if file_contents[i] == '(':
        marker_end = file_contents[i:].find(')')
        marker = file_contents[i+1:i+marker_end]
        i += marker_end + 1
        count, _, repeat = marker.partition('x')
        to_repeat = file_contents[i:i+int(count)]
        for _ in xrange(int(repeat)):
            decompressed += to_repeat
        i += int(count)

    else:
        decompressed += file_contents[i]
        i += 1

print len(decompressed)
