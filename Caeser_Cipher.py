def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            elif char.isupper():
                start = ord('A')
                encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    
    choice = input("Would you like to Encrypt or Decrypt? (E/D): ").upper()
    if choice not in ('E', 'D'):
        print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")
        return
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'E':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)
    elif choice == 'D':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
