import random
test_global = "goodies"

def good() :
    print(test_global)

for i in range(0, 100) :
    print('{} :: {}'.format(i, random.random()))
    print('{} :: {}'.format(i, random.randint(0, 100)))
good()



