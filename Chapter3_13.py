#13 Determining Compound Interest
#using the formula A = P(1 + rt)^(n*t) for compund interest we'll gather our variables from the user input
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
while True:
    try:
        n_number = int(input("What is the number of times the interest is compounded per year?: "))
        break
    except ValueError:
        print("Please use numbers only")

rate2 = rate / 100
exponent = n_number * years
fraction = rate2/n_number
formula = (1+ fraction)**exponent
total = principal*formula
rounded_total = round(total, 2)#the function 'round' helps us round the total and the two specifies the decimal place
print(f'{principal} invested at {rate}% for {years} years compounded {n_number}')
print(f'per year is ${rounded_total}')
