# function that accepts a number as an argument and retuns a boolean value
# return true if the number is even; return False if it is not even

# parameter is number, if the remainder of that number divided by two is zero, then we know that the number is even
def is_even(number):
    if number % 2 == 0:
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
print('\nPlease input a number to see if it is even or not')
user_input = is_integer()

#call the function is even with the user input as the argument
answer = is_even(user_input)

# print out the return of the function call
print(f'\nOur function says {answer}\n')