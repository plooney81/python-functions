# function that accepts a list of numbers as arguments.
# the function should return the largest number in the list.

import random

# function that checks if the user has inputed a integer or not, if not, it keeps asking
def is_it_integer():
    while True:
        try:
            some_input = int(input('> '))
            return some_input
        except ValueError:
            print('\nInvalid input, please input an integer')

# function that iterates over a list and finds and returns the largest number in the list
def largest_numb(some_list):
    # variable to house the most recent largest number, we initate it with a small number
    largest_var = -100
    for number in some_list:
        if number > largest_var:
            largest_var = number
    # return the largest var
    return largest_var

# prompt the user for a upper and lower bounds of the random number generator
print('\nPlease input a number for the upper and lower bounds of the random number generator')
user_input = is_it_integer()

# prompt the user for the length of our random number list
print('\nPlease input a number for the length of the list')
list_length = is_it_integer()

# initiate a list to house our random numbers
random_list = []

# for loops that iterates list length times and adds a new random number into our empty list
for numbers in range(list_length):
    random_list.append(random.randint(-user_input, user_input))

# print out the random list
print(f'\nHere is the list of random numbers from {-user_input} to {user_input} with a length of {list_length}\n{random_list}')

# call our new function that returns the largest number
list_largest_numb = largest_numb(random_list)

# print the largest number from the list
print(f'\nThe largest number from that list is {list_largest_numb}\n')