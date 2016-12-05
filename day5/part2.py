from hashlib import md5

input = 'ojvtpuvg'

i = 0

answer = [None] * 8

while True:
    to_hash = "{}{}".format(input, str(i))
    hash = md5(to_hash).hexdigest()
    if hash.startswith("00000"):
        if hash[5].isdigit() and 0 <= int(hash[5]) <= 7 and answer[int(hash[5])] is None:
            answer[int(hash[5])] = hash[6]
            print hash[5], hash[6]
            if answer.count(None) == 0:
                break
    i += 1

print "".join(answer)

