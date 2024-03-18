alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
text_len = len(text)

def encrypt(plan_text,shift_amount):
    cipher_text = ""
    for letter in plan_text:
        position = alphabet.index(letter)
        new_position = position-shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)

encrypt(plan_text=text,shift_amount=shift)