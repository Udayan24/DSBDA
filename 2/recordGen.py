# 31117 - Udayan - Script to generate a large number of random records 

from random import *
import secrets
import string

for i in range(49):
    id = 102 + i
    wt = randrange(75, 101)
    cc = randrange(75, 101)
    ai = randrange(75, 101)
    dsbda = randrange(75, 101)

    fNFA = secrets.choice(string.ascii_uppercase)
    fN = ''.join(secrets.choice(string.ascii_lowercase) for i in range(5))
    fNFinal = fNFA+fN

    lNFA = secrets.choice(string.ascii_uppercase)
    lN = ''.join(secrets.choice(string.ascii_lowercase) for i in range(5))
    lNFinal = lNFA+lN

    print("{},{},{},{},{},{},{}".format(id, fNFinal, lNFinal, wt, cc, ai, dsbda))

fNFA = secrets.choice(string.ascii_uppercase)
fN = ''.join(secrets.choice(string.ascii_lowercase) for i in range(6))
fNFinal = fNFA+fN 