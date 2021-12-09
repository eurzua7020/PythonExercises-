#10  Self-Checkout
while True:
    try:
        price1 = float(input("Enter the price of item 1: "))
        break
    except ValueError:
        print("Please use numbers only")
        
while True:
    try:
        qty1 = float(input("Enter the quantity of item 1: "))
        break
    except ValueError:
        print("Please use numbers only")

while True:
    try:
        price2 = float(input("Enter the price of item 2: "))
        break
    except ValueError:
        print("Please use numbers only")

while True:
    try:
        qty2 = float(input("Enter the quantity of item 2: "))
        break
    except ValueError:
        print("Please use numbers only")
        
while True:
    try:
        price3 = float(input("Enter the price of item 3: "))
        break
    except ValueError:
        print("Please use numbers only")

while True:
    try:
        qty3 = float(input("Enter the quantity of item 3: "))
        break
    except ValueError:
        print("Please use numbers only")

sub1 = price1 * qty1
sub2 = price2 * qty2
sub3 = price3 * qty3
subtotal = round((sub1 + sub2 + sub3), 2)
subtax = subtotal / 100
tax = subtax * 5.5
total = round((subtotal + tax), 2)

print(f'Subtotal: ${subtotal:.2f}')#use :.2f to show the 2 decimal places
print(f'Tax: ${round(tax,2)}')#a different way to show 2 decimal places
print(f'Total: ${total}')
