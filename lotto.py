import random
from random import randint, randrange

#print(random.random())
# module Random returns random float between 0.0 and 1.0

print (random.randint(1,50))
# method of printing integer between given parameters
# which are included

#random.sample(sequence, k)
#method of returning the sample of given characters, from the randomly generated range
# first item included, last excluded
lottery=random.sample(range(1,51),6)
print(lottery)
#to print the string instead of a list, with a given separator
print(*lottery,sep=',' )


