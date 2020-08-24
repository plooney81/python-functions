# write a function that accepts a list of numbers as an argument
# the function then returns a new list with only the odd numbers from the first list

# function definition
def only_odds(some_list):
    # create a even list that will house only the even numbers from the list given as a parameter
    odd_list = []
    # we then loop over each item in the list and check if the number is odd, if it isn't, then it isn't added to our new odd list
    # if it is odd, then it is appended to our new list
    for params in some_list:
        if params % 2 != 0:
            odd_list.append(params)
    # once we are done looping through the list, then we return our new list with all the even numbers.
    return odd_list

#initiate our first list with some random stuff
combined_list = [1, 2, 3, 4, 5, 6]

new_list = only_odds(combined_list)

# first we print the beginning list
print(f'\nOur beginning list is \n{combined_list}')

# next we print the list with only even numbers
print(f'\nOur new list is \n{new_list}')