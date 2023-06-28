# import library
import math

# ask user for the calculation they want to do.

print("investment   - to calculate the amount of interest you'll earn on your investment")
print("bond         - to calculate the amount you'll have to pay a home loan")

# Repeat the question until user input either "bond" or "investment"
while True:
    calculation_type = input(
        "Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    if calculation_type == "bond" or calculation_type == "investment":
        print("Thank you, we will proceed with",
              calculation_type.upper(), "calculation.\n\n")
        break
    else:
        print("Please input either 'investment' or 'bond' to proceed.\n\n")
        continue

# Proceed Investment calculation
if calculation_type == "investment":

    # Ask user informations for calculation
    deposit = float(input("Please tell us the amount of deposit : "))
    interest_rate = float(input("Please tell us the interest rate : "))
    period = float(input("How many year you are plan on investing : "))
    interest = input(
        "Which 'simple' or 'compound' interest do you want to calculate : ").lower()

    # check if the calculation method in simple or comound and calculate
    if interest == "simple":
        profit = deposit * (1 + interest_rate/100 * period)
    elif interest == "compound":
        profit = deposit * math.pow((1 + interest_rate/100), period)

    # output the calculation result
    print("\n--------Result-------------\nAmount of deposit:", deposit, "\nInterest rate:", interest_rate,
          "\nYear on investing:", period, "\nInterest:", interest, "\nThe total return of investment is:", round(profit, 2))

# proceed Bond calculation
if calculation_type == "bond":

    # Ask user informations for calculation
    house_value = float(input("What is the present value of the house : "))
    interest_rate = float(input("What is the interest rate : "))
    period = float(
        input("What is the number of months you plan to take to repay the bond : "))

    # calculate the repayment
    repayment = (interest_rate/100/12 * house_value) / \
        (1 - (1 + interest_rate/100/12)**(-period))

    # output the calculation result
    print("\n--------Result-------------\nPresent value of house:", house_value, "\nInterest rate:", interest_rate,
          "\nNumber of months:", period, "\nYou will have to repay (each month):", round(repayment, 2))

