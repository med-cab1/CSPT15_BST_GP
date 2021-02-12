"""
The game of TicTacToe, while simple for us to understand, 
has quite a few challenges for us to deal with while coding. Things like displaying the game's board, 
allowing players to input moves, updating the game board, detecting a winner, and so on. Beyond this, 
we also have to think about where things might go wrong, 
such as players attempting to play where someone else has already played, 
or playing in a non-existent spot, and so on!

As you may be realizing now, despite the simplicity of TicTacToe, 
there are many smaller intricacies that we have to deal with and handle for that we just take for given when we play on a piece of paper. 
With any task like these where there are many things to be done, we need to just break down the entire objective, 
either in our head or in some notes. In this case, we know we need some basic things:

Visualize the game somehow
Allow players to enter moves
Make sure moves are valid and handle if not.
Determine if there's a winner.
We can tackle these in order, so let's start with #1. How will we visualize this board? I propose, 
to start, we just use lists. In this case, a list of lists. Later, we can convert these lists of lists to be something a bit more pretty, 
but it's going to make more sense for us while programming this to keep it in terms a program understands.

So how might we define our game map? We could start by trying something like:

______________________________________________________________________
game = (0, 0, 0,
        0, 0, 0,
        0, 0, 0)
Clearly that's a 3x3 grid, right? Easy enough!

Well, not so fast there, let's print it out:

print(game)
(0, 0, 0, 0, 0, 0, 0, 0, 0)
>>> 
Also, this is a tuple, so it's immutable and we can't change it over time. 
Thus, we shall use lists!

game = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

print(game)
[0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> 
Still not quite what we wanted yet. 
Let's instead convert this to a list of lists.

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print(game)
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> 



Still flat, but we can see they're now clearly 3 groups. 
How can we separate these out? You might ask.... 
how might we iterate over these?. Ah, a for loop!

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

for row in game:
    print(row)
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
>>> 


So we've got a game board, what's next? We need some way let players play. 
This step has 2 parts. 
  One part is figuring out where exactly the user wants to play, 
  and the other is actually marking that spot on the game's board. 
  In the next tutorial, 
  we're going to cover how we can determine from the user where they wish to play.


"""
# game = [[0, 0, 0,], 
#         [0, 0, 0], 
#         [0, 0, 0]]
# for row in game:        
#     print(row)

"""
Now we're making progress! I think we've got our game board to start.

So my thinking for now is that 0 means no one has played there, 
then we'll use the number 1 for player 1 and number 2 for player 2. Later, 
we can come in and use this list of lists to generate a more pretty version of the game, but, for now, 
this logic should work well.

___________________________________________________________

the next step in a game of TicTacToe would be...
someone wants to play! So, now, 
we have to think of some way for players to input where they want to play. 
Being that this game is text-based and has no real user interface, 
we can't just let players "click" where they want to play. Instead, 
we can utilize the fact that this is a grid, and let players input the position on the grid, 
in a sort of x,y fashion.


                   1  2  3
                1 [0, 0, 0]
                2 [0, 0, 0]
                3 [0, 0, 0]



Now, if we ask the user something like "Where would you like to play? (row, column)," 
the user could input something like 1,2. 
Where would this be? Row 1, column 2. 
So that might be:

       1  2  3
    1 [0, X, 0]
    2 [0, 0, 0]
    3 [0, 0, 0]
"""
"""
Okay. So that's my idea of how I want to do it, 
now we just need to program it! Okay, so this breaks down again. 
Remember a moment ago how the game of TicTacToe was apparently only four steps?

1. Visualize the game somehow
2. Allow players to enter moves
3. Make sure moves are valid and handle if not.
4. Determine if there's a winner.
Well, it turns out.... we're still on step #1 and now we've got some sub steps! A lot of programming is just like this. You come up with the macro steps, then you start working on the macro steps and these have sub-steps that you will need to break down in the same way.

How might we break these ones down? Well, 
we're wanting to add some numbers to the top of the game board, 
and to the side. The top numbers are super simple. We can just...
print them out. Let's do that first!



"""
# game = [[0, 0, 0], 
#         [0, 0, 0], 
#         [0, 0, 0],]

# print("0 1 2")
# for row in game:
#     print(row)



"""
  0 1 2
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]


Note I started with 0, rather than 1. 

In programming, "counting" starts at 0. 
We can start with 1 for the player's visualization, 
but later we'd need to subtract one for their inputs. 
This is totally fine if you want to do that, 
but I'll do it this way to keep it simple for now. 

Okay, what about the right-hand side?

Here's a perfect example of a programmer's ability to do just about anything with basic tools, 
even when there are more advanced tools for this exact purpose. To begin, 
we could create some sort of simple counter.



Before our for loop, we could add in count = 0. 

Then, in the loop, we can print(count, row). 

Then, right under that, do count += 1. 

Whooooaa there what's this += stuff?!?!

Something like count += 1 is the same as doing count = count+1. 
It's just a quick way to add things. You could do count += 5 for example too, 
to add 5 every loop. 
Finally, you can also do all of the other operations like this like *= or -= or /=. 
Okay, back on track here's our code:

"""  


