# Caesar Cipher

## Description

This Python script implements the Caesar Cipher algorithm, a classic encryption technique where each letter in the plaintext is shifted a fixed number of positions in the alphabet. This script allows you to encrypt and decrypt messages using this method.

## Features

- **Encryption**: Shift each letter in the message forward by the specified number of positions.
- **Decryption**: Shift each letter in the encrypted message backward by the same number of positions.

## Requirements

- Python 3.x

## Installation

No installation is required. Simply ensure that Python 3 is installed on your system.

## Usage

1. **Clone or Download the Repository**:
   - Clone or download the repository to your local machine.

2. **Navigate to the Directory**:
   - Open your terminal and navigate to the directory containing `caesar_cipher.py`:
     ```sh
     cd path/to/your/project
     ```

3. **Run the Script**:
   - Execute the script using Python 3:
     ```sh
     python3 caesar_cipher.py
     ```

4. **Interact with the Script**:
   - The script will prompt you to choose between encryption (`E`) or decryption (`D`).
   - Enter the message you wish to encrypt or decrypt.
   - Provide a numeric shift value. This value determines how many positions each letter will be shifted.

## Examples

### Encryption

```sh
Caesar Cipher Encryption and Decryption
Would you like to Encrypt or Decrypt? (E/D): E
Enter the message: HELLO
Enter the shift value: 3
Encrypted Message: KHOOR
```

### Decryption

```sh
Caesar Cipher Encryption and Decryption
Would you like to Encrypt or Decrypt? (E/D): D
Enter the message: KHOOR
Enter the shift value: 3
Decrypted Message: HELLO
```

## Code Explanation

- `caesar_cipher_encrypt(text, shift)`: Encrypts the text by shifting each letter by the specified shift value.
- `caesar_cipher_decrypt(text, shift)`: Decrypts the text by reversing the shift applied during encryption.
- `main()`: Manages user input and displays the result.
