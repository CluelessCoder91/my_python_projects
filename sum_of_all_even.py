total = 0
for number in range(0, 101):
    if number % 2 == 0:
        total += number
print(total)

#  Alternative method:
# total = 0
# for num in range(0, 101, 2):
#     total += num
# print(total)
#  This method adds a 'step' in the function range(). This 'step' allows us to skip a
#  specific value without having to compute the remainder. Handy!