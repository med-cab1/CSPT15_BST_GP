# def addition(x, y):
#     return x+y
    #Now we can do something like:

# def addition(x, y):
#     return x+y


# print(addition(5, 6))

# print(addition("Hey", " there"))

# print(addition(5, " there"))
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
def game_board(player, row, column):
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)


def game_board(player, row, column):
    game[row][column] = player
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)

game_board(player=2, row=0, column=0)

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(player, row, column):
    game[row][column] = player
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)


game_board(player=2, row=0, column=0)

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(player=0, row=0, column=0):
    game[row][column] = player
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)


game_board()
game_board(player=2, row=0, column=0)

def game_board(player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)


game_board(just_display=True)
game_board(player=1, row=2, column=1)


# we're going to be covering function parameters.  
# The idea of function parameters is that we can make our functions fairly 
# dynamic by allowing them to take in parameters 
# and do something specific with them. Let's see a basic example.

# Let's say we wanted to make a function that can take 
# in two numbers, and return them summed. That's as simple as:

# Giving us:

# 11
# >>> 
# Cool!

# Just for fun too... what happens if...

# Hey there
# >>> 
# Here's an example of Python's dynamic-typing. In most languages, 
# you need to specify the type of object that can be assigned to a variable, like int, 
# string, a float...etc. In Python, this isn't actually required. 
# There are ways to use static typing with Python, 
# but no one does. At most, people will make use of something called

# Cython

# ... but, for now, enjoy the freedoms of dynamic typing!
# What if we do:

# Traceback (most recent call last):
#   File "C:\Users\H\Desktop\python3-updated-series\part7.py", line 6, in 
#     print(addition(5, " there"))
#   File "C:\Users\H\Desktop\python3-updated-series\part7.py", line 3, in addition
#     return x+y
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>> 
# While we can enjoy dynamic typing, we cannot actually 
# add an int and a string together, 
# because their addition methods are not the same.


# Okay, back to work, let's revisit our game's function:



# So now our game_board accept various parameters, 
# but we're not actually doing anything with them. 
# Let's use them! We can just add a line of game[row][column] = player in the function:

# Now we can play game like:


# Example of a script now:


# output:

#    0  1  2
# 0 [0, 0, 0]
# 1 [0, 0, 0]
# 2 [0, 0, 0]
#    0  1  2
# 0 [2, 0, 0]
# 1 [0, 0, 0]
# 2 [0, 0, 0]
# >>> 
# One issue here is if a player actually 
# does occupy the position at 0,0? The above is going to replace their position. 
# Eventually, we will need to stop overwriting any 
# position there, but, for now, we can also do something like:

#  0  1  2
# 0 [2, 0, 0]
# 1 [0, 0, 0]
# 2 [0, 0, 0]
# >>> 
# It should also be noted that functions can have defaults, 
# or not, or a mixture. For example, we probably 
# want to first print out the empty game board. 
# How might we do that? We could just do an initial for loop and print, 
# or we could pass all 0's to our parameters, but then it might look weird in the code. 
# Instead, we could set 0 as all of the defaults. For example: