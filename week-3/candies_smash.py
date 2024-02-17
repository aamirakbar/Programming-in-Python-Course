'''Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

Write an arithmetic expression below to calculate how many candies they must smash for a given haul.'''

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 37
bob_candies = 7
carol_candies = 9

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
total_candies = alice_candies + bob_candies + carol_candies
to_smash = total_candies % 3

#print the number of candies they must smash
print (to_smash)
