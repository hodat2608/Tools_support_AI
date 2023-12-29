from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Hàm để mã hóa email
def encrypt_email(email, secret_key):
    cipher = AES.new(secret_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(email.encode('utf-8'))
    encoded_cipher = base64.b64encode(cipher.nonce + ciphertext + tag).decode('utf-8')
    return encoded_cipher

# Tạo một khóa bí mật (lưu ý rằng bạn cần bảo mật khóa này)
secret_key = get_random_bytes(16)

# Sử dụng hàm encrypt_email để mã hóa email
email = "abc132@gmail.com"
encoded_cipher = encrypt_email(email, secret_key)
print("Email sau khi mã hóa:", encoded_cipher)
