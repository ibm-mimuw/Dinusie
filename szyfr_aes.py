from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt_aes_cryptography(data, key):
    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return iv, ct

def decrypt_aes_cryptography(iv, ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext

if __name__ == "__main__":
    user_input = input("Wprowadź wiadomość do zaszyfrowania: ")
    data = user_input.encode('utf-8')  # Zamiana tekstu na bajty

    key = os.urandom(16)  # 128-bitowy klucz AES

    iv, ct = encrypt_aes_cryptography(data, key)
    print("\nZaszyfrowana wiadomość (hex):", ct.hex())

    decrypted = decrypt_aes_cryptography(iv, ct, key)
    print("Odszyfrowana wiadomość:", decrypted.decode('utf-8'))
