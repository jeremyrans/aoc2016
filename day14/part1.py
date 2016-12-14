from hashlib import md5
import itertools

import re

salt = "ngcjuoqr"
triplets_re = re.compile(r'(([a-zA-Z0-9])\2\2)')
key_count = 0
computed_hashes = {}


def get_triplets(hash):
    return [i[1] for i in triplets_re.findall(hash)]


def has_5x_repeating(hash, char):
    return (char * 5) in hash


for i in itertools.count():
    computed_hashes[i] = computed_hashes[i] if i in computed_hashes else md5('{}{}'.format(salt, i)).hexdigest()
    triplets = get_triplets(computed_hashes[i])
    if triplets:
        for j in xrange(i+1, i+1001):
            computed_hashes[j] = computed_hashes[j] if j in computed_hashes else md5('{}{}'.format(salt, j)).hexdigest()
            if has_5x_repeating(computed_hashes[j], triplets[0]):
                key_count += 1
                if key_count == 64:
                    print i
                    exit()
                break
