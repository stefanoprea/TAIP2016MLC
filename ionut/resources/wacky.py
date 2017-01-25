import random
import string

with open('wachy.txt', 'w') as fout:
    for _ in range(10):
        w1 = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 20)))
        w2 = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 20)))
        fout.write('{0}\t{1}\n'.format(w1, w2))

