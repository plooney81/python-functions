# write a function shortest that accepts a list of strings as arguments, that returns the shortest string in the list.

# initiate our string list with some names
string_list = ["Pete", "Derek", "Joe", "Jacky", "Katherine"]

# define our function, we will loop over the list that will be given as a parameter
# if the length of a item is longer than the previously longest index, then it will save 
# that word in our variable for longest string
def longest_string_finder(some_list):
    # initiate a variable that holds the longest string, we initate it as a empty string
    string_long = ''
    # for loop that iterates over the some_list parameter
    for strings in some_list:
        # if the length of the current index of the list is longer than the length of string_length, then we save that strings to string_length
        if len(strings) > len(string_long):
            string_long = strings
    
    # after we are done iterating over the list, then we need to return the string_long variable
    return string_long

# call our function with the string_list as the parameter, its saved to a variable named whats_longest
whats_longest = longest_string_finder(string_list)

# print out the initial list
print(f'\nThe list of strings is: \n{string_list}')

# print out the longest string in the list
print(f'\nThe longest string in that list is {whats_longest}, at {len(whats_longest)} characters\n')