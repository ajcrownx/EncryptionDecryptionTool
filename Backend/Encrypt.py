from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

class Encrypt:
    def __init__(self) -> None:
        pass

    def encrypt_file(self, file_path, key):
        with open(file_path, 'rb') as f:
            data = f.read()

        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(data)

        return encrypted_data

    def write_encrypted_file(self, encrypted_data, output_file):
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)
        
        return 1

    def encrypt_multiple_files(self, file_paths, output_file, key):
        encrypted_files = {}

        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"skdnf kandfkaf ajksdhf as dfnajhe laksne fk",
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(key))

        for file_path in file_paths:
            encrypted_data = self.encrypt_file(file_path, key)
            encrypted_files[os.path.basename(file_path)] = encrypted_data

        return self.write_encrypted_file(str(encrypted_files).encode(), output_file)

if __name__=="__main__":
    # Example usage:
    files_to_encrypt = ["file1.txt", "file2.txt"]  # List of file paths to encrypt
    output_encrypted_file = "encrypted_files.bin"  # Output file path for the encrypted data

    user_key = input("Enter your encryption key: ").encode()  # Taking encryption key from the user

    enc = Encrypt()

    print(enc.encrypt_multiple_files(files_to_encrypt, output_encrypted_file, user_key))