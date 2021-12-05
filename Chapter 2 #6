#6 Retirement calculator
while True:
    try:
        current_age = int(input("what is your current age?"))
        break
    except ValueError:
        print("Please use numbers only")
while True:
    try:
        retire_age = int(input("at what age would you like to retire?"))
        break
    except ValueError:
        print("Please use numbers only")
future_age = retire_age - current_age
#import this module to get the current date
from datetime import date
todays = date.today()
current_year = todays.year
retire_year = current_year + future_age
if future_age > 0:
    print(f'You have {future_age} years left until you can retire.')
    print(f" It's {current_year}, so you can retire in {retire_year}")
else:
    print("According to your plans you can already retire")
