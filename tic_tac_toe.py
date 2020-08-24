# use nested lists to create a tic tac toe game
    # 1).We need to generate the board
    #   we know that the size of the board is a three
    #   by three grid where players can choose to to place 
    #   an x in any of the squares on the grid
    #   so the grid should look something like this
    # _____|______|_____
    # _____|______|_____
    # _____|______|_____
    # 2). if the player chooses a specific box, then an x is put there
    # 3). once the player chooses a box, then the computer makes a move 
    #     and the user is prompted to make another move

import random
# initiates the list with three, three element lists inside of it
tic_grid = [["","",""],["","",""],["","",""]]

# ------------------------------------------------------------------------------------------------------
# function part of the code

# function that prints our grid the way we want it to look
def print_grid():
    #print the grid the way we want it to look
    for x in range(3):
        for y in range(3):
            # this prints the all of the elements in a row all on one line (this is what the end='' does)
            print(tic_grid[x][y], end='')
        #once we loop through a entire row, then we tell it to go to a new line in the output
        print("\n")


# function that does two things: 1).checks if it is an integer (if it isn't, then a value error with throw when we attempt to convert it into int())
#                                2).checks to see if the integer is between 0 and 2 (if it isn't, then we will raise a value error)
def is_it_integer():
    while True:
        try:
            # if the below code doesn't work then it will go to the except clause 
            # and ask the user for another input
            user_input = int(input('> '))
            if user_input < 0 or user_input > 2:
                # if the integer isn't between 0 and 2, then we raise a value error 
                # and it will got to the except clause and then ask the user for another input
                raise ValueError
            else: 
                # if it is an integer and and it is between 0 and 2, then we return the user_input
                # (the return for functions will automatically break out of our infinite while loop,
                # so we do not need a break statement)
                return user_input
        except ValueError:
            print('\nInvalid input, please input an integer between 0 and 2')

# function that places an X where the user specifies it to
# it has three parameters, row, col, and list_param
# when we call the function we give it the row_val first
# then the col_val
# and finally our current tic_grid list, and the last parameter is the character to place on the board, 
# O for computer and X for the user player.
def place_move(row, col, list_param, char):
    # place an x at the index they inputted
    for x in range(3):
        for y in range(3):
            if (x == row and y == col):
                if y != 2:
                    list_param[x][y] = f'__{char}__|'
                else:
                    list_param[x][y] = f'__{char}__'
    return list_param

# we need to check if that value has already been placed, if so then we need to get new values for the comp_row_val 
# and comp_col_val
def check_move(row, col, list_param, char):
    while True:
        for x in range(3):
            for y in range(3):
                # we find the index in question
                if x == row and y == col:
                    # boolean variable that is true if there aren't any moves in the index [x][y]
                    # will eventually have to put in more lines for if the computer has a move there as well.
                    is_empty = (list_param[x][y] != f'__X__|') and (list_param[x][y] != f'__X__') and (list_param[x][y] != f'__O__|') and (list_param[x][y] != f'__O__')
                    # if our boolean variable is true, then we know the index in question is empty and the move
                    # can be placed there, if not we will have to find another index
                    if is_empty:
                        #place the move onto the grid with the specified character whenever the function was called.
                        return place_move(row, col, list_param, char)
                    elif char == "O":
                        #we need to regenerate the random numbers
                        # generate a random number for the computers row index value, assign it to a variable named comp_row_val
                        row = random.randint(0,2)
                        # generate a random number for the computers column index value, assign it to a variable named comp_col_val
                        col = random.randint(0,2)
                    elif char == "X":
                        # we need to prompt the user for different inputs
                        #ask for user input for the row index
                        print('\nThat index is not empty, please input a new row index')
                        row = is_it_integer()

                        # ask for the user to input our column index
                        print('\nPlease input a new column index')
                        col = is_it_integer()

# this function will check if there is a winner, if there is then it will print out the winner, if not then the code continues to ask for inputs
def check_winner(list_param):
    # initialize a dummy variable that keeps track of if anybody won
    dummy_var = 0
    # set a few variables so we don't have to keep putting those strings for the following checks
    comp_move = '__O__|'
    player_move = '__X__|'
    comp_2_move = '__O__'
    player_2_move = '__X__'
    # first we check the rows  
    for x in range(3):
        y = 0
        if list_param[x][y] == list_param[x][y+1]:
            if list_param[x][y] == comp_move and list_param[x][y+2] == comp_2_move:
                print('The computer has won\n')
                dummy_var += 1
            elif list_param[x][y] == player_move and list_param[x][y+2] == player_2_move:
                print('Congratulations you have won!\n')
                dummy_var += 1
    # the we check the columns
    for y in range(3):
        x = 0
        if list_param[x][y] == list_param[x+1][y] and list_param[x+2][y] == list_param[x][y]:
            if list_param[x][y] == comp_move or comp_2_move:
                print('The computer has won\n')
                dummy_var += 1
            elif list_param[x][y] == player_move or player_2_move:
                print('Congratulations you have won!\n')
                dummy_var += 1
    # then we check the diagonals
    for x in range(3):
        y = 0
        # top left to bottom right
        if x == 0:
            if list_param[x][y] == list_param[x+1][y+1]:
                if list_param[x][y] == comp_move and list_param[x+2][y+2] == comp_2_move:
                    print('The computer has won\n')
                    dummy_var += 1
                elif list_param[x][y] == player_move and list_param[x+2][y+2] == player_2_move:
                    print('Congratulations you have won!\n')
                    dummy_var += 1
        # bottom left to top right
        if x == 2:
            if list_param[x][y] == list_param[x-1][y+1]:
                if list_param[x][y] == comp_move and list_param[x-2][y+2] == comp_2_move:
                    print('The computer has won\n')
                    dummy_var += 1
                elif list_param[x][y] == player_move and list_param[x-2][y+2] == player_2_move:
                    print('Congratulations you have won!\n')
                    dummy_var += 1
                
    # we return the dummy_var
    return dummy_var

