from hashlib import md5
import itertools

import re

salt = "ngcjuoqr"
triplets_re = re.compile(r'(([a-zA-Z0-9])\2\2)')
key_count = 0
index_hashes = {}
hash_hashes = {}


def get_triplets(hash):
    return [i[1] for i in triplets_re.findall(hash)]


def has_5x_repeating(hash, char):
    return (char * 5) in hash


def hash_lots(to_hash, i):
    result = md5('{}{}'.format(to_hash, i)).hexdigest()
    for _ in xrange(2016):
        prev = result
        result = hash_hashes[result] if result in hash_hashes else md5(prev).hexdigest()
        hash_hashes[prev] = result
    return result


for i in itertools.count():
    index_hashes[i] = index_hashes[i] if i in index_hashes else hash_lots(salt, i)
    triplets = get_triplets(index_hashes[i])
    if triplets:
        for j in xrange(i+1, i+1001):
            index_hashes[j] = index_hashes[j] if j in index_hashes else hash_lots(salt, j)
            if has_5x_repeating(index_hashes[j], triplets[0]):
                key_count += 1
                if key_count == 64:
                    print i
                    exit()
                break
