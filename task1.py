def caesar_cipher_encrypt(text, shift):
    """Encrypts the given text using the Caesar cipher with the specified shift."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabetic character
            # Determine the ASCII base depending on uppercase or lowercase
            shift_base = ord('A') if char.isupper() else ord('a')
            # Perform the shift and wrap around using modulo
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """Decrypts the given text using the Caesar cipher by encrypting with the negative shift."""
    return caesar_cipher_encrypt(text, -shift)  # Simply call encrypt with the negative shift

def get_valid_shift():
    """Prompts the user for a shift value and validates it."""
    while True:
        try:
            shift = int(input("Enter the shift value (0-25): "))  # Get user input
            if 0 <= shift <= 25:  # Check if the shift is in the valid range
                return shift  # Return the valid shift value
            else:
                print("Please enter a valid shift value between 0 and 25.")  # Error message for out of range
        except ValueError:
            print("Invalid input. Please enter a number.")  # Error message for non-integer input

def main():
    """Main function to run the Caesar cipher program."""
    print("Caesar Cipher Program")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt? ").lower()  # User choice
    message = input("Enter your message: ")  # User message input
    shift = get_valid_shift()  # Get a valid shift value from the user

    # Perform the encryption or decryption based on user choice
    if choice == 'e':
        encrypted_message = caesar_cipher_encrypt(message, shift)  # Encrypt the message
        print(f"Encrypted Message: {encrypted_message}")  # Output the encrypted message
    elif choice == 'd':
        decrypted_message = caesar_cipher_decrypt(message, shift)  # Decrypt the message
        print(f"Decrypted Message: {decrypted_message}")  # Output the decrypted message
    else:
        print("Invalid choice. Please choose 'e' to encrypt or 'd' to decrypt.")  # Error message for invalid choice

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
