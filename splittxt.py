from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

# Tạo cặp khóa RSA (công khai và riêng tư)
def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Mã hóa email bằng khóa công khai
def encrypt_email(email, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_email = base64.b64encode(cipher.encrypt(email.encode('utf-8')))
    return encrypted_email

# Giải mã email bằng khóa riêng tư
def decrypt_email(encrypted_email, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_email = cipher.decrypt(base64.b64decode(encrypted_email)).decode('utf-8')
    return decrypted_email

# Tạo cặp khóa
private_key, public_key = generate_key_pair()

# Sử dụng hàm encrypt_email để mã hóa địa chỉ email
email_to_encrypt = "datthanho2806@gmail.com"
encrypted_email = encrypt_email(email_to_encrypt, public_key)

# Sử dụng hàm decrypt_email để giải mã địa chỉ email
email_to_encrypt = b'FMBfXFtRwd0Qsymlo3wMrU9597XOaopTc2cj7B5CNT4G77m2bR0f94NM9lYUe9ji4lLTouVMFCkQHpB0blEpbX7mgEMhi1t6yVEAh3YbzQ21CcHXMJV4wiC8oNgPRqV64EQAI8BFtz9KEqWhIzHeep/ki64Yh34ic2j7oyP3iGBS2eVDbo6VtXUxWtMuBcSN9foyGhU+BYX9SbpqsYr6dOtEJSTs85LKFSdEAP4mv6NacPj3hzx7Z5Upwun/VnjBAKeE2ppZZD65L75HTKEftEMFfpHXPfW93gxnkdP+qHT02/QTunv3CYY2xYLnB2xkfOZyVSUNk/kiSKZmvy7FXA=='
decrypted_email = decrypt_email(encrypted_email, private_key)

# print("Email gốc:", email_to_encrypt)
# print("Email đã mã hóa:", encrypted_email)
print("Email đã giải mã:", decrypted_email)
