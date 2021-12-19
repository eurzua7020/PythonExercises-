#11 Currency Conversion
while True:
    try:
        euros = float(input("How many euros are you exchanging? "))
        break
    except ValueError:
        print("Please use numbers only")

while True:
    try:
        rate_to_dollars = float(input("What is the exchange rate? "))
        break
    except ValueError:
        print("Please use numbers only")

"""after getting the input from the user we'll do the math to apply the rate.
the exchange rate should be given in the amount of cents i.e. 1 dollar is 100 cents therefore the user will input 100
the math will be multiplying our euros by the rate then divide by 100.
this is not required by the book, but in case the user inputs the exchange rate in whole dollars and not cents I will use an IF statement.
IF the rate is less than 10, it will assume is in whole dollars and not divide by 100. """
if (rate_to_dollars < 10):
    exchanged = round((euros * rate_to_dollars), 2)
    print(f'{euros} euros at an exchange rate of {rate_to_dollars} is')
    print(f'{exchanged} U.S. dollars.')
else:
    exchanged2 = round(((euros * rate_to_dollars) / 100), 2)
    print(f'{euros} euros at an exchange rate of {rate_to_dollars} is')
    print(f'{exchanged2} U.S. dollars.')
