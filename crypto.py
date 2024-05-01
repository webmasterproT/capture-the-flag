from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import hashlib

class Cryptography:
    def __init__(self):
        self.block_size = AES.block_size

    def generate_key(self, passphrase):
        salt = get_random_bytes(16)
        key = hashlib.pbkdf2_hmac('sha256', passphrase.encode('utf-8'), salt, 100000)
        return key, salt

    def encrypt_data(self, data, passphrase):
        key, salt = self.generate_key(passphrase)
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), self.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        return {'iv': iv, 'ciphertext': ct, 'salt': b64encode(salt).decode('utf-8')}

    def decrypt_data(self, enc_dict, passphrase):
        salt = b64decode(enc_dict['salt'])
        key = hashlib.pbkdf2_hmac('sha256', passphrase.encode('utf-8'), salt, 100000)
        iv = b64decode(enc_dict['iv'])
        ct = b64decode(enc_dict['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), self.block_size)
        return pt.decode('utf-8')

    def solve_cipher(self, cipher_text, cipher_type, key=None):
        if cipher_type == 'caesar':
            return self.caesar_decrypt(cipher_text, key)
        elif cipher_type == 'transposition':
            return self.transposition_decrypt(cipher_text, key)
        # Add more cipher types as needed
        else:
            raise ValueError("Unsupported cipher type")

    def caesar_decrypt(self, cipher_text, key):
        decrypted = ""
        for char in cipher_text:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - shift - key) % 26 + shift)
            else:
                decrypted += char
        return decrypted

    def transposition_decrypt(self, cipher_text, key):
        # Implement transposition cipher decryption
        pass

# Example usage:
crypto = Cryptography()
passphrase = "securepass"
data = "Sensitive government data"

encrypted = crypto.encrypt_data(data, passphrase)
print("Encrypted:", encrypted)

decrypted = crypto.decrypt_data(encrypted, passphrase)
print("Decrypted:", decrypted)