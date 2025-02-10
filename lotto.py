# import the random module, which implements random number generators
import random

# help(random)
# this showed the following information: "randint(a, b) method of Random instance -- return random integer in range [a, b], including both end points"
# but this only gives you one random number between 1-50
# so this method is better: "sample(self, population, k, *, counts=None) -- chooses k unique random elements from a population sequence"
# "To choose a sample from a range of integers, use range() for the population argument"

# create a variable and use the sample method to select 6 integers (defined as the second arg k) from a range of 1 to 51 (range is the first arg)
# state 1 to 51 because the stop value of the range function is not included in the returned output
lottery_numbers = random.sample(range(1, 51),6)

# print the 6 numbers, concatenate the string and the 6 random integers
print("Your lottery numbers are:", lottery_numbers)