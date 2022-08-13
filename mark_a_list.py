row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
new_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the X mark?\n")
# Here we have to -1 because for normal people, it doesn't
# make sense to start with a zero. To avoid out of range inputs
# we -1 internally with our codes.
col = int(position[0]) - 1  # position[0] is the first digit from the user's input variable named 'position'
row = int(position[1]) - 1  # position[0] is the second digit from the user's input variable named 'position'

new_map[row][col] = "X"
print(f"{row1}\n{row2}\n{row3}")
