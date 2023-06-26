#12 Computing Simple Interest
#using the formula A = P(1 + rt) for simple interest we'll gather our variables from the user input
while True:
    try:
        principal = float(input("Enter the principal: "))
        break
    except ValueError:
        print("Please use numbers only")
        
while True:
    try:
        rate = float(input("Enter the rate of interest: "))
        break
    except ValueError:
        print("Please use numbers only")

while True:
    try:
        years = int(input("Enter the number of years: "))
        break
    except ValueError:
        print("Please use numbers only")
rate2 = rate / 100
total = principal*(1+(rate2*years))
i = 1
while i < 5:
    total = principal*(1+(rate2*i))
    rounded_total = round(total, 2)
    print(f'After {i} years at {rate}%, the  investment will be worth ${rounded_total}')
    i += 1
