print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combined_name = name1 + name2
T = 0
R = 0
U = 0
E = 0

L = 0
O = 0
V = 0

for i in combined_name:
    if i == "t":
        T += 1
    elif i == "r":
        R += 1
    elif i == "u":
        U += 1
    elif i == "e":
        E += 1
    elif i == "l":
        L += 1
    elif i == "o":
        O += 1
    elif i == "v":
        V += 1

total_true = T + R + U + E
total_love = L + O + V + E
love_score = int(str(total_true) + str(total_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")