def another_player_move(list_param):
    # we then print out the computers move
    print('\nThe computer generated move is:')
    print_grid()

    # Ask the user for another input
    print('\nInput another row index')
    row_val = is_it_integer()

    # ask for the user to input our column index
    print('\nInput another column index')
    col_val = is_it_integer()

    # calls our check_move function that returns an updated tic_grid given we feed it the current row_val, col_val, and tic_grid as parameters
    # we then save the return value back to our tic_grid list
    # call check move
    list_param = check_move(row_val, col_val, list_param, "X")

    return list_param

def another_computer_move(list_param):
    # generate a random number for the computers row index value, assign it to a variable named comp_row_val
    comp_row_val = random.randint(0,2)

    # generate a random number for the computers column index value, assign it to a variable named comp_col_val
    comp_col_val = random.randint(0,2)

    # call check move
    list_param = check_move(comp_row_val, comp_col_val, list_param, "O")

    print('\nThe computer generated move is:')
    print_grid()
    return list_param


# end function part of code
# ------------------------------------------------------------------------------------------------------

# hard code the initiation of an empty grid
# tic_grid = [
    #     [   # 00      01      02
    #         "____|", "____|", "____"
    #     ],
    #     [   # 10      11      12
    #         "____|", "____|", "____"
    #     ],
    #     [   # 20      21      22
    #         "____|", "____|", "____"
    #     ]
    # ]

# welcome to the tic tac game
print('\nWelcome to the tic tac toe game')

# nested loops that initiate our grid like above
for x in range(3):
    for y in range(3):
        if y != 2:
            tic_grid[x][y] = f'_' * 5 + '|'
        else:
            tic_grid[x][y] = f'_' * 5

# shows the empty board
print('\nHere is our empty tic tac toe board\n')
# calls the function to print the grid
print_grid()

# for loop to initiate the grid with the indexes so 
# the user has a way to tell the program which box they would like to make their move into
for x in range(3):
    for y in range(3):
        if y != 2:
            tic_grid[x][y] = f'_{x}_{y}_|'
        else:
            tic_grid[x][y] = f'_{x}_{y}_'

# now we show the boar with indeces
print('\nAnd here is our empty tic tac board with indeces\n')
# calls the function to print our grid
print_grid()

# this explains the game to the user and gives an example of a move
print('\n\nNext you will be able to make a move.')
print('First you will be prompted to choose an index for the row')
print('Then you will be prompted to choose an index for the column')

#example of a move
print('\nSo if we chose to make our move into row 0 column 1, then the grid would look as follows:\n')


# call the function with our example moves as parameters and the current tic_grid list as the last parameter
tic_grid = place_move(0, 1, tic_grid, 'X')

# calls the function to print our grid
print_grid()

# need to git rid of the example move now
for x in range(3):
    for y in range(3):
        if x == 0 and y == 1:
            tic_grid[x][y] = f'_{x}_{y}_|'


# we show the grid with indeces one more time before asking for user input
print('\nHere is the grid again with indeces:\n')
# call our function that prints the grid
print_grid()

#ask for user input for the row index
print('\nInput a row index')
row_val = is_it_integer()

# ask for the user to input our column index
print('\nInput a column index')
col_val = is_it_integer()

# calls our tic_grid function that returns an updated tic_grid given we feed it the current row_val, col_val, and tic_grid as parameters
# we then save the return value back to our tic_grid list
tic_grid = place_move(row_val, col_val, tic_grid, 'X')

print('\nHere is the grid with your move on it\n')
print_grid()

# generate a random number for the computers row index value, assign it to a variable named comp_row_val
comp_row_val = random.randint(0,2)

# generate a random number for the computers column index value, assign it to a variable named comp_col_val
comp_col_val = random.randint(0,2)

# call check move
tic_grid = check_move(comp_row_val, comp_col_val, tic_grid, "O")

# now we need a block that checks if anybody has won yet, will write here and then convert into a function so we can call it later on
# we call the check_winner function to see if anyboy has won yet
is_there_a_winner = check_winner(tic_grid)

# while loop that keeps on calling another move until someone has won
while True:
    if is_there_a_winner == 0:
        tic_grid = another_player_move(tic_grid)
        is_there_a_winner = check_winner(tic_grid)
        if is_there_a_winner == 0:
            tic_grid = another_computer_move(tic_grid)
            is_there_a_winner = check_winner(tic_grid)
        else:
            break
    else:
        break