name = input("What's your name? ")
sales = input("How much do you sold? ")
sales = int(sales)
commission = sales * 10 / 100
print(f"Hello {name}, your commission is ${round(commission)}")