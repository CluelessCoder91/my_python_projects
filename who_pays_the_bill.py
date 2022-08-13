import random

name_input = input("Enter everybody's names. Separate by a comma.\n")
names = name_input.split(", ")

num_names = len(names)
random_num = random.randint(0, num_names - 1)
random_name = names[random_num]
print(f"{random_name} pays today!")