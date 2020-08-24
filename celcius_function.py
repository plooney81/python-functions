# create a function that converts celcius to fahrenheit
# the celcius value is a user input

# function should return the fahrenheit value

# one parameter which is celcsius
def cel_to_fahren(cel):
    return (cel * (9/5)) + 32

# function that makes sure the user inputted an integer
def is_it_float():
    while True:
        try:
            some_input = float(input('> '))
            return some_input
        except ValueError:
            print('Invalid input, please input an integer')

# prompt the user to input an integer
print('\nPlease a degree in celsius you would like to see converted to fahrenheit:')
user_input = is_it_float()

# show the user the conversion
conversion = cel_to_fahren(user_input)
print(f'\n\n{user_input} degrees Celsius = {conversion} degrees Fahrenheit\n\n')