import random
# Problem:
    # write a function that calculates how many bills and coins someone would recieve as change.
    # have a function named make_change that accepts two arguments
        #1). total_charge
        #2). payment
    # return a 2-dimensional tuple whose values represent the bills and coins.
    #
    # the first index of the tuple represents bills and has 6 indeces
        # 0 --> singles
        # 1 --> fives
        # 2 --> ten
        # 3 --> twenty
        # 4 --> fifties
        # 5 --> hundred
    # the second index of the tuple represent coins and has 4 indeces
        # 0 --> pennies
        # 1 --> nickels
        # 2 --> dimes
        # 3 --> quarters

#-----------------------------------------------------------------------------------------------
# START FUNCTION SECTION

# function to check if the user inputted a float that is larger than the total bill value
def is_it_number(bill_val):
    while True:
        try:
            some_input = float(input('> '))
            if some_input < bill_val:
                raise ValueError
            else:
                return some_input
        except ValueError:
            print(f'\nInvalid input, please type in a number that is larger than the total bill of ${bill_val}')

# takes the payment minus the bill_val and then calls specific functions that get the bills tuple and then another that gets the coins tuple
# def make_change(payment, bill_val):
    # total_change = payment - bill_val
    # bills = []
    # coins = []

# END FUNCTION SECTION
#-----------------------------------------------------------------------------------------------

# first we will get our random float for the bill or total_charge
total_charge = round(random.random()*100, 2)

# then we will get our user input for the payment
print(f'\nHere is the total charge for your meal:\n${total_charge} \nHow much money would you like to pay?\nDon\'t worry we are really good at making change')
user_input = is_it_number(total_charge)