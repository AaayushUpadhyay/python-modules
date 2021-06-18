import random
 # we should not use this module
 # for security purposes
#  we can use secrets module for that

# To get random values between 0 and 1
value=random.random()


#To get random floating values within a range(endpoints exclusive)
value=random.uniform(1,5)

# To get random integers within a range(endpoints inclusive)
value=random.randint(1,6) # simulating a dice throw
value=random.randint(0,1) # simulating a coin toss --> 0:heads,1:tails

# To pick a random value from a list of values
greetings = ['Hello','Hi','Hola','Howdy','Bye']
value=random.choice(greetings)

# To pick a random value more than once from a list of values
colors=['Red','Green','Blue']
value=random.choices(colors,k=12)
# k is no of times we want random values
# in the above list probability of selection of each element is same (1/3)
# we can change that by using weights
value=random.choices(colors,weights=[9,9,2],k=12)
# now ,P(Red)=9/20,
# now ,P(Green)=9/20,
# now ,P(Blue)=2/20

# To shuffle a list of values like shuffling a deck of cards

deck=list(range(1,53))
random.shuffle(deck)
print(deck)

# To get random unique values everytime from a list
hand=random.sample(deck,k=5)
print(hand)


