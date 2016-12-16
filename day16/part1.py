input = "01110110101001000"
disk_size = 272


def apply_step(a):
    b = ""
    for c in a[::-1]:
        if c == "1":
            b += "0"
        else:
            b += "1"
    return a + "0" + b


disk = input
while len(disk) < disk_size:
    disk = apply_step(disk)
disk = disk[:disk_size]


def get_checksum(x):
    result = ""
    for i in xrange(0, len(x)-1, 2):
        if x[i:i+2] == "00" or x[i:i+2] == "11":
            result += "1"
        else:
            result += "0"
    if len(result) % 2 == 0:
        return get_checksum(result)
    else:
        return result


checksum = get_checksum(disk)

print checksum
