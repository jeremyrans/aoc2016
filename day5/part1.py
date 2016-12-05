from hashlib import md5

input = 'ojvtpuvg'

i = 0

answer = []

while True:
    to_hash = "{}{}".format(input, str(i))
    hash = md5(to_hash).hexdigest()
    if hash.startswith("00000"):
        answer.append(hash[5])
        print hash[5]
        if len(answer) == 8:
            break
    i += 1

print "".join(answer)

