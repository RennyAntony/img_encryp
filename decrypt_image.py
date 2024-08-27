from cryptography.fernet import Fernet

# Function to load the key from the current directory
def load_key():
    return open("secret.key", "rb").read()

# Function to decrypt the image
def decrypt_image(encrypted_image_path):
    # Load the key
    key = load_key()
    fernet = Fernet(key)
    
    # Read the encrypted image as bytes
    with open(encrypted_image_path, "rb") as enc_file:
        encrypted_image = enc_file.read()

    # Decrypt the image
    decrypted_image = fernet.decrypt(encrypted_image)
    
    # Write the decrypted image to a file
    with open("decrypted_image.jpg", "wb") as dec_file:
        dec_file.write(decrypted_image)

if __name__ == "__main__":
    # Decrypt the image
    decrypt_image("encrypted_image.enc")
    print("Image has been decrypted and saved as 'decrypted_image.jpg'.")
