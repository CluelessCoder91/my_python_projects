alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    encrypted_text = ""
    for i in plain_text:
        if i == " ":
            encrypted_text += " "
        elif i == ".":
            encrypted_text += "."
        else:
            position = alphabet.index(i)
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            encrypted_text += new_letter
    print(f"The encrypted text is '{encrypted_text}'.")


def decrypt(plain_text, shift_amount):
    decrypted_text = ""
    for i in plain_text:
        if i == " ":
            decrypted_text += " "
        elif i == ".":
            decrypted_text += "."
        else:
            position = alphabet.index(i)
            new_position = (position - shift_amount) % 26
            new_letter = alphabet[new_position]
            decrypted_text += new_letter
    print(f"The decrypted text is '{decrypted_text}'.")


if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decrypt(plain_text = text, shift_amount = shift)
