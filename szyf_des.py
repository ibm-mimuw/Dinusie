from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_des(key, data):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = pad(data.encode(), DES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return encrypted

def decrypt_des(key, encrypted_data):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded = cipher.decrypt(encrypted_data)
    decrypted = unpad(decrypted_padded, DES.block_size)
    return decrypted.decode()

# DES wymaga klucza o długości dokładnie 8 bajtów
key = b'8bytekey'  # Musi być dokładnie 8 bajtów

plain_text = "To jest tajna wiadomość."

# Szyfrowanie
encrypted_data = encrypt_des(key, plain_text)
print("Zaszyfrowane (hex):", encrypted_data.hex())

# Deszyfrowanie
decrypted_text = decrypt_des(key, encrypted_data)
print("Odszyfrowane:", decrypted_text)
