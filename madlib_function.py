# create a function that accepts two arguments: a name and a subject
# the function should return a string with the name and subject inerpolated in
# the function should have default arguments in case the user has ommitted inputs

# define our function with default arguments of Pete and computer science for name and subject respectively
def madlib(name="Pete", subject="computer science"):
    return f'{name}\'s favorite subject is {subject}'

# prompt the user for name and subject
print('\nPlease input your name')
user_name = input('> ')

print('\nPlease input your favorite subject')
user_subject = input('> ')

# call the madlib function with the two user inputs as the parameters, then we save
# the return of that function into a new variable named string output, which we will then print below
string_output = madlib(user_name, user_subject)
print(f'\n\n{string_output}\n\n')
