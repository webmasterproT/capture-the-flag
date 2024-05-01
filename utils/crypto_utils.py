```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
import base64
import os

# Shared dependencies
encrypt_data = 'encrypt_data'
decrypt_data = 'decrypt_data'
solve_cipher = 'solve_cipher'

# Constants
SALT_SIZE = 16
KEY_ITERATIONS = 100000
KEY_SIZE = 32
BLOCK_SIZE = AES.block_size

def generate_key(password, salt):
    return PBKDF2(password, salt, dkLen=KEY_SIZE, count=KEY_ITERATIONS)

def encrypt(plaintext, password):
    salt = get_random_bytes(SALT_SIZE)
    key = generate_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), BLOCK_SIZE))
    return base64.b64encode(salt + cipher.iv + ciphertext).decode()

def decrypt(ciphertext, password):
    data = base64.b64decode(ciphertext)
    salt, iv, ciphertext = data[:SALT_SIZE], data[SALT_SIZE:SALT_SIZE+BLOCK_SIZE], data[SALT_SIZE+BLOCK_SIZE:]
    key = generate_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), BLOCK_SIZE)
    return plaintext.decode()

def hash_data(data):
    hasher = SHA256.new()
    hasher.update(data.encode())
    return hasher.hexdigest()

def solve_classic_cipher(ciphertext, cipher_type, key):
    # Placeholder for solving classic ciphers like Caesar, transposition, etc.
    # Implement specific cipher algorithms based on cipher_type and key
    pass

# Example usage:
# encrypted_message = encrypt('Secret Message', 'password123')
# decrypted_message = decrypt(encrypted_message, 'password123')
# hashed_message = hash_data('Sensitive Data')
```