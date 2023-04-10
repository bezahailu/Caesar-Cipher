alphabet = "abcdefghijklmnopqrstuvwxyz"
num_alpha = len(alphabet)

def encrypt(plaintext, key):
    ciphertext = " "
    for letter in plaintext:
        letter = letter.lower()
        if not letter == " ":
            index = alphabet.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_alpha:
                    new_index -= num_alpha
                ciphertext += alphabet[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = " "
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == " ":
            index = alphabet.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_alpha
                plaintext += alphabet[new_index]
    return plaintext
                                

print("____WELCOME TO THE CAESAR CIPHER PROGRAM____")
print()

print("Would you like to Encrypt or Decrypt the text?")
print()
print("If you want to encrypt, enter 'E'. If you would like to decrypt, enter 'D'.")
user_input = input("E/D: ").upper()
print()

if user_input == "E":
    print("ENCRYPTION SELECTED")
    print()
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to encrypt:" )
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')
    
elif user_input == "D":
    print("DECRYPTION SELECTED")
    print()
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to decrypt:" )
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')






















