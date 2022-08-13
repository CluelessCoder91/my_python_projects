print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N? ").upper()
extra_cheese = input("Do you want extra cheese? Y or N? ").upper()

total_bill = 0
# Small size
if size == "S":  # S = $15
    total_bill = 15
    if add_pepperoni == "Y":  # add pep for S size +$2
        total_bill += 2
    if extra_cheese == "Y":  # add cheese for all size +$1
        total_bill += 1
    else:
        total_bill += 0
else:
    total_bill += 0

# Medium size
if size == "M":  # M = $20
    total_bill = 20
    if add_pepperoni == "Y":  # add pep for M size +$3
        total_bill += 3
    if extra_cheese == "Y":  # add cheese for all size +$1
        total_bill += 1
    else:
        total_bill += 0
else:
    total_bill += 0

# Large size
if size == "L":  # L = $25
    total_bill = 25
    if add_pepperoni == "Y":  # add pep for L size +$2
        total_bill += 3
    if extra_cheese == "Y":  # add cheese for all size +$1
        total_bill += 1
    else:
        total_bill += 0
else:
    total_bill += 0

print(f"Your final bill is: ${total_bill}.")