from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import ast
import os
import base64


class Decrypt:
    def __init__(self) -> None:
        pass

    def decrypt_file(self, encrypted_data, key):
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data

    def decrypt_and_write_files(self, encrypted_file, key):
        with open(encrypted_file, 'rb') as f:
            encrypted_files = ast.literal_eval(f.read().decode())

        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"skdnf kandfkaf ajksdhf as dfnajhe laksne fk",
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(key))

        try:
            for file_name, encrypted_data in encrypted_files.items():
                decrypted_data = self.decrypt_file(encrypted_data, key)
                with open("./Home/Decrypted/"+file_name, 'wb') as f:
                    f.write(decrypted_data)
        except:
            return 0

        return 1

if __name__=="__main__":
    # Example usage:
    encrypted_file = "encrypted_files.bin"  # Encrypted file path
    user_key = input("Enter your encryption key: ").encode()  # Taking encryption key from the user

    dec = Decrypt()
    print(dec.decrypt_and_write_files(encrypted_file, user_key))