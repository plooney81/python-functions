# function that finds if the user inputed number is odd

# parameter is number, if the remainder of that number divided by two is zero, then we know that the number is even
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

def is_integer():
    while True:
        try:
            some_input = int(input('> '))
            return some_input
        except ValueError:
            print('\nInvalid input, please try again')


# prompt the user for a number
print('\nPlease input a number to see if it is odd or not')
user_input = is_integer()

#call the function is even with the user input as the argument
answer = is_odd(user_input)

# print out the return of the function call
print(f'\nOur function says {answer}\n')