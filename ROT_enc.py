def rot_encrypt(text, rotation_factor):
    # Create a mapping of the alphabet to the rotated alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotated_alphabet = alphabet[rotation_factor:] + alphabet[:rotation_factor]
    mapping = {c: r for c, r in zip(alphabet, rotated_alphabet)}

    # Encrypt the text by replacing each letter with the corresponding letter in the rotated alphabet
    encrypted_text = ""
    for c in text:
        encrypted_text += mapping.get(c.upper(), c)

    return encrypted_text

# Get user input
text = input("Enter the text to encrypt: ")
rotation_factor = int(input("Enter the rotation factor: "))

# Encrypt the text
encrypted_text = rot_encrypt(text, rotation_factor)

# Print the encrypted text
print(encrypted_text)
