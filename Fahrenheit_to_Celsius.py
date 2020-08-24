# create a function that converts a temp from Fahrenheit to celsuius
# should return the temp

# converts to celsius and returns the value
def conversion(far):
    return (far -32) * (5/9)

# checks to see if user inputs a number, if not it will keep asking
def is_it_number():
    while True:
        try:
            some_input = float(input('> '))
            return some_input
        except ValueError:
            print('Invalid input, please input a number')

# prompt the user to input a tempterature
print('\nPlease input a temperature you would like to see converted to Celsius from Fahrenheit')
user_input = is_it_number()

# call our conversion fucntion and save the returned value into a new variable
to_cel = conversion(user_input)

# print the new value
print(f'\n\n{user_input} degrees Fahrenheit = {to_cel} degrees Celsius\n\n')