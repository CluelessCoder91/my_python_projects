print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
rounded_bill = round(total_bill, 2)

tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
tip_percentage = tip / 100
total_bill_with_tip = float(rounded_bill + (rounded_bill * tip_percentage))

number_of_people = int(input("How many people to split the bill? "))
even_split = float(total_bill_with_tip) / number_of_people
rounded_even_split = round(even_split, 2)
each_pay = f"Each person should pay: {rounded_even_split}"
print(each_pay)