# game = [[0, 0, 0], 
#         [0, 0, 0], 
#         [0, 0, 0],]
# Okay, our top row got out of alignment because we added 
# more text to the rows below it. No big deal, 
# add 2 more spaces:
# print("0 1 2")
# count = 0
# for row in game:
#     print(row) 
#     count += 1
# Nice, looking good! We solved the task just fine. 
# This code is more than fast enough and it's logic is sound. ...
# but there is a better way. This was is with enumerate. 
# Enumerate() is another built-in function with Python, 
# and it's one of the more "fancy" 
# tools that is indeed nice to have and know, 
# but you don't actually need it to get the job done. 
# It does become exceptionally more 
# useful when you intend to iterate over a few iterables together, 
# though there are also many ways (including with fancy tools) to do this too! 
# One thing to learn quickly about programming 
# is that there are many ways to do something, 
# and people get all tribal about *their* way. The bottom line is: 
# make stuff! It's never going to be perfect. 
# Pretty much any code you ever write will have bugs, 
# it will not be as fast as it could be. If you get hung up on this, 
# you'll never actually produce something, and that's a bummer!
# game = [[0, 0, 0], 
#         [0, 0, 0],
#         [0, 0, 0]]
# l = [1, 2, 3, 4, 5]
# l[1] = 99
# print(l)
# print(" 0  1  2")

# for count, row in enumerate(game):
#     print(count, row)
    
    
    #    Result:

#    0  1  2
# 0 [0, 0, 0]
# 1 [0, 0, 0]
# 2 [0, 0, 0]
# >>> 

"""
 Next, we need some way to actually modify the positions. 
 Right now we're assuming all of the zeros are empty, 
 and we'd like to have some way to denote a player actually maintaining one of the positions! 
 
 This has 2 parts to it: 
 actually taking in the player's intentions via some sort of input, and then actually marking. 
 We can do the actual player input later and right now focus on how we'd actually mark the board.

To do this, we're going to use indexing. 
We can use indexes to 

get values or set new ones. Let's see some examples.

let's say we've got a list:

l = [1, 2, 3, 4, 5]


Each item in the list has an index value as we've seen before with our enumerate function that returns index and the item. We start at 0 and go up. So what if we wanted to reference the 2 in this case? That would have an index of one. We can do this by:

print(l[1])
Notice that the index goes inside of square brackets. The output is:

2
>>> 
We can also go backwards with indexes. So right now the 5 has an index of 4. Like so:

l = [1, 2, 3, 4, 5]
print(l[4])
5
>>> 
But we can also reference the 5 with the index of .... -1!

l = [1, 2, 3, 4, 5]
print(l[-1])
5
>>> 
Pretty cool!

While we're here, we might as well see slices. To do a slice, it's just an index to another index and everything in between. We denote this by passing the first index, then a colon, then the ending index. For example:

l = [1, 2, 3, 4, 5]
print(l[2:4])
[3, 4]
>>> 
Finally, we can set values at a certain index. For example:

l = [1, 2, 3, 4, 5]
l[1] = 99
print(l)
[1, 99, 3, 4, 5]
>>> 





In our case, this is a list of lists. 
We need 1 index to reference the specific list we want, 
then we need the index of the item from within that list. 
We can do this by stacking up the indexes. 
Let's see an example. 
Let's pretend we have the following:

"""
# game = [[0, 2, 0],
#         [0, 0, 0],
#         [0, 0, 0]]
# print(game[0][1])
"""
What position is that 2 in? Iterating over game, 
means we iterate FIRST over the lists. So this is in the first list, 
so the one with the index of 0. 
Inside of that list, what's the index of the 2? 1. 
     Okay, so all together, that's: game[0][1]


Great, we can also set values now. 
So let's start with an empty game:



game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
Then set that same spot:

game[0][1] = 2
Then print out our game:

print("   0  1  2")

for count, row in enumerate(game):
    print(count, row)
Full code is:

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

game[0][1] = 2

print("   0  1  2")

for count, row in enumerate(game):
    print(count, row)
Output:

   0  1  2
0 [0, 2, 0]
1 [0, 0, 0]
2 [0, 0, 0]
>>> 




"""
# game = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]
# game[0][1] = 2
# print(" 0 1 2")
# for count, row in enumerate(game):
#     print(count, row)

"""
Our code now looks like:
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print("   0  1  2")
for count, row in enumerate(game):
    print(count, row)

game[0][1] = 2

print("   0  1  2")
for count, row in enumerate(game):
    print(count, row)

-------------------------------------------

So the block of code is repeated twice now already, 
and obviously we can't keep this up for long! 
Any time we find that we've got repetition in our code, 
it should probably be a red flag that you can make it better. 
In this case, the replication is exact, but, even if there are some slight differences, 
you should know to probably use a function to handle for it. So, 
in our case, we can begin defining our function with def then the name, 
then parameters inside of parenthesis, followed by a colon:


def game_board():
In this case, we're not going to pass parameters, 
but we will cover doing this later. Now, for our function, 
we're just going to pass the code that we've been using:

def game_board():
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)
Now, we can call this to run by saying game_board(). 
A common mistake is to forget the parenthesis, and call game_board instead... 
which just points to the function itself, not for it to actually run!

Finally, for us to display the game board, 
make a move, then display it again, 

our code can look like:

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board():
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)


game_board()

game[0][1] = 2

game_board()
Giving us:

   0  1  2
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
   0  1  2
0 [0, 2, 0]
1 [0, 0, 0]
2 [0, 0, 0]
>>> 
Okay, now the moves that we play are also going to be getting repetitive, 
like, the pattern of moving and then calling game_board(). 
Thus, we probably want to just pass the next move as a parameter in the function, 
instead of separate from it. So, 
we're going to use the next tutorial to talk about function parameters!



"""             
# game = [[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]]


# def game_board():
#     print("   0  1  2")
#     for count, row in enumerate(game):
#         print(count, row)


# game_board()

# game[0][1] = 2

# game_board()clear


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