"""This is an example phyton program showing a simple interest calculation
Based on which kind of investement the user want to refer and giving
The amount of deposit, the interest rate, the number of year and
the program will give back the possible earning!"""

import os # import in order to clear the screen
import math
import time



#creating a function for clear the screen
def clearscreen():
    """Clearing the screen function."""
    os.system("cls")




#declaring variable
IS_THE_RIGHT_INPUT = False #using a bool in order to check if the user didn't
#accidentaly digit the wrong input

#showing the possibilities, using a user_input variable to have read
# #the user selection

print("Welcome to your saving plan!\n")
time.sleep(1) # waiting one second in order to show the other messages
print("--------------------------------------------------------------------------------")
print("investement - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan \n")
print("exit - quit the program") # exiting the program


#Checking if the user is typing the right input
while IS_THE_RIGHT_INPUT is False:

    user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed, or exit to quit: ")
    #converting the input into lower case in order to pass the checks
    user_input = user_input.lower()
    if(user_input == "investment") or (user_input == "bond" or user_input == exit):
        IS_THE_RIGHT_INPUT = True
    else:
        print("Your selection doesn't match the options above, try again: ")

#Case investment, reading the deposit, the interest rate and for how many years
#  the investment will be locked
clearscreen()

print(f"Your selection is: {user_input}\n")

if user_input == "investment":
    deposit = int(input("Insert your initial deposit: "))
    interest_rate = int(input("Insert your interest rate: % "))
    #making sure to convert the interest rate in order to calculate the percentage
    interest_rate_percentage = interest_rate / 100
    years = int(input("Number of years that your money will be locked: "))

    #Input the type of investment and lower the string in case of miss typing
    INTEREST = str(input("Are you looking for a 'simple' or 'compound' investment?: "))
    INTEREST = INTEREST.lower()

    clearscreen()

    #CALCULATING THE TYPE OF INTEREST
    if INTEREST == "simple":
        amount = deposit * (1 + (interest_rate_percentage * years))


        print(f"""With a deposit of {deposit} and an interest of {interest_rate}%, your investment should
         reach {amount} in {years} years!""")


    if INTEREST == "compound":
        amount = deposit * math.pow((1 + interest_rate_percentage), years)
        amount = f"{amount:0.2f}" #formatting in order to have only 2 digits for the float
        print(f"""With a deposit of {deposit} and an interest of {interest_rate}%, your investment should
         reach {amount} in {years} years!""")
    #END CALCULATING
        
if user_input == "bond":
    house_value = int(input("Which is the present value of the house?: "))
    interest_rate = int(input("Insert your interest rate: % "))
    years = int(input("Number of years in which you are planning to repay the bond: "))
    monthly_interest_rate = ((interest_rate / 100) / 12) # calculating the monthly interest
    months = years * 12 #Converting the years in months
    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-months)) # calculating the repayment
    repayment = f"{repayment:0.2f}" #formatting in order to have only 2 digits for the float
    print(f"In order to repay the bond in {years} years, you need to pay monthly {repayment}£")








