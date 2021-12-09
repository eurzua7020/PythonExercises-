#8 Pizza party
while True:
    try:
        people = int(input("How many people?"))
        break
    except ValueError:
        print("Please use whole numbers only")
while True:
    try:
        pizza = int(input("How many pizzas?"))
        break
    except ValueError:
        print("Please use whole numbers only")

slices = (pizza * 8) // people
leftover = (pizza * 8) % people
print(f'{people} people with {pizza} pizzas')
print(f'Each person gets {slices} pieces of pizza.')
print(f'There are {leftover} leftover pieces. ')
