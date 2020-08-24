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
def make_change(coin_payment, bills_payment):
    bills = []
    coins = []
    bills = make_bills_change(bills_payment)
    coins = make_coins_change(coin_payment)
    return (bills, coins)


def make_bills_change(bills_change):
    # initiate an empty bills_list
    bills_list = [0, 0, 0, 0, 0, 0]
    while bills_change != 0:
        if bills_change >= 100:
            bills_list[-1] += 1
            bills_change -= 100
        elif bills_change >= 50:
            bills_list[-2] += 1
            bills_change -= 50
        elif bills_change >= 20: 
            bills_list[-3] += 1
            bills_change -= 20
        elif bills_change >= 10:
            bills_list[-4] += 1
            bills_change -= 10
        elif bills_change >= 5:
            bills_list[-5] += 1
            bills_change -= 5
        elif bills_change >= 1:
            bills_list[-6] += 1
            bills_change -= 1
    return bills_list

def make_coins_change(coins_change):
    # initiate an empty coins_list
    coins_list = [0, 0, 0, 0]
    rounded_coins = round(coins_change, 2)
    while rounded_coins != 0.00:
        if rounded_coins >= 0.25:
            coins_list[-1] += 1
            rounded_coins -= 0.25
        elif rounded_coins >= 0.10:
            coins_list[-2] += 1
            rounded_coins -= 0.10
        elif rounded_coins >= 0.05:
            coins_list[-3] += 1
            rounded_coins -= 0.05
        elif rounded_coins >= 0.01:
            coins_list[-4] += 1
            rounded_coins -= 0.01
        elif rounded_coins < 0.01:
            rounded_coins = 0.00
            coins_list[-4] += 1
    return coins_list

# END FUNCTION SECTION
#-----------------------------------------------------------------------------------------------

# first we will get our random float for the bill or total_charge
total_charge = round(random.random()*100, 2)

# then we will get our user input for the payment
print(f'\nHere is the total charge for your meal:\n${total_charge} \nHow much money would you like to pay?\nDon\'t worry we are really good at making change')
user_input = is_it_number(total_charge)

# get the total change amount
total_change = user_input - total_charge

# divides up our total_charge into the whole number (for bills_charge) and decimal number (for coins_charge) parts
bills_charge, coins_charge = divmod(total_change, 1)

# we need to round our coins charge again
coins_charge = round(coins_charge, 2)

# print(coins_charge)
# print(bills_charge)
# call the make_change function with the bills_charge and coins_charge as the parameters
answer = make_change(coins_charge, bills_charge)

print(answer)