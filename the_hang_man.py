import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Testing code
# print(chosen_word)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've guessed the letter '{guess}' already. Try again.")
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"The letter '{guess}' is not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"The word is '{chosen_word}'. Game over.")

        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])
