import random
from random import randint, randrange

#print(random.random())
# module Random returns random float between 0.0 and 1.0

print (random.randint(1,50))
# method of printing integers between given parameters
# which are included

lottery=random.sample(range(1,51),6)
print(lottery)

