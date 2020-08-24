# function that accepts a list of numbers as arguments.
# the function should return the smallest number in the list.

import random

# function that checks if the user has inputed a integer or not, if not, it keeps asking
def is_it_integer():
    while True:
        try:
            some_input = int(input('> '))
            return some_input
        except ValueError:
            print('\nInvalid input, please input an integer')

# function that iterates over a list and finds and returns the smallest number in the list
def smallest_numb(some_list):
    # variable to house the most recent smallest number, we initate it with a large number
    smallest_var = 100
    for number in some_list:
        if number < smallest_var:
            smallest_var = number
    return smallest_var

# prompt the user for a upper and lower bounds of the random number generator
print('\nPlease input a number for the upper and lower bounds of the random number generator')
user_input = is_it_integer()

print('\nPlease input a number for the length of the list')
list_length = is_it_integer()

# initiate a list to house our random numbers
random_list = []

# for loops that iterates list length times and adds a new random number into our empty list
for numbers in range(list_length):
    random_list.append(random.randint(-user_input, user_input))

# print out the random list
print(f'Here is the list of random numbers from {-user_input} to {user_input} with a length of {list_length}\n{random_list}')

# call our new function that returns the smallest number
list_smallest_numb = smallest_numb(random_list)

# print the smallest number from teh list
print(f'\nThe smallest number from that list is {list_smallest_numb}')