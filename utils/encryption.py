from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as f:
        f.write(Fernet.generate_key())

with open(KEY_FILE, "rb") as f:
    key = f.read()

cipher = Fernet(key)

def encrypt_message(message):
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(message):
    return cipher.decrypt(message.encode()).decode()