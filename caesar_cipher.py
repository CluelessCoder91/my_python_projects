alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Upgrade to make the code shorter and more intuitive
def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
        elif cipher_direction == "decode":
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            end_text += alphabet[new_position]
        elif cipher_direction == "encode":
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
    print(f"The {direction}d text is: {end_text}")


keep_running = True
while keep_running is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    restart = input("Would you like to restart the cipher? Type 'yes' to proceed, 'no' to exit:\n").lower()
    if restart == 'no':
        keep_running = False
        print("Goodbye!")
    else:
        keep_running = True


# def encrypt(plain_text, shift_amount):
#     encrypted_text = ""
#     for i in plain_text:
#         if i == " ":
#             encrypted_text += " "
#         elif i == ".":
#             encrypted_text += "."
#         else:
#             position = alphabet.index(i)
#             new_position = (position + shift_amount) % 26
#             new_letter = alphabet[new_position]
#             encrypted_text += new_letter
#     print(f"The encrypted text is '{encrypted_text}'.")


# def decrypt(cipher_text, shift_amount):
#     decrypted_text = ""
#     for i in cipher_text:
#         if i == " ":
#             decrypted_text += " "
#         elif i == ".":
#             decrypted_text += "."
#         else:
#             position = alphabet.index(i)
#             new_position = (position - shift_amount) % 26
#             new_letter = alphabet[new_position]
#             decrypted_text += new_letter
#     print(f"The decrypted text is '{decrypted_text}'.")


# if direction == "encode":
#     encrypt(plain_text = text, shift_amount = shift)
# elif direction == "decode":
#     decrypt(cipher_text = text, shift_amount = shift)
